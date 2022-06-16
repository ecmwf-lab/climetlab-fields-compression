# Development notes


Only required if you wish to install all the required prerequisites in [Miniconda](https://docs.conda.io/en/latest/miniconda.html)/[Anaconda](https://www.anaconda.com/) for local development and testing.

```sh
conda env create -f environment.yml
```

Then activate with `conda activate climetlab-fields-compression`.

## Installing

```
pip install -e .
```

## Testing

```
cd tests
python -m pytest -v -s
```

## Versioning

This project uses [semantic versioning](https://semver.org/).
