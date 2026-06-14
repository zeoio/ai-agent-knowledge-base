#!/usr/bin/env python3
"""Validate registry JSON files without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "registries"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
ALLOWED_STATUSES = {
    "watching",
    "evaluating",
    "active",
    "paused",
    "rejected",
    "archived",
}
ALLOWED_TRUST_LEVELS = {
    "unknown",
    "low",
    "medium",
    "high",
    "critical",
}
REQUIRED_ENTRY_FIELDS = {
    "id",
    "name",
    "status",
    "trust_level",
    "summary",
    "tags",
    "links",
    "created_at",
    "updated_at",
}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, path, f"invalid JSON at line {exc.lineno}: {exc.msg}")
        return None

    if not isinstance(data, dict):
        fail(errors, path, "top-level value must be an object")
        return None

    return data


def validate_entry(path: Path, index: int, entry: Any, seen_ids: dict[str, Path], errors: list[str]) -> None:
    if not isinstance(entry, dict):
        fail(errors, path, f"items[{index}] must be an object")
        return

    entry_id = entry.get("id")
    if not isinstance(entry_id, str) or not ID_RE.match(entry_id):
        fail(errors, path, f"items[{index}].id must match {ID_RE.pattern}")
    elif entry_id in seen_ids:
        fail(errors, path, f"duplicate id '{entry_id}' also found in {seen_ids[entry_id].relative_to(ROOT)}")
    else:
        seen_ids[entry_id] = path

    missing = sorted(REQUIRED_ENTRY_FIELDS - set(entry))
    if missing:
        fail(errors, path, f"{entry_id or f'items[{index}]'} missing required fields: {', '.join(missing)}")

    status = entry.get("status")
    if status is not None and status not in ALLOWED_STATUSES:
        fail(errors, path, f"{entry_id}.status '{status}' is not allowed")

    trust_level = entry.get("trust_level")
    if trust_level is not None and trust_level not in ALLOWED_TRUST_LEVELS:
        fail(errors, path, f"{entry_id}.trust_level '{trust_level}' is not allowed")

    for field in ("tags", "links"):
        if field in entry and not isinstance(entry[field], list):
            fail(errors, path, f"{entry_id}.{field} must be an array")

    for field in ("created_at", "updated_at"):
        value = entry.get(field)
        if value is not None and (not isinstance(value, str) or not DATE_RE.match(value)):
            fail(errors, path, f"{entry_id}.{field} must use YYYY-MM-DD")

    detail_path = entry.get("detail_path")
    if isinstance(detail_path, str) and detail_path:
        target = ROOT / detail_path
        if not target.exists():
            fail(errors, path, f"{entry_id}.detail_path does not exist: {detail_path}")


def validate_registry(path: Path, seen_ids: dict[str, Path], errors: list[str]) -> None:
    data = load_json(path, errors)
    if data is None:
        return

    for field in ("registry_version", "item_type", "items"):
        if field not in data:
            fail(errors, path, f"missing top-level field: {field}")

    items = data.get("items")
    if not isinstance(items, list):
        fail(errors, path, "items must be an array")
        return

    for index, entry in enumerate(items):
        validate_entry(path, index, entry, seen_ids, errors)


def main() -> int:
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    paths = sorted(REGISTRY_DIR.glob("*.json"))
    if not paths:
        print("No registry files found.")
        return 1

    for path in paths:
        validate_registry(path, seen_ids, errors)

    if errors:
        print("Registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Registry validation passed for {len(paths)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
