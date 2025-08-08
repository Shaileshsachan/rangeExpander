# Range Expander Utility

This Python utility expands strings representing sequences of numbers, ranges, steps, repetitions, and supports multiple output formats.

---

## Features by Stage

| Stage | Feature Description                                                                 | Status |
|-------|--------------------------------------------------------------------------------------|--------|
| 1     | Basic range expansion (`"1-3" → [1, 2, 3]`)                                          | Done     |
| 2     | Ignores whitespace and empty parts                                                  | Done     |
| 3     | Supports custom range delimiters like `..`, `to`, `~`                               | Done     |
| 4     | Gracefully handles reversed ranges, single-point ranges, and invalid syntax        | Done     |
| 5     | Supports step values (`1-10:2`, `10-1:3`)                                           | Done     |
| 6     | Merges overlapping ranges and deduplicates numbers                                 | Done     |
| 7     | Output format control: list, CSV string, or Python set                             | Done     |

---

## Running the Tests

```bash
pip install -r requirements.txt
pytest -v
