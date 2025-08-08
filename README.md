# Range Expander Utility

This Python utility expands strings representing sequences of numbers and ranges into a full list of integers. It supports advanced features such as custom range delimiters, step values, repetitions, deduplication, and output format customization.

---

## Features by Stage

| Stage | Feature Description                                                                 | Status |
|-------|--------------------------------------------------------------------------------------|--------|
| 1     | Basic range expansion (`"1-3"` → `[1, 2, 3]`)                                        | Done |
| 2     | Ignores whitespace and empty parts                                                  | Done |
| 3     | Supports custom range delimiters like `..`, `to`, `~`                               | Done |
| 4     | Handles reversed ranges, single-point ranges, and invalid syntax                   | Done |
| 5     | Supports step values (`1-10:2`, `10-1:3`)                                           | Done |
| 6     | Merges overlapping ranges and deduplicates numbers                                 | Done |
| 7     | Output format control: Python `list`, `set`, or `CSV` string                       | Done |

---

## Example

```python
Input:  "1-3, 5, 7..5, 10 to 14:2, 8*2"
Output: [1, 2, 3, 5, 7, 6, 5, 10, 12, 14, 8, 8]
```

---

## Running the Tests

```bash
pip install -r requirements.txt
pytest -v
```

---

## Live Demo

[![Try the Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shaileshsachan-rangeexpander-streamlit-app-yxrdty.streamlit.app/)

Click the badge above to test the utility in your browser via Streamlit.

---

## Note

- Each stage is implemented and committed **separately** with its own test cases.
- Final submission includes test coverage for all features and a fully working deployment.

---

## Deadline Reminder

📢 Please make sure to submit your GitHub repository link within **24 hours** of receiving the assignment.
