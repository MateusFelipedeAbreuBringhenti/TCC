from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import os
import shutil
import zipfile
import json

from tsa_service import gerar_tst
from pdf_utils import verificar_tst_conteudo

app = FastAPI(title="Autoridade de Carimbo do Tempo - TSA")

UPLOAD_DIR = "uploads"
RESULT_DIR = "results"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)


@app.post("/carimbar/")
async def carimbar_documento(file: UploadFile):
    
    # Salva PDF original
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Lê bytes do PDF original
    with open(file_location, "rb") as f:
        conteudo = f.read()

    # Gera TST (assina o digest com RSA)
    tst = gerar_tst(conteudo)

    # Salva PDF carimbado (mantém o pdf original bytes)
    output_pdf = os.path.join(RESULT_DIR, f"carimbado_{file.filename}")
    shutil.copy(file_location, output_pdf)

    # Salva o TST em JSON
    output_tst = os.path.join(RESULT_DIR, f"{file.filename}.tst.json")
    with open(output_tst, "w", encoding="utf-8") as f:
        json.dump(tst, f, ensure_ascii=False, indent=4)

    # Cria um zip com os dois arquivos
    zip_path = os.path.join(RESULT_DIR, f"{file.filename}_carimbado.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(output_pdf, f"carimbado_{file.filename}")
        zipf.write(output_tst, f"{file.filename}.tst.json")

    return FileResponse(zip_path, filename=f"{file.filename}_carimbado.zip")


@app.post("/verificar/")
async def verificar_documento(pdf: UploadFile, tst_file: UploadFile):
    
    # Salva arquivos enviados
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