# altariya

## Prerequisites

- Python 3.11
- Required Python packages are listed in the `requirements.txt` file.

## Installation
2. Run project in virtual environment 🚀
2.1. Create virtual env:

```bash
        python -m virtualenv venv
```

2.2. Create virtual environment version depend:

```bash
        virtualenv venv --python=python3.11
```

2.3. activate

```bash
  .\venv\Scripts\activate.bat
```

2.4 Install requirements:

```bash
pip install -r requirements.txt
```

## Docker
for docker build: 
```bash
docker build -t app .
```

for docker run:
```bash
docker run -d -p 8000:8000 app
```