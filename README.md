# Wire Validator

Automotive wire harness validator for CSV/Excel data with duplicate, missing-value and cross-section checks.

## Overview

**Wire Validator** is a Python application for validating automotive wire harness data exported from tools such as E3.series, Excel, or CSV-based workflows.

The project focuses on **data quality checks commonly used in automotive wiring harness development**, including:

- Duplicate wire numbers
- Missing wire numbers
- Missing cross sections
- Small wire cross sections

The application is built with a clean modular architecture and includes automated tests using **pytest**.

---

## Features

- Read wire lists from CSV files
- Detect duplicate wire numbers
- Detect missing wire numbers
- Detect missing cross sections
- Detect small wire cross sections
- Generate console validation reports
- Automated unit tests

---

## Project Structure

```text
wire-validator/
├── data/
│   └── sample_wires.csv
├── tests/
│   ├── test_wire.py
│   └── test_validator.py
├── wire.py
├── validator.py
├── csv_reader.py
├── report.py
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.13+
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/OSI-de/wire-validator.git
cd wire-validator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -v
```

Run the application:

```bash
python main.py
```

---

## Example CSV

```csv
wire,section
W1001,0.35
W1002,0.75
W1002,0.75
,1.50
W1005,
```

---

## Example Output

```text
===== Validation Report =====
⚠ W1002 is duplicated.
⚠ Wire number is missing.
⚠ W1005 has no cross section.
⚠ W1001 has a small cross section.

=======================
Errors: 4
```

---

## Testing

This project uses **pytest** for automated testing.

Run all tests:

```bash
pytest -v
```

---

## Roadmap

- [x] CSV import
- [x] Validation logic
- [x] Console report
- [x] Unit tests
- [ ] Excel import (openpyxl)
- [ ] GUI (PySide6)
- [ ] PDF reports
- [ ] Logging
- [ ] GitHub Actions (CI)

---

## Technologies

- Python 3
- Object-Oriented Programming (OOP)
- CSV
- pytest
- Git & GitHub

---

## Motivation

This project is intended as both a **learning project** and a **practical automotive engineering utility**.

It combines Python development with real-world wire harness validation tasks typically encountered in automotive supplier and EDS workflows.

---

## Author

**OSI-de**

GitHub: https://github.com/OSI-de