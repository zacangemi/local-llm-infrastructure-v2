#!/usr/bin/env python3
"""Validate public repository structure, cost arithmetic, links, and privacy patterns."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOM = ROOT / "data" / "bill-of-materials.csv"
IMAGES = [
    ROOT / "assets" / "images" / "v2-open-case.jpg",
    ROOT / "assets" / "images" / "bench-assembly.jpg",
    ROOT / "assets" / "images" / "gpu-slot-gap.jpg",
    ROOT / "assets" / "images" / "airflow-layout.jpg",
]

REQUIRED = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "docs" / "architecture.md",
    ROOT / "docs" / "build-notes.md",
    ROOT / "docs" / "bill-of-materials.md",
    ROOT / "docs" / "airflow.md",
    ROOT / "docs" / "remote-operations.md",
    ROOT / "docs" / "limitations-and-upgrades.md",
    ROOT / "docs" / "sources.md",
    BOM,
    *IMAGES,
]

EXPECTED = {
    "v2": Decimal("8439.27"),
    "v1": Decimal("2330.28"),
    "all": Decimal("10769.55"),
}

TEXT_SUFFIXES = {".md", ".csv", ".py", ".yml", ".yaml", ".txt"}

FORBIDDEN = {
    "Linux home path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "macOS home path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "Windows home path": re.compile(
        r"(?i)(?<![A-Za-z0-9])[A-Z]:\\Users\\[A-Za-z0-9._-]+\\"
    ),
    "private IPv4 address": re.compile(
        r"(?<![\d.])(?:10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)"
        r"\d{1,3}\.\d{1,3}(?![\d.])"
    ),
    "Tailscale-style IPv4 address": re.compile(
        r"(?<![\d.])100\.(?:\d{1,3}\.){2}\d{1,3}(?![\d.])"
    ),
    "MAC address": re.compile(
        r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}:){5}[0-9a-f]{2}(?![0-9a-f])"
    ),
    "email address": re.compile(
        r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
    ),
    "North American phone number": re.compile(
        r"(?<!\d)(?:\+?1[-. ()]*)?(?:\d{3}[-. ()]*){2}\d{4}(?!\d)"
    ),
    "US Social Security number": re.compile(
        r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)"
    ),
    "private key": re.compile(
        r"(?i)-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"
    ),
    "credential assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|client[_-]?secret|password|passwd|auth[_-]?token|"
        r"access[_-]?token)\s*[:=]"
    ),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style secret key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "receipt, order, or tracking identifier": re.compile(
        r"(?i)\b(?:order|receipt|invoice|tracking)\s*"
        r"(?:(?:number|no\.?|id)\s*[:#=]|#)\s*[A-Z0-9][A-Z0-9-]{3,}"
    ),
    "serial or service-tag identifier": re.compile(
        r"(?i)\b(?:serial|service\s+tag|imei)\s*(?:number|no\.?|#|id)\s*[:#=]"
    ),
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SAFE_COMMIT_EMAIL_SUFFIXES = (
    "@users.noreply.github.com",
    "@github.com",
)


def money(value: str) -> Decimal:
    return Decimal(value).quantize(Decimal("0.01"))


def validate_required() -> list[str]:
    return [
        f"missing required file: {path.relative_to(ROOT)}"
        for path in REQUIRED
        if not path.is_file()
    ]


def validate_bom() -> list[str]:
    errors: list[str] = []
    totals = {"v2": Decimal("0"), "v1": Decimal("0"), "all": Decimal("0")}

    with BOM.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != 13:
        errors.append(f"expected 13 BOM rows, found {len(rows)}")

    for line_number, row in enumerate(rows, start=2):
        item = money(row["item_price"])
        plan = money(row["protection_plan"])
        shipping = money(row["shipping"])
        pre_tax = money(row["pre_tax_total"])
        tax = money(row["sales_tax"])
        post_tax = money(row["post_tax_total"])

        if item + plan + shipping != pre_tax:
            errors.append(f"BOM line {line_number}: pre-tax arithmetic does not reconcile")
        if pre_tax + tax != post_tax:
            errors.append(f"BOM line {line_number}: post-tax arithmetic does not reconcile")

        bucket = "v1" if row["origin"] == "V1 carryover" else "v2"
        totals[bucket] += post_tax
        totals["all"] += post_tax

    for key, expected in EXPECTED.items():
        actual = totals[key].quantize(Decimal("0.01"))
        if actual != expected:
            errors.append(f"{key} BOM total: expected {expected}, found {actual}")

    return errors


def public_text_files() -> list[Path]:
    ignored_names = {
        "BLOG-DRAFT-v2-2026-08-13.md",
        "BLOG-PROJECT-1-BUILD-DRAFT-v3-2026-08-14.md",
        "BLOG-PROJECT-2-COMMISSIONING-DRAFT-v1-2026-08-14.md",
        "cpu-upgrade-path.md",
    }
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.name not in ignored_names
        and path.suffix.lower() in TEXT_SUFFIXES
    ]


def validate_privacy() -> list[str]:
    errors: list[str] = []
    for path in public_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in FORBIDDEN.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: possible {label}")
    return errors


def validate_git_metadata() -> list[str]:
    """Reject personally identifying author or committer email addresses."""
    errors: list[str] = []
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--format=%H%x09%ae%x09%ce"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        return [f"unable to inspect Git commit metadata: {exc}"]

    for line in result.stdout.splitlines():
        commit, author_email, committer_email = line.split("\t", 2)
        for role, email in (
            ("author", author_email),
            ("committer", committer_email),
        ):
            normalized = email.strip().lower()
            if normalized and not normalized.endswith(SAFE_COMMIT_EMAIL_SUFFIXES):
                errors.append(
                    f"{commit}: {role} email is not a privacy-preserving "
                    "GitHub noreply address"
                )
    return errors


def validate_image_metadata() -> list[str]:
    """Reject common embedded EXIF/XMP metadata containers in public photos."""
    errors: list[str] = []
    markers = (
        b"Exif\x00\x00",
        b"http://ns.adobe.com/xap/1.0/",
        b"GPSLatitude",
        b"GPSLongitude",
    )
    for path in IMAGES:
        if not path.is_file():
            continue
        data = path.read_bytes()
        if any(marker in data for marker in markers):
            errors.append(
                f"{path.relative_to(ROOT)}: embedded EXIF/XMP metadata detected"
            )
    return errors


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for path in public_text_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in MARKDOWN_LINK.findall(text):
            clean = target.split("#", 1)[0].strip()
            if not clean or "://" in clean or clean.startswith("mailto:"):
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors


def main() -> int:
    errors = validate_required()
    if not errors:
        errors.extend(validate_bom())
    errors.extend(validate_privacy())
    errors.extend(validate_git_metadata())
    errors.extend(validate_image_metadata())
    errors.extend(validate_local_links())

    if errors:
        print("Repository validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation PASSED")
    print("- required public files present")
    print("- 13 BOM rows reconcile to $10,769.55")
    print("- public text passed privacy-pattern checks")
    print("- Git commit metadata uses privacy-preserving noreply addresses")
    print("- public images contain no EXIF/XMP metadata containers")
    print("- local Markdown links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
