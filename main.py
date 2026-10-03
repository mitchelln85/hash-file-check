"""Hash File Check — Compute SHA-256 for files and compare them against a checksum list."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='hash_file_check',
        description='Compute SHA-256 for files and compare them against a checksum list.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Hash File Check')
    print('Verify a download folder against SHA-256 sums.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
