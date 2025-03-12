class HTMLReporter:
    @staticmethod
    def generate(results):
        html = "<html><body><h1>Test Report</h1><table border='1'><tr><th>Test</th><th>Status</th><th>Details</th></tr>"
        for result in results:
            html += f"<tr><td>{result['test']}</td><td>{result['status']}</td><td>{result.get('error', '')}</td></tr>"
        html += "</table></body></html>"
        with open("reports_output/report.html", "w") as f:
            f.write(html)
