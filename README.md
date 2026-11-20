# Watchdog de Certificados TLS/SSL | TAVARDT Portugal

[![TLS Watchdog](https://img.shields.io/badge/Security-TLS%20Watchdog-5b3cf5.svg)](https://tools.tavardt.com/pt/)
[![Regulatory Compliance](https://img.shields.io/badge/Region-EUR-00C853.svg)](https://ag.tavardt.com/pt/)

Monitorização automatizada de expiração de certificados SSL/TLS e integridade de cifras perante o RGPD em Portugal.

Maintained by the infrastructure resilience and cybersecurity division at [TAVARDT Portugal](https://ag.tavardt.com/pt/).

---

## 1. Capabilities

* **Expiration Watchdog:** Computes real-time days until SSL/TLS certificate expiry with configurable warning thresholds.
* **Cipher Suite Inspection:** Detects deprecated TLS versions (TLS 1.0/1.1) and verifies forward secrecy support.
* **Certificate Authority Validation:** Audits issuing CA identity and chain validity.
* **Zero External Dependencies:** Built with native Python `ssl` and `socket` modules for seamless integration into CI/CD pipelines, cron jobs, and server health checks.

---

## 2. Quick Start

Execute directly via Python without installing third-party packages:

```bash
python watchdog.py example.com
```

---

## 3. Online Diagnostic Suite

For comprehensive vulnerability scanning, DNS verification, and technical audits, visit our localized tools portal:

* [Online HTTP Security Headers Checker](https://tools.tavardt.com/pt/security-headers-check/)
* [Exposed Secret & Credential Scanner](https://tools.tavardt.com/pt/exposed-files-scanner/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/pt/dmarc-checker/)
* [Full Diagnostic Portal](https://tools.tavardt.com/pt/)

For professional remediation and cybersecurity advisory, contact [TAVARDT Portugal](https://ag.tavardt.com/pt/contact/).
