from utils import check_firewall

def generate_report(results):
    with open("reports/sample_report.md", "w", encoding="utf-8") as f:
        f.write("# Relatório CyberGuardian\n\n")
        for r in results:
            f.write(f"### {r['check']}\n")
            f.write(f"- Status: **{r['status']}**\n")
            f.write(f"- Detalhes: {r['details']}\n\n")

if __name__ == "__main__":
    print("[*] Iniciando análise de segurança...\n")
    results = []
    results.append(check_firewall.check_firewall())
    generate_report(results)
    print("[✔] Relatório gerado em: reports/sample_report.md")
