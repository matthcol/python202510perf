# Application geo

## Installation

Environnement Python 3.13:
- natif sur la cible
- environnement virtuel
- docker

Si environnement virtuel:
- venv (intégré à Python: même version)
- virtualenv (choix version python)
- conda
- poetry

### Environnement conda
Si conda installé (anaconda, miniconda, minforge, ...).
```
conda create -n envgeo_py313 python=3.13  
conda env list
conda activate envgeo_py313
conda install --file requirements.txt
```

### Environnement Python
```

pip install -r requirements.txt
```

