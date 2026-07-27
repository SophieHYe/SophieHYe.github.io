#!/usr/bin/env python3
"""Fetch GitHub stars and HuggingFace dataset downloads for each project and
write them to _data/projects.yml (read by the project cards in _pages/about.md).

Run by .github/workflows/project-stats.yml. Best-effort: on a failed fetch the
previous value in the YAML is kept, so a transient error never zeroes a badge.
"""
import datetime
import json
import pathlib
import sys
import urllib.request

import yaml

DATA = pathlib.Path(__file__).resolve().parents[2] / "_data" / "projects.yml"
HEADERS = {"User-Agent": "personal-site-stats-bot", "Accept": "application/json"}

PROJECTS = {
    "terminalworld": {"github": "EuniAI/TerminalWorld", "hf_dataset": "EuniAI/TerminalWorld"},
    "contextbench": {"github": "EuniAI/ContextBench", "hf_dataset": "Contextbench/ContextBench"},
    "prometheus": {"github": "EuniAI/Prometheus"},
}


def get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def github_stars(repo):
    return int(get_json(f"https://api.github.com/repos/{repo}")["stargazers_count"])


def hf_downloads(dataset):
    return int(get_json(f"https://huggingface.co/api/datasets/{dataset}").get("downloads", 0))


def main():
    data = yaml.safe_load(DATA.read_text()) if DATA.exists() else {}
    data = data or {}

    for key, cfg in PROJECTS.items():
        entry = data.get(key) or {}
        try:
            entry["github_stars"] = github_stars(cfg["github"])
        except Exception as exc:
            print(f"WARN {key} github: {exc}", file=sys.stderr)
        if cfg.get("hf_dataset"):
            try:
                entry["hf_downloads"] = hf_downloads(cfg["hf_dataset"])
            except Exception as exc:
                print(f"WARN {key} hf: {exc}", file=sys.stderr)
        data[key] = entry

    data["updated"] = datetime.date.today().isoformat()

    header = "# Auto-updated daily by .github/workflows/project-stats.yml — do not edit by hand.\n"
    DATA.write_text(header + yaml.safe_dump(data, sort_keys=True, default_flow_style=False))
    print(yaml.safe_dump(data, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
