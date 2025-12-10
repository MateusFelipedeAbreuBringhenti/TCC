from backend.database import SessionLocal, Documento, init_db
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from io import BytesIO
import os
import shutil
import zipfile
import json

from backend.tsa_service import gerar_tst
from backend.pdf_utils import verificar_tst_conteudo

init_db()

app = FastAPI(title="Autoridade de Carimbo do Tempo - TSA")

UPLOAD_DIR = "uploads"
RESULT_DIR = "results"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

@app.post("/carimbar/")
async def carimbar_documento(file: UploadFile):
    
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    with open(file_location, "rb") as f:
        conteudo = f.read()

    tst = gerar_tst(conteudo)

    output_pdf = os.path.join(RESULT_DIR, f"carimbado_{file.filename}")
    shutil.copy(file_location, output_pdf)

    output_tst = os.path.join(RESULT_DIR, f"{file.filename}.tst.json")
    with open(output_tst, "w", encoding="utf-8") as f:
        json.dump(tst, f, ensure_ascii=False, indent=4)

    zip_path = os.path.join(RESULT_DIR, f"{file.filename}_carimbado.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(output_pdf, f"carimbado_{file.filename}")
        zipf.write(output_tst, f"{file.filename}.tst.json")

    return FileResponse(zip_path, filename=f"{file.filename}_carimbado.zip")


@app.post("/verificar/")
async def verificar_documento(pdf: UploadFile, tst_file: UploadFile):
    
    pdf_path = os.path.join(UPLOAD_DIR, pdf.filename)
    with open(pdf_path, "wb") as f:
        shutil.copyfileobj(pdf.file, f)

    tst_path = os.path.join(UPLOAD_DIR, tst_file.filename)
    with open(tst_path, "wb") as f:
        shutil.copyfileobj(tst_file.file, f)

    try:
        valido, tst = verificar_tst_conteudo(pdf_path, tst_path)
        return {"valido": valido, "tst": tst}
    except Exception as e:
        return {"valido": False, "erro": str(e)}
    

@app.post("/salvar/")
async def salvar_no_banco(pdf: UploadFile = File(...), tst_file: UploadFile = File(...)):
 
    pdf_path = os.path.join(UPLOAD_DIR, pdf.filename)
    tst_path = os.path.join(UPLOAD_DIR, tst_file.filename)

    with open(pdf_path, "wb") as f:
        shutil.copyfileobj(pdf.file, f)
    with open(tst_path, "wb") as f:
        shutil.copyfileobj(tst_file.file, f)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(pdf_path, arcname=pdf.filename)
        zipf.write(tst_path, arcname=tst_file.filename)

    zip_buffer.seek(0)
    zip_bytes = zip_buffer.read()

    with open(tst_path, "r", encoding="utf-8") as f:
        tst_data = json.load(f)

    db = SessionLocal()
    doc = Documento(
        nome_arquivo=pdf.filename,
        binario=zip_bytes,
        tst=tst_data
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    db.close()

    return {"mensagem": "Documento salvo com sucesso!", "id": doc.id}


@app.post("/reconstruir/{id}/")
async def reconstruir_documento(id: int):
    db = SessionLocal()
    doc = db.query(Documento).filter(Documento.id == id).first()
    db.close()

    if not doc:
        return {"erro": "Documento não encontrado."}

    zip_buffer = BytesIO(doc.binario)
    with zipfile.ZipFile(zip_buffer, "r") as zipf:
        zipf.extractall(RESULT_DIR)

    tst_path = os.path.join(RESULT_DIR, f"recuperado_{doc.nome_arquivo}.tst.json")
    with open(tst_path, "w", encoding="utf-8") as f:
        json.dump(doc.tst, f, ensure_ascii=False, indent=4)

    pdf_files = [f for f in os.listdir(RESULT_DIR) if f.endswith(".pdf")]
    if not pdf_files:
        return {"erro": "Nenhum PDF encontrado dentro do binário."}

    pdf_path = os.path.join(RESULT_DIR, pdf_files[0])
    return FileResponse(pdf_path, filename=f"recuperado_{pdf_files[0]}")