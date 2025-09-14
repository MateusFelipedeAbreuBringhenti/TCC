# 🧾 TCC - Trabalho de Conclusão de Curso

![Python](https://img.shields.io/badge/python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-brightgreen)
![Postman](https://img.shields.io/badge/Postman-API%20Test%20-orange)

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

Este projeto, desenvolvido como Trabalho de Conclusão de Curso, cria uma solução prática para emissão de carimbos de tempo digitais, garantindo **autenticidade e integridade** dos documentos. Permite upload de PDFs, geração de JSON com hash, emissão de TST simulado e PDF final combinando o documento original com a página de TST.

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.9+**
* **FastAPI** – Framework moderno para APIs rápidas e seguras.
* **FPDF** – Geração de PDFs reais e estilizados.
* **pypdf** – Manipulação e combinação de PDFs.
* **Postman** – Testes de API.

---

## 🚀 Como Executar

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/MateusFelipedeAbreuBringhenti/TCC
cd TCC
```

### 2️⃣ Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

> Se não existir `requirements.txt`, instale manualmente:

```bash
pip install fastapi uvicorn fpdf pypdf
```

### 4️⃣ Executar a Aplicação

```bash
uvicorn main:app --reload
```

Acesse a aplicação em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **POST /upload** → Upload de PDF
* **GET /emitir/{id}** → Emissão do PDF final com página de TST

---

## 🔤 Siglas e Conceitos

* **TSA (Time-Stamp Authority)** – Autoridade de Carimbo do Tempo. Recebe o hash do documento e devolve o TST.
* **TSP (Time-Stamp Protocol)** – Protocolo definido na RFC 3161.
* **TST (Time-Stamp Token)** – Token emitido pela TSA, com hash, timestamp e assinatura.
* **CRL (Certificate Revocation List)** – Lista de certificados revogados.
* **OCSP (Online Certificate Status Protocol)** – Verifica em tempo real a validade de certificados.
* **PKI (Public Key Infrastructure)** – Infraestrutura de Chaves Públicas.
* **CA (Certification Authority)** – Autoridade Certificadora.
* **RA (Registration Authority)** – Autoridade de Registro.
* **CSR (Certificate Signing Request)** – Requisição de assinatura de certificado.
* **X.509** – Padrão de certificados digitais.
* **LTV (Long-Term Validation)** – Validação de longo prazo de assinaturas/carimbos.
* **ICP-Brasil** – Infraestrutura nacional de certificação digital.

---

## 📝 Referências

1. RFC 3161 - [Time-Stamp Protocol (TSP)](https://www.rfc-editor.org/rfc/rfc3161)
2. FastAPI - [FastAPI Documentation](https://fastapi.tiangolo.com/)
3. FPDF - [FPDF Python Library](https://pyfpdf.github.io/fpdf2/)
4. PYPDF - [pypdf Documentation](https://pypdf.readthedocs.io/)
