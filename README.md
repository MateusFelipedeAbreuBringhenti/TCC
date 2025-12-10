# 🧾 TCC - Trabalho de Conclusão de Curso

![Python](https://img.shields.io/badge/python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-brightgreen)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)

---

> **Descrição breve:**  
> Este projeto implementa uma **Autoridade de Carimbo do Tempo (TSA)** baseada no protocolo **RFC 3161**, garantindo a **autenticidade, integridade e validade temporal** de documentos digitais.

---

## 📌 Índice

1. [Sobre](#sobre)  
2. [Objetivos do Projeto](#objetivos-do-projeto)  
3. [Arquitetura e Estrutura](#arquitetura-e-estrutura)  
4. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
5. [Como Executar](#como-executar)  
6. [Fluxo do Sistema](#fluxo-do-sistema)  
7. [Siglas e Conceitos](#siglas-e-conceitos)  
8. [Autor](#autor)  
9. [Referências](#referências)

---

## 📝 Sobre

Este projeto é parte do **Trabalho de Conclusão de Curso** de Tecnologia da Informação na **UniMater**.  
O objetivo é criar uma solução prática e funcional que simula o funcionamento de uma **TSA (Time-Stamp Authority)** — entidade responsável por emitir carimbos de tempo digitais, permitindo comprovar a **existência e integridade de arquivos** em um momento específico.

---

## 🎯 Objetivos do Projeto

- Garantir a **integridade** de documentos digitais através de **hashes criptográficos (SHA-256)**.  
- Implementar **assinatura digital** com chaves assimétricas (RSA).  
- Enviar os hashes para uma **TSA** simulada via **API**, que devolve um **TST (Time-Stamp Token)**.  
- Permitir a **verificação posterior** do documento, confirmando se ele foi alterado.  
- Demonstrar na prática conceitos de **PKI (Infraestrutura de Chaves Públicas)** e **segurança da informação**.  

---

## 🧩 Arquitetura e Estrutura

O sistema é dividido em duas camadas principais:

- **Backend (API)**: responsável pela canonização de JSON, geração de hash, assinatura digital e emissão do carimbo de tempo (TST).  
- **Frontend (Interface)**: em desenvolvimento, permitirá o envio e verificação de documentos de forma amigável.  

A comunicação entre os módulos segue o padrão HTTP/JSON, utilizando o framework **FastAPI**.  

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.9+**  
- **FastAPI** – Framework moderno para construção de APIs.    
- **Cryptography** – Biblioteca de criptografia para geração e verificação de assinaturas.
-     
- **Requests** – Para comunicação com a TSA simulada.  

---

## 🚀 Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/MateusFelipedeAbreuBringhenti/TCC
cd TCC
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
```bash
<<<<<<< HEAD
Copiar código
uvicorn backend.main:app --reload
Acesse em: http://localhost:8000/docs
=======
uvicorn main:app --reload
Acesse em: http://localhost:8000
>>>>>>> 7dca36239901ad963884ff4e44af8ef4c5795aa6
```

---

## 🔄 Fluxo do Sistema
O usuário envia um arquivo JSON.

O sistema canoniza e gera o hash SHA-256.

O hash é assinado digitalmente com a chave privada.

O hash é enviado para a TSA, que retorna o carimbo de tempo (TST).

O TST é armazenado e pode ser verificado futuramente.

Em uma verificação, o sistema confirma:

Se o hash atual bate com o original.

Se a assinatura é válida.

Se o carimbo é autêntico e dentro do prazo.

---

## 🔤 Siglas e Conceitos

TSA (Time-Stamp Authority)
Autoridade de Carimbo do Tempo, é a entidade confiável que recebe o hash do documento e devolve o carimbo do tempo assinado

TSP (Time-Stamp Protocol)
Protocolo de Carimbo do Tempo, definido na RFC 3161, regras de como o hash deve ser enviado para a TSA e como o carimbo é devolvido

TST (Time-Stamp Token)
O token emitido pela TSA, contém o hash, a data/hora e a assinatura digital da TSA, provando que o documento existia naquele momento

CRL (Certificate Revocation List)
Lista de Certificados Revogados, é publicada pela Autoridade Certificadora para informar que um certificado foi cancelado antes da expiração

OCSP (Online Certificate Status Protocol)
Protocolo que permite verificar em tempo real se um certificado é válido ou foi revogado, sem precisar baixar toda a CRL

PKI (Public Key Infrastructure)
Infraestrutura de Chaves Públicas, conjunto de tecnologias, políticas e procedimentos que suportam certificados digitais

CA (Certification Authority)]
Autoridade Certificadora, emite e gerencia certificados digitais

RA (Registration Authority)
Autoridade de Registro, faz a validação da identidade antes da emissão do certificado pela CA

CSR (Certificate Signing Request)
Requisição de Assinatura de Certificado, arquivo gerado quando alguém pede um certificado digital para uma CA

X.509
Padrão de certificados digitais usado em PKI, todos os certificados, inclusive os da TSA, seguem esse formato

LTV (Long-Term Validation)
Validação de Longo Prazo, técnica para garantir que assinaturas/carimbos continuem válidos mesmo anos depois

ICP-Brasil
Infraestrutura de Chaves Públicas Brasileira, sistema nacional que regula a certificação digital no Brasil

---

## 👨‍💻 Autor

> Mateus Felipe de Abreu Bringhenti
> 
> 📘 UniMater – Trabalho de Conclusão de Curso 2025
> 
> 📅 Data de entrega: A definir

---

## 📚 Referências

RFC 3161 – Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)

ICP-Brasil – Documentos e Políticas de Certificação

....

---
