Installer Poetry
```
conda install pipx
pipx --version
pipx ensurepath
pipx install poetry
```

Nouveau projet
- poetry new geoapp (vide)
- poetry init (déjà du code)

Dans le répertoire du projet
poetry install
poetry add numpy matplotlib pandas
poetry add --group dev pytest pytest-cov pyright


Possibilité d'ajouter les configurations des outils annexes:
- pytest
- mypy ou pyright
- ruff (ou black + ...)

poetry run pytest
poetry run pytest --cov

poetry run ruff check .      # Linting/style
poetry run ruff format .     # Formatting
poetry run pyright          # Type checking

 poetry run ruff check . --fix # Fix things