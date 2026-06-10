# Setup Guide

## Requirements

- Python 3.10 or higher

## Setup

All commands below should be run from the **project root directory** (the folder containing `app.py` and `pyproject.toml`).

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

```bash
# Mac / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -e .
```

To also install development tools use:

```bash
pip install -e ".[dev]"
```

4. Create a `logs` folder inside the `data` directory at the project root and place your JSON log files inside it:

```
matchbook-log-analyser/   <- project root
|--data/
    |--logs/
        |--logfile1.json
        |--logfile2.json
```

5. Run the dashboard:

```bash
streamlit run app.py
```

A browser tab will open automatically with the dashboard.
