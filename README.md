# wordfreq‑tiny

A tiny, zero‑dependency Python tool that reads a text file and prints the most common words.

## Features
- One‑file implementation (`wordfreq.py`).
- CLI usage: `python -m wordfreq <PATH>`.
- Unit test with `pytest`.
- GitHub Actions CI that runs lint, test, and a security scan.
- MIT license, `.gitignore`, and a solid repo template following 2024 best‑practice checklists.

## Installation
```bash
git clone https://github.com/your‑user/wordfreq‑tiny.git
cd wordfreq‑tiny
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python -m wordfreq sample.txt
```

## Test
```bash
pytest
```

---
*Repository created with security‑hardening scripts, pinned actions, and least‑privilege permissions.*