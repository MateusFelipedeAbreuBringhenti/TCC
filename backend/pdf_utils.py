import json
from hashlib import sha256
from typing import Tuple
from backend.tsa_service import verificar_tst

def verificar_tst_conteudo(pdf_path: str, tst_path: str) -> Tuple[bool, dict]:
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    with open(tst_path, "r", encoding="utf-8") as f:
        tst = json.load(f)

    valido = verificar_tst(pdf_bytes, tst)
    return valido, tst