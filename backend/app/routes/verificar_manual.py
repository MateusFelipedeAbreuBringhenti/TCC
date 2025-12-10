import json
import hashlib
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.tsa_service import verificar_tst

router = APIRouter()

@router.post("/verificar-manual")
async def verificar_manual(
    arquivo: UploadFile = File(...),
    tst: UploadFile = File(...)
):
    # lê arquivo original
    conteudo = await arquivo.read()
    if len(conteudo) == 0:
        raise HTTPException(status_code=400, detail="Arquivo vazio.")

    # lê TST
    tst_bytes = await tst.read()
    try:
        tst_json = json.loads(tst_bytes.decode())
    except:
        raise HTTPException(status_code=400, detail="TST inválido ou corrompido.")

    # validação real
    valido = verificar_tst(conteudo, tst_json)

    return {
        "arquivo": arquivo.filename,
        "tst": tst.filename,
        "valido": valido,
        "hash_arquivo": hashlib.sha256(conteudo).hexdigest(),
        "hash_tst": tst_json.get("hash"),
        "timestamp": tst_json.get("timestamp"),
        "autoridade": tst_json.get("tsa"),
        "mensagem": "Documento válido." if valido else "Documento inválido."
    }
