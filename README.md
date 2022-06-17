# Climetlab's Fields Compression Dataset

A [climetlab](https://climetlab.readthedocs.io/en/latest/)'s dataset plugin for [uncompressed 64-bit floating-point atmospheric and wave model outputs](https://apps.ecmwf.int/research-experiments/expver/hplp/) used by the [Fields Compression project](https://github.com/ecmwf-lab/fields-compression).
Each dataset contains uncompressed IEEE-754 Standard (1985) 64-bit floating-point single-time atmospheric and wave model (long window 4Dvar) outputs for experiment version `hplp`. Currently, the following four datasets are available for download:

| #   | Model             | Type           |
| --- | ----------------- | -------------- |
|     | Atmospheric model |                |
| 1   |                   | Model Level    |
| 2   |                   | Pressure Level |
| 3   |                   | Surface        |
|     | Ocean             |                |
| 4   |                   | Wave           |


## Prerequisites

- Linux, Windows, or macOS
- Python (3.7 or later)


## How to install

```
# TODO: Publish on PyPI
git clone https://github.com/ecmwf-lab/climetlab-fields-compression.git
cd climetlab-fields-compression
pip install .
```


## Usage

Climetlab's Fields Compression Dataset `load_dataset` class requires both `model` and `levtype` arguments. The other optional arguments are `levels`, `params`, and `step` to filter out unneeded data. For example, passing `param=['2t']`, as in the example below, will result in downloading only the 2 m air temperature present in the dataset. If you want to check the list of available parameters for each argument to use in each dataset, please see `climetlab_fields_compression/expver-hplp.json`.


### Example

```py
import climetlab as cml

# Download total precipitable water and 2 m air temperature
ds = cml.load_dataset("climetlab-fields-compression",
    model='atmospheric-model', levtype='sfc', param=['2t'])
# Convert data to xarray's Dataset format
ds.to_xarray()
```


## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md)


## Development notes

See [DEVELOP.md](DEVELOP.md)


## Copyright and license

Copyright 2022 ECMWF. Licensed under [Apache License 2.0](LICENSE.txt). In applying this licence, ECMWF does not waive the privileges and immunities granted to it by virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.
