[![release](https://img.shields.io/github/release/raffclar/python-project-template.svg)](https://github.com/raffclar/python-project-template/releases/latest)
[![tests](https://github.com/raffclar/python-project-template/actions/workflows/check-format-and-lint.yaml/badge.svg)](https://github.com/raffclar/python-project-template/actions/workflows/check-format-and-lint.yaml)
[![codecov](https://codecov.io/gh/raffclar/python-project-template/branch/main/graph/badge.svg?token=8GXLOL8A2V)](https://codecov.io/gh/raffclar/python-project-template)
# python-project-template

My project template for python.

## Requirements
1. Python >=3.9
2. Poetry

## Install the dependencies
```
poetry install --with dev --no-root
```

## Run the tests
```
poetry run python -m unittest
```

## Code coverage for tests
```
poetry run coverage run -m unittest
```