# 🧾 TCC - Trabalho de Conclusão de Curso

![Python](https://img.shields.io/badge/python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-brightgreen)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-orange)

---

> **Descrição breve:** Este projeto implementa uma Autoridade de Carimbo do Tempo (TSA) usando o protocolo RFC 3161, garantindo segurança e integridade de documentos digitais.

---

## 📌 Índice

1. [Sobre](#sobre)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Como Executar](#como-executar)
4. [Siglas e Conceitos](#siglas-e-conceitos)
5. [Referências](#referências)

---

## 📝 Sobre

Este projeto foi desenvolvido como Trabalho de Conclusão de Curso e tem como objetivo criar uma solução prática para emissão de carimbos de tempo digitais, garantindo **autenticidade e integridade** dos documentos.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI** – Framework moderno para APIs rápidas e seguras.
- **Flask** – Micro framework web em Python.
- **Docker** – Containerização para fácil deploy e reprodução do ambiente.

---

## 🚀 Como Executar

### 1. Clonar o Repositório

```
git clone https://github.com/MateusFelipedeAbreuBringhenti/TCC.git
cd TCC
```

2. Criar e Ativar o Ambiente Virtual
```
bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. Instalar Dependências

```bash
Copiar código
pip install -r requirements.txt
```
4. Executar a Aplicação
```bash
Copiar código
uvicorn main:app --reload
```
Acesse a aplicação em http://localhost:8000.

🔤 Siglas e Conceitos
TSA: Time-Stamp Authority – Autoridade de Carimbo do Tempo.

TSP: Time-Stamp Protocol – Protocolo de Carimbo do Tempo.

TST: Time-Stamp Token – Token de Carimbo do Tempo.

CRL: Certificate Revocation List – Lista de Certificados Revogados.

OCSP: Online Certificate Status Protocol – Protocolo de Status de Certificado Online.


