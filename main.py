from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import hashlib, json, os, uuid
from datetime import datetime
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter

app = FastAPI()

STORAGE = "storage"
UPLOADS = "uploaded"
GENERATED = "generated"
os.makedirs(STORAGE, exist_ok=True)
os.makedirs(UPLOADS, exist_ok=True)
os.makedirs(GENERATED, exist_ok=True)

# TSA fake (gera TST simples)
def gerar_tst(hash_hex: str):
    return {
        "tsa": "Prefeitura de Vitorino - TSA Simulada",
        "hash": hash_hex,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "assinatura": "fake-signature-12345"
    }

@app.post("/upload")
async def upload_documento(file: UploadFile = File(...)):
    conteudo = await file.read()
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOADS}/{file_id}.pdf"
    with open(file_path, "wb") as f:
        f.write(conteudo)

    # JSON canônico (metadados simples)
    json_doc = {
        "id": file_id,
        "nome_arquivo": file.filename,
        "tipo": "alvara_funcionamento",
        "data_upload": datetime.utcnow().isoformat() + "Z"
    }

    # Hash SHA-256
    hash_hex = hashlib.sha256(json.dumps(json_doc, sort_keys=True).encode()).hexdigest()

    # Gera TST fake
    tst = gerar_tst(hash_hex)

    # Salva JSON + hash + TST
    registro = {
        "json": json_doc,
        "hash": hash_hex,
        "tst": tst
    }
    with open(f"{STORAGE}/{file_id}.json", "w") as f:
        json.dump(registro, f, indent=4)

    return {"id": file_id, "hash": hash_hex, "tst": tst}

@app.get("/emitir/{file_id}")
async def emitir_pdf(file_id: str):
    storage_file = f"{STORAGE}/{file_id}.json"
    uploaded_pdf = f"{UPLOADS}/{file_id}.pdf"
    output_pdf = f"{GENERATED}/{file_id}.pdf"
    
    if not os.path.exists(uploaded_pdf) or not os.path.exists(storage_file):
        return {"erro": "Documento não encontrado"}

    # Lê o PDF original
    reader = PdfReader(uploaded_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    # Adiciona uma página com o TST
    with open(storage_file, "r") as f:
        registro = json.load(f)
    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Documento Notarizado - TST Simulado", ln=True, align="C")
    pdf.ln(10)

    # Linha de separação
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    # Conteúdo do TST
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"TSA: {registro['tst']['tsa']}", ln=True)
    pdf.cell(0, 8, f"Hash do Documento: {registro['hash']}", ln=True)
    pdf.cell(0, 8, f"Timestamp: {registro['tst']['timestamp']}", ln=True)
    pdf.ln(5)

    # Assinatura fake
    pdf.set_font("Arial", "I", 12)
    pdf.multi_cell(0, 8, f"Assinatura Digital (Simulada): {registro['tst']['assinatura']}")
    pdf.ln(10)

    # Linha final
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    tmp_pdf_path = f"{GENERATED}/{file_id}_tst.pdf"
    pdf.output(tmp_pdf_path)

    # Adiciona a página do TST ao PDF original
    tst_reader = PdfReader(tmp_pdf_path)
    for page in tst_reader.pages:
        writer.add_page(page)

    # Salva PDF final
    with open(output_pdf, "wb") as f:
        writer.write(f)

    return FileResponse(output_pdf, media_type="application/pdf", filename=f"{file_id}.pdf")