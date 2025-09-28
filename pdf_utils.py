# pdf_utils.py
import json
from hashlib import sha256
from typing import Tuple
from tsa_service import verificar_tst

def verificar_tst_conteudo(pdf_path: str, tst_path: str) -> Tuple[bool, dict]:
    # Lê bytes do PDF
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    # Lê tst json
    with open(tst_path, "r", encoding="utf-8") as f:
        tst = json.load(f)

    # Usa função do tsa_service (verifica hash+assinatura)
    valido = verificar_tst(pdf_bytes, tst)
    return valido, tst