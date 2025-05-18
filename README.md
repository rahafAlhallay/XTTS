# XTTS v2 TTS Project

This is a custom setup for running **XTTS v2** from [Coqui TTS](https://github.com/coqui-ai/TTS ) with support for multilingual speech synthesis, including Arabic.

> ⚠️ This repo does **not include large files** like models (`xtts_v2/`), or virtual environments.

---

## 🧾 Requirements

- **Python 3.10** (recommended)

> ⚠️ Newer versions of Python (e.g., 3.11+) may cause issues with unpickling due to PyTorch's `weights_only=True` default behavior.

---

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/rahafAlhallay/XTTS.git 
cd XTTS

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run your script
python xtts_clone.py