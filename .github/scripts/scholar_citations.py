#!/usr/bin/env python3
"""Fetch total Google Scholar citations and write them to _data/scholar.yml.

Run by .github/workflows/scholar-citations.yml. Google Scholar has no public API
and blocks CORS, so this server-side scrape is the practical way to keep the count
fresh. It is best-effort: if Scholar returns a consent/CAPTCHA page (no count found),
the script exits non-zero WITHOUT touching the data file, so a stale-but-valid value
is kept and the workflow surfaces the failure.
"""
import datetime
import pathlib
import re
import sys
import urllib.request

USER_ID = "K6V2VzsAAAAJ"
URL = f"https://scholar.google.com/citations?user={USER_ID}&hl=en"
DATA_FILE = pathlib.Path(__file__).resolve().parents[2] / "_data" / "scholar.yml"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def main() -> int:
    req = urllib.request.Request(URL, headers=HEADERS)
    try:
        html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    except Exception as exc:  # network / HTTP error
        print(f"ERROR: request failed: {exc}", file=sys.stderr)
        return 1

    # The stats table renders as <td class="gsc_rsb_std">2495</td> ...
    # Order is Citations(All), Citations(Since), h-index(All), ... so [0] = total citations.
    matches = re.findall(r'gsc_rsb_std">([\d,]+)<', html)
    if not matches:
        print("ERROR: citation count not found (consent/CAPTCHA page?).", file=sys.stderr)
        return 1

    citations = int(matches[0].replace(",", ""))
    if citations <= 0:
        print(f"ERROR: implausible citation count parsed: {citations}", file=sys.stderr)
        return 1

    DATA_FILE.write_text(
        "# Auto-updated daily by .github/workflows/scholar-citations.yml — do not edit by hand.\n"
        f"citations: {citations}\n"
        f'updated: "{datetime.date.today().isoformat()}"\n'
    )
    print(f"citations: {citations}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
