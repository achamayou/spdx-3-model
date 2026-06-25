#!/usr/bin/env python3
"""List SPDX model concepts relevant to CoSPDX CBOR label allocation."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass, fields
from pathlib import Path


PROFILE_PREFIXES = {
    "AI": "ai",
    "Build": "build",
    "Dataset": "dataset",
    "ExpandedLicensing": "expandedlicensing",
    "Extension": "extension",
    "FunctionalSafety": "functionalsafety",
    "Hardware": "hardware",
    "Operations": "operations",
    "Security": "security",
    "Service": "service",
    "SimpleLicensing": "simplelicensing",
    "Software": "software",
    "SupplyChain": "supplychain",
}

DIRECTORY_CATEGORIES = {
    "Classes": "Object/class term",
    "Individuals": "Special singleton term",
    "Properties": "Model property",
    "Vocabularies": "Vocabulary/type class",
}


@dataclass(frozen=True)
class Concept:
    path: str
    profile: str
    directory: str
    category: str
    cddl_name: str
    metadata_name: str
    nature: str
    instantiability: str
    type_: str
    subclass_of: str
    iri: str
    entry_count: int
    entries: str


def metadata_block(markdown: str) -> str:
    match = re.search(r"^## Metadata\s*\n\n(.*?)(?:\n## |\Z)", markdown, re.S | re.M)
    return match.group(1) if match else ""


def parse_metadata(markdown: str) -> dict[str, str]:
    block = metadata_block(markdown)
    metadata: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^- ([^:]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            metadata[key.strip()] = value.strip()
    return metadata


def parse_entries(markdown: str) -> list[str]:
    match = re.search(r"^## Entries\s*\n\n(.*?)(?:\n## |\Z)", markdown, re.S | re.M)
    if not match:
        return []
    entries: list[str] = []
    for entry_match in re.finditer(r"^- `?([A-Za-z0-9_]+)`?:", match.group(1), re.M):
        entries.append(entry_match.group(1))
    return entries


def prefixed_name(profile: str, local_name: str) -> str:
    if profile == "Core":
        return local_name
    prefix = PROFILE_PREFIXES.get(profile)
    if not prefix:
        return f"{profile.lower()}_{local_name}"
    return f"{prefix}_{local_name}"


def cddl_name(profile: str, directory: str, local_name: str) -> str:
    if directory == "Properties":
        return f"label.{prefixed_name(profile, local_name)}"
    if directory == "Vocabularies":
        return f"const.{prefixed_name(profile, local_name)}"
    if directory == "Individuals":
        return f"const.{prefixed_name(profile, local_name)}"
    if directory == "Classes":
        return f"const.{prefixed_name(profile, local_name)}"
    raise ValueError(f"Unsupported model directory: {directory}")


def iter_concepts(model_dir: Path) -> list[Concept]:
    concepts: list[Concept] = []
    for path in sorted(model_dir.glob("*/*/*.md")):
        if len(path.parts) < 4:
            continue
        profile = path.parts[-3]
        directory = path.parts[-2]
        if directory not in DIRECTORY_CATEGORIES:
            continue

        markdown = path.read_text(encoding="utf-8")
        metadata = parse_metadata(markdown)
        local_name = metadata.get("name") or path.stem
        entries = parse_entries(markdown)

        concepts.append(
            Concept(
                path=str(path),
                profile=profile,
                directory=directory,
                category=DIRECTORY_CATEGORIES[directory],
                cddl_name=cddl_name(profile, directory, local_name),
                metadata_name=local_name,
                nature=metadata.get("Nature", ""),
                instantiability=metadata.get("Instantiability", ""),
                type_=metadata.get("type", ""),
                subclass_of=metadata.get("SubclassOf", ""),
                iri=metadata.get("IRI", ""),
                entry_count=len(entries),
                entries=", ".join(entries),
            )
        )
    return concepts


def write_tsv(concepts: list[Concept]) -> None:
    fieldnames = [field.name for field in fields(Concept)]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, dialect="excel-tab")
    writer.writeheader()
    for concept in concepts:
        writer.writerow(asdict(concept))


def markdown_cell(value: object) -> str:
    text = str(value)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def write_markdown(concepts: list[Concept]) -> None:
    fieldnames = [field.name for field in fields(Concept)]
    print("| " + " | ".join(fieldnames) + " |")
    print("|" + "|".join("---" for _ in fieldnames) + "|")
    for concept in concepts:
        row = asdict(concept)
        print("| " + " | ".join(markdown_cell(row[field]) for field in fieldnames) + " |")


def write_json(concepts: list[Concept]) -> None:
    json.dump([asdict(concept) for concept in concepts], sys.stdout, indent=2)
    sys.stdout.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Traverse model/*/{Classes,Individuals,Properties,Vocabularies}/*.md "
            "and print concepts relevant to CoSPDX CBOR label allocation."
        )
    )
    parser.add_argument(
        "--model-dir",
        default="model",
        type=Path,
        help="Path to the SPDX model directory. Defaults to ./model.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "tsv", "json"),
        default="markdown",
        help="Output format. Defaults to Markdown.",
    )
    args = parser.parse_args()

    concepts = iter_concepts(args.model_dir)

    if args.format == "json":
        write_json(concepts)
    elif args.format == "tsv":
        write_tsv(concepts)
    else:
        write_markdown(concepts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
