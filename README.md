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

Este projeto será desenvolvido como Trabalho de Conclusão de Curso e tem como objetivo criar uma solução prática para emissão de carimbos de tempo digitais, garantindo **autenticidade e integridade** dos documentos.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI** – Framework moderno para APIs rápidas e seguras.
- **Flask** – Micro framework web em Python.
- **Docker** – Containerização para fácil deploy e reprodução do ambiente.

---

## 🚀 Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/MateusFelipedeAbreuBringhenti/TCC
```

2. Criar e Ativar o Ambiente Virtual
```bash

```
3. Instalar Dependências

```bash

```
4. Executar a Aplicação
```bash

```
Acesse a aplicação em http://localhost:8000.

---

## 🔤 Siglas e Conceitos

**TSA (Time-Stamp Authority)**

Autoridade de Carimbo do Tempo, é a entidade confiável que recebe o hash do documento e devolve o carimbo do tempo assinado

**TSP (Time-Stamp Protocol)**

Protocolo de Carimbo do Tempo, definido na RFC 3161, regras de como o hash deve ser enviado para a TSA e como o carimbo é devolvido

**TST (Time-Stamp Token)**

O token emitido pela TSA, contém o hash, a data/hora e a assinatura digital da TSA, provando que o documento existia naquele momento

**CRL (Certificate Revocation List)**

Lista de Certificados Revogados, é publicada pela Autoridade Certificadora para informar que um certificado foi cancelado antes da expiração

**OCSP (Online Certificate Status Protocol)**

Protocolo que permite verificar em tempo real se um certificado é válido ou foi revogado, sem precisar baixar toda a CRL

**PKI (Public Key Infrastructure)**

Infraestrutura de Chaves Públicas, conjunto de tecnologias, políticas e procedimentos que suportam certificados digitais

**CA (Certification Authority)**]

Autoridade Certificadora, emite e gerencia certificados digitais

**RA (Registration Authority)**

Autoridade de Registro, faz a validação da identidade antes da emissão do certificado pela CA

**CSR (Certificate Signing Request)**

Requisição de Assinatura de Certificado, arquivo gerado quando alguém pede um certificado digital para uma CA

**X.509**

Padrão de certificados digitais usado em PKI, todos os certificados, inclusive os da TSA, seguem esse formato

**LTV (Long-Term Validation)**

Validação de Longo Prazo, técnica para garantir que assinaturas/carimbos continuem válidos mesmo anos depois

**ICP-Brasil**

Infraestrutura de Chaves Públicas Brasileira, sistema nacional que regula a certificação digital no Brasil

## 📝 Referências

Blablablabla


