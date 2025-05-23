import subprocess

def check_firewall():
    try:
        command = [
            "powershell",
            "-Command",
            "Get-NetFirewallProfile | Select-Object Name, Enabled"
        ]
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        output = result.decode("utf-8")

        if "True" in output:
            return {"check": "Firewall", "status": "OK", "details": "Firewall está ativo em pelo menos um perfil ✅"}
        elif "False" in output:
            return {"check": "Firewall", "status": "ALERTA", "details": "Firewall desativado em todos os perfis ❌"}
        else:
            return {"check": "Firewall", "status": "DESCONHECIDO", "details": "Não foi possível interpretar a saída"}
    except Exception as e:
        return {"check": "Firewall", "status": "ERRO", "details": f"Erro ao executar comando: {e}"}
