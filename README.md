# shipping-ci-practice

ICS 499 Week 10 practice repo: unit tests, branch coverage and a CI coverage gate.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest --cov=app --cov-branch --cov-report=term-missing --cov-fail-under=70
```
