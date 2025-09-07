# **Artigo / TCC**

Vídeo para decidir Fastapi x flask

https://www.youtube.com/watch?v=9kyZMUqwM9U


##### **Siglas**



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



---



##### **Termos técnicos utilizados / roteiro (em ordem)**





\## **JSON Canônico (JCS-like)**



JSON comum vai permitir variações (espaços, ordem das chaves, etc.), o que mudaria o hash

Canonização determinística (JCS – JSON Canonicalization Scheme) vai garantir que os dados iguais, sempre geram o mesmo JSON byte a byte



Exemplo



&nbsp; json

&nbsp; {"nome":"Mateus","idade":25}



&nbsp; e



&nbsp; json

&nbsp; { "idade":25 , "nome":"Mateus" }



&nbsp; -> viram a mesma string canônica antes do hash, assim o hash sempre será consistente



---



\## **Hashing (SHA-256)**



Função criptográfica que vai transformar os dados em um resumo único de 256 bits (um hash fixo de 64 caracteres hexadecimais) site https://site112.com/gerador-hash

&nbsp; Propriedades:



&nbsp; \* Integridade -> qualquer alteração mínima muda todo o hash

&nbsp; \* Irreversibilidade -> não dá pra voltar do hash pro original

&nbsp; \* Resistência a colisões -> extremamente improvável que dois documentos diferentes tenham o mesmo hash



Exemplo prático:



&nbsp; "Mateus" → "6bf60d4084ebb84ff32e834a4e75fc0b46160f886572cb2a471eede5304473b0" 



---



\## **Carimbo do Tempo (RFC 3161 / TSP)**



Time-Stamp Protocol (TSP) protocolo para provar quando um dado existia

&nbsp; Processo:



&nbsp; 1. O sistema gera o hash do documento

&nbsp; 2. Envia esse hash para a Time-Stamp Authority (TSA)

&nbsp; 3. A TSA devolve um Time-Stamp Token (TST), assinado digitalmente, com:



&nbsp; \* Hash recebido

&nbsp; \* Data e hora UTC precisa

&nbsp; \* Identificação da TSA



Esse token pode ser validado a qualquer momento e prova que o dado já existia naquela data



---



\## **PKI (Public Key Infrastructure)**



Infraestrutura de certificados digitais que garante confiança

&nbsp; Elementos principais:



&nbsp; \* Certificado digital -> identifica a chave pública de alguém

&nbsp; \* Cadeia de certificação -> certificado raiz → intermediário → TSA

&nbsp; \* Revogação -> se um certificado for comprometido, entra em CRL (Certificate Revocation List) ou é checado em tempo real por OCSP (Online Certificate Status Protocol)



No meu sistema...



&nbsp; \* Serve pra validar a assinatura da TSA no carimbo

&nbsp; \* Garante que o TST não foi emitido por uma autoridade falsa ou comprometida

&nbsp; \* Algo a mais???????



---



\## **BoV (Build-on-Verify)**



Princípio de construção sob demanda

&nbsp; O documento (PDF final) só é gerado após a verificação de



&nbsp; \* Hash calculado corretamente

&nbsp; \* TST válido e assinado por TSA confiável

&nbsp; \* Cadeia PKI íntegra e não revogada



Benefício: o sistema não guarda PDFs prontos, apenas JSON + TST

Isso garante sigilo, privacidade e segurança, reduzindo riscos de vazamento



---



\## **Protótipo (Implementação)**



\* Linguagem: Python

\* API REST: Flask ou FastAPI

\* Hashing: hashlib (SHA-256)

\* PKI / Assinaturas: cryptography + OpenSSL

\* Requisição TSA: POST com hash -> recebe TST

\* Validação: utilitário offline pra checar assinatura TSA, cadeia PKI, OCSP/CRL

\* Autenticação: login simples antes de permitir a geração do PDF

\* Armazenamento: só guarda JSON + TST, sem PDF final



---



##### **Roteiro de Funcionamento da Solução (expectativa né)**



**Entrada de dados**

&nbsp; O usuário fornece um documento (ou dados) em JSON canônico



**Canonização + Hash**

&nbsp; O sistema aplica canonização determinística (JCS-like)

&nbsp; Gera o hash SHA-256 do JSON



**Requisição à TSA (TSP – RFC 3161)**

&nbsp; O hash é enviado à Time-Stamp Authority (TSA) via protocolo TSP

&nbsp; A TSA devolve o Time-Stamp Token (TST), contendo hash + data/hora + assinatura digital



**Validação (PKI)**

&nbsp; O sistema valida a assinatura do TST

&nbsp; Cadeia de certificados da TSA (X.509)

&nbsp; Status de revogação (OCSP/CRL)



**Autenticação do usuário**

&nbsp; Somente após login/autenticação válida, o sistema autoriza a geração do PDF



**Geração do PDF sob demanda (BoV)**

&nbsp; O documento PDF é montado apenas sob demanda, incorporando o JSON original, o hash e o TST

&nbsp; Nenhum PDF é armazenado permanentemente



**Armazenamento mínimo**

&nbsp; O sistema mantém somente:

&nbsp;  JSON canônico

&nbsp;  TST emitido pela TSA

&nbsp;  O PDF não é guardado



