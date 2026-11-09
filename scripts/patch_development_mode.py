#!/usr/bin/env python3
"""Idempotently disable neo's Developer options check in decoded smali."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


METHOD_NAME = "developmentModeCheck"
ORIGINAL_BODY = """.method public static developmentModeCheck(Landroid/content/Context;)Z
    .locals 2

    .line 14
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;
    move-result-object p0
    const-string v0, "development_settings_enabled"
    const/4 v1, 0x0
    invoke-static {p0, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I
    move-result p0
    if-eqz p0, :cond_0
    const/4 p0, 0x1
    return p0
    :cond_0
    return v1
.end method"""

PATCHED_BODY = """.method public static developmentModeCheck(Landroid/content/Context;)Z
    .locals 0

    const/4 p0, 0x0
    return p0
.end method"""


def canonical(method: str) -> str:
    return "\n".join(line.rstrip() for line in method.strip().splitlines())


def patch_file(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    method_pattern = re.compile(
        r"(?m)^\.method\s+[^\n]*\bdevelopmentModeCheck\(Landroid/content/Context;\)Z\s*$"
        r".*?^\.end method\s*$",
        re.DOTALL,
    )
    matches = list(method_pattern.finditer(source))
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one {METHOD_NAME} method, found {len(matches)}")

    match = matches[0]
    current = canonical(match.group(0))
    if current == canonical(PATCHED_BODY):
        return False
    if current != canonical(ORIGINAL_BODY):
        raise ValueError(
            f"{METHOD_NAME} body differs from the known original; refusing to modify it"
        )

    updated = source[: match.start()] + PATCHED_BODY + source[match.end() :]
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    default_path = Path(
        "neo-recovery/apktool/smali_classes4/com/xamdesign/safe_device/"
        "DevelopmentMode/DevelopmentModeCheck.smali"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("smali_file", nargs="?", type=Path, default=default_path)
    args = parser.parse_args()

    changed = patch_file(args.smali_file)
    print("Patched developmentModeCheck." if changed else "Already patched; no changes made.")


if __name__ == "__main__":
    main()
