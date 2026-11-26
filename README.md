<p align="center">
  <a href="https://ag.tavardt.com/pt/">
    <img src="https://ag.tavardt.com/img/tavardt-banner.png" alt="TAVARDT" width="1024" />
  </a>
</p>

# Watchdog de Certificados TLS/SSL

[![Âmbito de Verificação Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Monitorização técnica de expiração de certificados SSL/TLS, integridade criptográfica e conformidade de transporte seguro em Portugal.

Desenvolvido e mantido pela prática de ciberdefesa da **TAVARDT** para o ecossistema tecnológico português.

***

## 1. Âmbito de Verificação Perimetral

Este utilitário de terminal inspeciona o ciclo de vida de certificados, suítes criptográficas e cadeias de confiança:

* **Alerta Preventivo de Expiração:** Calcula os dias restantes para o vencimento com limites automatizados (> 30 dias válido, <= 30 dias alerta, <= 0 dias expirado).
* **Auditoria de Versão do Protocolo:** Verifica a imposição de TLS 1.3 e TLS 1.2 conforme as orientações de transporte seguro da CNPD e RGPD.
* **Avaliação de Suíte de Cifra:** Inspeciona algoritmos de cifra negociados e comprimento de chave simétrica (128/256 bits).
* **Validação de Autoridade Certificadora (CA):** Inspeciona a organização emissora na cadeia de confiança e os nomes alternativos do sujeito (SAN).
* **Zero Dependências Externas:** Funciona integralmente com os módulos nativos `ssl` e `socket` da biblioteca padrão do Python.

***

## 2. Matriz de Linha de Base Criptográfica e Ciclo de Vida

<table>
  <thead>
    <tr>
      <th>Parâmetro Inspecionado</th>
      <th>Método de Avaliação no Handshake</th>
      <th>Linha de Base Recomendada</th>
      <th>Risco Operacional Mitigado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Validade do Certificado</strong></td>
      <td>Compara o registo <code>notAfter</code> com a hora UTC atual</td>
      <td>Alerta preventivo com &gt; 30 dias de antecedência</td>
      <td>Queda de disponibilidade e alertas de ligação insegura</td>
    </tr>
    <tr>
      <td><strong>Versão do Protocolo</strong></td>
      <td>Analisa a versão negociada via <code>ssock.version()</code></td>
      <td><code>TLSv1.3</code> preferencial, <code>TLSv1.2</code> mínimo</td>
      <td>Ataques de downgrade e exploração de protocolos legados</td>
    </tr>
    <tr>
      <td><strong>Suíte de Cifra e Chaves</strong></td>
      <td>Obtém parâmetros de cifra via <code>ssock.cipher()</code></td>
      <td>Cifras modernas AEAD com chaves de &gt;= 128 bits</td>
      <td>Interceção man-in-the-middle e quebra de cifras fracas</td>
    </tr>
    <tr>
      <td><strong>Autoridade Certificadora (CA)</strong></td>
      <td>Extrai a organização emissora da cadeia de confiança</td>
      <td>CA raiz pública reconhecida pela cadeia do sistema</td>
      <td>Certificados autoassinados e interceção de tráfego</td>
    </tr>
    <tr>
      <td><strong>Subject Common Name (CN)</strong></td>
      <td>Valida o nome do host contra o assunto do certificado</td>
      <td>Correspondência estrita ao FQDN ou SAN wildcard</td>
      <td>Erros de incompatibilidade de domínio e falsificação de identidade</td>
    </tr>
  </tbody>
</table>

***

## 3. Guia de Execução Rápida e Automação

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python watchdog.py exemplo.pt
```

O motor de auditoria analisa o handshake de socket de forma determinística:

* **Biblioteca Padrão Nativa:** Opera exclusivamente via bibliotecas padrão do Python (`ssl`, `socket`, `datetime`), sem pacotes externos.
* **Diagnóstico em Três Níveis:** Classifica o estado do certificado como PASS (> 30 dias), WARN (próximo ao vencimento) ou FAIL (expirado).
* **Compatibilidade com CI/CD:** Adequado para etapas de validação em fluxos de deploy automatizado e esteiras de segurança.

***

## 4. Perguntas Frequentes (FAQ Técnico)

### 1. Por que o limite preventivo de 30 dias para alerta de expiração é crítico para a operação?
A notificação com 30 dias de antecedência concede tempo operacional para renovação automatizada via ACME ou substituição manual de chaves. Ultrapassar essa data faz com que navegadores bloqueiem o acesso de utilizadores com alertas severos de segurança.

### 2. Como o watchdog.py inspeciona o handshake TLS sem realizar o download de páginas HTTP?
O utilitário estabelece uma ligação direta via socket TCP na porta 443 encapsulada com TLS nativo (`ssl.wrap_socket`). Os dados de cifra, versão e emissor são extraídos durante o handshake, garantindo velocidade máxima com consumo mínimo de largura de banda.

### 3. Quais são os riscos decorrentes do uso de versões legadas como TLS 1.0 e TLS 1.1?
Versões depreciadas utilizam algoritmos criptográficos vulneráveis a ataques de downgrade e interceção man-in-the-middle. A imposição de TLS 1.2 ou TLS 1.3 assegura confidencialidade persistente (forward secrecy) e cifras autenticadas modernas.

### 4. De que forma o script processa tanto nomes de domínio diretos quanto URLs completas?
O script analisa o argumento fornecido via módulo `urllib.parse`. Caso o utilizador forneça uma URL iniciando com `http://` ou `https://`, ele extrai puramente o hostname correspondente para abrir a ligação socket na porta 443.

### 5. É possível executar este watchdog em pipelines de CI/CD e rotinas agendadas (cron)?
Sim, o script opera nativamente em ambientes Linux, macOS e Windows sem necessidade de bibliotecas de terceiros. Seu comportamento determinístico viabiliza execuções em GitHub Actions, rotinas cron e painéis de monitorização de disponibilidade.

***

## 5. Ferramentas Técnicas Online (Portugal)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Validador de Consent Mode v2 e RGPD](https://tools.tavardt.com/pt/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC e Segurança de E-mail](https://tools.tavardt.com/pt/verificador-dmarc-email/)
* [Deteção de Ficheiros Sensíveis Expostos](https://tools.tavardt.com/pt/verificador-ficheiros-expostos/)
* [Portal de Diagnóstico Técnico Portugal](https://tools.tavardt.com/pt/)

***

## 6. Consultoria e Blindagem Criptográfica em Portugal

Para auditoria criptográfica especializada, conformidade com o RGPD e testes de cibersegurança em Portugal, entre em contacto com a equipa da **TAVARDT**.

***

## Links Úteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suíte de Diagnósticos:** https://tools.tavardt.com/pt/
* **Contacto Técnico:** https://ag.tavardt.com/pt/contacto/

***

### Licença
Distribuído sob a Licença MIT.

***

© 2026 TAVARDT. Todos os direitos reservados.
