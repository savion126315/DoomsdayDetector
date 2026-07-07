"""
This test metrics module has helpers for recording test results 
and also code to push results into a results csv file that persists

Savion Ragster
"""

import csv
from pathlib import Path
from datetime import datetime


_metrics: dict[str, dict[str, object]] = {}

def record(test_name: str, key: str, result: object) -> None:
    _metrics.setdefault(test_name, {})[key] = result

def get_all() -> dict[str, dict[str, object]]:
    return _metrics


def reset() -> None:
    _metrics.clear()

# CSV writing:
def write_csv() -> None:
    csv_dir = Path("records")
    csv_dir.mkdir(exist_ok=True)
    csv_file = csv_dir / "test_results.csv"

    rows = []

    for test_name, metrics in _metrics.items():
        row = {
            "timestamp": datetime.now().isoformat(),
            "test_name": test_name,
            **metrics,
        }
        rows.append(row)
        
    if not rows:
        return
    
    fieldnames = sorted({
        key
        for row in rows
        for key in row.keys()
    })
    write_header = not csv_file.exists()

    with open(csv_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerows(rows)
