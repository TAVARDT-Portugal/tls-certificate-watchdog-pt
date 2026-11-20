#!/usr/bin/env python3
import sys
import socket
import ssl
from datetime import datetime, timezone
from urllib.parse import urlparse

def inspect_tls(hostname, port=443):
    print(f"\n[TAVARDT Portugal] A inspecionar certificado TLS e cadeia criptografica para: {hostname}:{port}\n")
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()
                
                expire_str = cert['notAfter']
                expire_date = datetime.strptime(expire_str, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
                now = datetime.now(timezone.utc)
                days_left = (expire_date - now).days
                
                issuer_dict = dict(x[0] for x in cert.get('issuer', []))
                common_name = dict(x[0] for x in cert.get('subject', [])).get('commonName', hostname)
                
                print(f"  [INFO] Common Name: {common_name}")
                print(f"  [INFO] Issuer: {issuer_dict.get('organizationName', 'Unknown')}")
                print(f"  [INFO] TLS Version: {version}")
                print(f"  [INFO] Cipher: {cipher[0]} ({cipher[2]} bits)")
                print(f"  [INFO] Expiry: {expire_date.strftime('%Y-%m-%d %H:%M:%S UTC')}")
                print(f"  [INFO] Remaining: {days_left} dias restantes")
                
                if days_left > 30:
                    print(f"\n  [PASS] Certificado valido. ({days_left} dias restantes)")
                elif days_left > 0:
                    print(f"\n  [WARN] Certificado proximo do termo de validade. ({days_left} dias restantes)")
                else:
                    print(f"\n  [FAIL] Certificado expirado.")
                    
                print(f"\nVerificação completa online: https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/")
                print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/pt/ciberseguranca/\n")
                
    except Exception as e:
        print(f"[TAVARDT Portugal] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python watchdog.py <hostname>")
        sys.exit(1)
        
    target = sys.argv[1].strip()
    if target.startswith("http://") or target.startswith("https://"):
        target = urlparse(target).hostname or target
        
    inspect_tls(target)
