# Climetlab's Fields Compression Dataset

A [climetlab](https://climetlab.readthedocs.io/en/latest/)'s dataset plugin for [uncompressed 64-bit floating-point atmospheric and wave model outputs](https://apps.ecmwf.int/research-experiments/expver/hplp/) used by the [Fields Compression project](https://github.com/ecmwf-lab/fields-compression).
Each dataset contains uncompressed IEEE-754 Standard (1985) 64-bit floating-point single-time atmospheric and wave model (long window 4Dvar) outputs for experiment version `hplp`. 


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

After installation, climetlab's load dataset class `climetlab.load_dataset` can be used to download the Fields Compression datasets by passing `climetlab-fields-compression` to the constructor and by specifying the `model` and `levtype` arguments (see table below for options). Other optional arguments are `levels`, `params`, and `step` (see table below for options). If optional arguments are not specified, the whole set will be downloaded.

| `model`             | `levtype` | `param`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `levelist`                                                                                  | `step`            |
| ------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------- |
| `atmospheric-model` | `ml`      | ['cc', 'ciwc', 'clwc', 'crwc', 'cswc', 'd', 'lnsp', 'o3', 'q', 't', 'vo', 'w', 'z', 'u', 'v']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [1, 2, ..., 137]                                                                            | [0, 12, ..., 240] |
| `atmospheric-model` | `pl`      | ['d', 'q', 'r', 't', 'vo', 'w', 'z', 'u', 'v']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 150, 200, 250, 300, 400, 500, 700, 850, 925, 1000] | [0, 12, ..., 240] |
| `atmospheric-model` | `sfc`     | ['10fg', '10u', '10v', '2d', '2t', 'asn', 'bld', 'blh', 'cape', 'chnk', 'ci', 'cin', 'cp', 'crr', 'csfr', 'dsrp', 'e', 'es', 'ewss', 'fal', 'flsr', 'fsr', 'fzra', 'gwd', 'hcc', 'i10fg', 'ie', 'iews', 'ilspf', 'inss', 'ishf', 'istl1', 'istl2', 'istl3', 'istl4', 'kx', 'lcc', 'lgws', 'lsm', 'lsp', 'lspf', 'lsrr', 'lssfr', 'mcc', 'mgws', 'mn2t', 'msl', 'mx2t', 'nsss', 'ocu', 'ocv', 'par', 'pev', 'ptype', 'ro', 'rsn', 'sd', 'sf', 'skt', 'slhf', 'smlt', 'src', 'sro', 'sshf', 'ssr', 'ssrc', 'ssrd', 'ssro', 'sst', 'stl1', 'stl2', 'stl3', 'stl4', 'str', 'strc', 'strd', 'sund', 'swvl1', 'swvl2', 'swvl3', 'swvl4', 'tcc', 'tciw', 'tclw', 'tco3', 'tcrw', 'tcsw', 'tcw', 'tcwv', 'tisr', 'totalx', 'tp', 'tsn', 'tsr', 'tsrc', 'ttr', 'ttrc', 'uvb', 'vimd', 'vis', 'z'] | `None`                                                                                      | [0, 12, ..., 240] |
| `ocean-model`       | `wave`    | ['cdww', 'dwi', 'hmax', 'mp1', 'mp2', 'mwd', 'mwp', 'phioc', 'pp1d', 'rhoao', 'swh', 'tauoc', 'ust', 'vst', 'wdw', 'wind', 'wmb', 'wstar', 'wind', 'dwi']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `None`                                                                                      | [0, 12, ..., 240] |




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
