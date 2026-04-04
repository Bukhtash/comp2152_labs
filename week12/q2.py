class Finding:
    def __init__(self, subdomain, title, severity):
        self.subdomain = subdomain
        self.title = title
        self.severity = severity
        self.severity_rank = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}

    def __str__(self):
        return f"[{self.severity}] {self.subdomain} — {self.title}"

    def __eq__(self, other):
        return self.subdomain == other.subdomain and self.title == other.title

    def __lt__(self, other):
        return self.severity_rank[self.severity] < self.severity_rank[other.severity]


class Report:
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    def add(self, finding):
        self.findings.append(finding)

    def __len__(self):
        return len(self.findings)

    def __add__(self, other):
        new_report = Report(f"Merged: {self.team_name} + {other.team_name}")
        new_report.findings = self.findings + other.findings
        return new_report
