import os
import json
import hashlib
import base64
from datetime import datetime
from typing import Dict

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend

KEYS_DIR = "keys"
PRIVATE_KEY_PATH = os.path.join(KEYS_DIR, "private_key.pem")
PUBLIC_KEY_PATH = os.path.join(KEYS_DIR, "public_key.pem")


def _ensure_keys_exist(key_size: int = 2048):
    
    os.makedirs(KEYS_DIR, exist_ok=True)
    if os.path.exists(PRIVATE_KEY_PATH) and os.path.exists(PUBLIC_KEY_PATH):
        return

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL, 
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open(PUBLIC_KEY_PATH, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


def _load_private_key():
    with open(PRIVATE_KEY_PATH, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())


def _load_public_key():
    with open(PUBLIC_KEY_PATH, "rb") as f:
        return serialization.load_pem_public_key(f.read(), backend=default_backend())


def gerar_tst(conteudo_bytes: bytes) -> Dict:

    _ensure_keys_exist()

    hash_hex = hashlib.sha256(conteudo_bytes).hexdigest()
    digest = hashlib.sha256(conteudo_bytes).digest()

    timestamp = datetime.utcnow().isoformat() + "Z"

    private_key = _load_private_key()
    signature = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    signature_b64 = base64.b64encode(signature).decode("utf-8")

    tst = {
        "tsa": "Prefeitura XXX - TSA Simulada",
        "hash": hash_hex,
        "timestamp": timestamp,
        "assinatura": signature_b64
    }
    return tst


def verificar_tst(conteudo_bytes: bytes, tst: Dict) -> bool:

    _ensure_keys_exist()
    public_key = _load_public_key()

    calc_hash_hex = hashlib.sha256(conteudo_bytes).hexdigest()
    if calc_hash_hex != tst.get("hash"):
        return False
    
    signature_b64 = tst.get("assinatura")
    if not signature_b64:
        return False

    try:
        signature = base64.b64decode(signature_b64)
    except Exception:
        return False

    digest = hashlib.sha256(conteudo_bytes).digest()

    try:
        public_key.verify(
            signature,
            digest,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False