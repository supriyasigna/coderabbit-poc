# CodeRabbit POC — Inventory Sample

A tiny Python project with **intentionally planted bugs** so you can watch
CodeRabbit catch them in a pull request review.

## Planted issues (don't fix these before your first PR!)

| # | File | Issue |
|---|------|-------|
| 1 | `inventory.py` | SQL injection via string formatting in `get_item_by_name` |
| 2 | `inventory.py` | Mutable default argument (`seen=[]`) in `add_discount` |
| 3 | `inventory.py` | Divide-by-zero not handled in `average_price` |
| 4 | `inventory.py` | O(n²) nested loop in `find_duplicates` |
| 5 | `inventory.py` | Bare `except:` swallowing errors in `load_config` |
| 6 | `inventory.py` | Off-by-one loop bug in `apply_bulk_update` (skips last item) |
| 7 | `inventory.py` | Hardcoded secret in `get_env_key` |
| 8 | `test_inventory.py` | Missing test coverage for edge cases and 3 functions |

## How to use this for the CodeRabbit POC

See the accompanying step-by-step guide. Short version:
1. Push this repo to GitHub.
2. Install the CodeRabbit GitHub App on it.
3. Create a branch, make a small change (or just open a PR as-is), push.
4. Watch CodeRabbit comment on the PR within a minute or two.
5. Reply to a comment to test the chat feature; try a one-click fix.
