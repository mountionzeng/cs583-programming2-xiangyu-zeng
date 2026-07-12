import json
import os
from pathlib import Path


result_path = Path(os.environ.get("OPTIMIZATION_RESULT", "optimization_result.json"))
required = {
    "validation_accuracy": (int, float),
    "training_accuracy": (int, float),
    "executed_cells": int,
    "error_count": int,
    "epochs_completed": int,
}

with result_path.open(encoding="utf-8") as handle:
    result = json.load(handle)

missing = [key for key in required if key not in result]
if missing:
    raise ValueError(f"Missing required metrics: {missing}")

for key, expected_type in required.items():
    if not isinstance(result[key], expected_type):
        raise TypeError(f"{key} has invalid type: {type(result[key]).__name__}")

print(json.dumps(result, sort_keys=True))
