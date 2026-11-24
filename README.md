# Watchdog de Certificados TLS/SSL | TAVARDT Portugal

[![Âmbito de Verificação Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/)
Monitorização técnica de expiração de certificados SSL/TLS, integridade criptográfica e conformidade de transporte seguro em Portugal.

Desenvolvido e mantido pela área de ciberdefesa e proteção de infraestruturas da **TAVARDT Portugal**.

***

## 1. Âmbito de Verificação Perimetral

Este utilitário de terminal inspeciona em tempo real a validade, cifras e autoridades certificadoras de ligações seguras:

* **Alerta Preventivo de Expiração:** Calcula os dias restantes para o término da validade do certificado com limites configuráveis.
* **Auditoria de Cifras e Protocolos:** Confirma a utilização de TLS 1.3 e a descontinuação de protocolos legados.
* **Validação de Autoridade Emissora (CA):** Inspeciona a cadeia de certificação e os nomes alternativos do sujeito (SANs).
* **Zero Dependências Externas:** Execução direta através das bibliotecas nativas ssl e socket do Python.

***

## 2. Guia de Execução Rápida

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python watchdog.py exemplo.pt
```

***

## 3. Ferramentas Técnicas Online (Portugal)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* Auditoria de Cabeçalhos de Segurança
* [Validador de Consent Mode v2 e RGPD](https://tools.tavardt.com/pt/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC e Segurança de E-mail](https://tools.tavardt.com/pt/verificador-dmarc-email/)
* [Deteção de Ficheiros Sensíveis Expostos](https://tools.tavardt.com/pt/verificador-ficheiros-expostos/)
* [Portal de Diagnóstico Técnico Portugal](https://tools.tavardt.com/pt/)

***

## 4. Consultoria e Remediação Técnica

Para hardening criptográfico de servidores, automação de renovação e proteção corporativa em Portugal, contacte a **TAVARDT Portugal**.
