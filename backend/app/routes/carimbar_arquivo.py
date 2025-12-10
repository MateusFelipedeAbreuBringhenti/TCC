import json
from fastapi import APIRouter, UploadFile, File, HTTPException, Response

from app.database import SessionLocal
from app.models.documento import Documento
from app.services.tsa_service import gerar_tst
from app.utils.zip_utils import criar_zip

router = APIRouter()

@router.post("/carimbar-arquivo")
async def carimbar_arquivo(arquivo: UploadFile = File(...)):
    conteudo = await arquivo.read()

    if len(conteudo) == 0:
        raise HTTPException(status_code=400, detail="Arquivo vazio.")

    # hash real do arquivo
    canon = conteudo

    # gera o TST
    tst = gerar_tst(canon)
    tst_bytes = json.dumps(tst, ensure_ascii=False, indent=4).encode()

    # cria o ZIP com conteúdo original + tst.json
    zip_bytes = criar_zip(canon, tst_bytes, nome_original=arquivo.filename)

    # salva no banco
    db = SessionLocal()
    doc = Documento(
        nome=arquivo.filename,
        zip_bin=zip_bytes,
        tst=tst
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    db.close()

    # devolve o ZIP diretamente pro usuário
    return Response(
        content=zip_bytes,
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename=carimbado_{doc.id}.zip"
        }
    )
