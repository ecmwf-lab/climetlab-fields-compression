# (C) Copyright 2022 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from pathlib import Path

import json

import climetlab as cml
from climetlab import Dataset
from climetlab.decorators import normalize

__version__ = "0.1.0"


class Main(Dataset):
    name = "Climetlab's Fields Compression Dataset"
    home_page = "https://github.com/ecmwf-lab/climetlab-fields-compression"
    # The licence is the licence of the data (not the licence of the plugin)
    licence = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    documentation = "https://github.com/ecmwf-lab/climetlab-fields-compression"
    citation = "https://doi.org/10.21957/r6rk-7978"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://github.com/ecmwf-lab/"
        "climetlab-climetlab-fields-compression/"
        "blob/main/LICENSE. "
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    def __init__(self, model, levtype, levels=None, param=None, step=None):

        with open(Path(__file__).parent / 'expver-hplp.json', 'r') as f:
            mars_config = json.load(f)

        validate_mars_request(data=mars_config, model=model,
            levtype=levtype, levels=levels, param=param, step=step)
            
        mars_request = patch_mars_request(data=mars_config, model=model,
            levtype=levtype, levels=levels, param=param, step=step)

        self.source = cml.load_source("mars", **mars_request)


def validate_mars_request(data, model, levtype, levels, param, step):

    models = data.keys()
    if model not in models:
        raise ValueError(f'{model} not avalable. Avalable models are {models}')

    if model != 'ocean-model':
        levtypes = data[model].keys()
        if levtype not in levtypes:
            raise ValueError(
                f'{levtype} not avalable. Avalable model types are {levtypes}')

        if levels:
            levelist = data[model][levtype]['levelist']
            if not all(elem in levelist for elem in levels):
                raise ValueError(
                    f'Check your list of levels. Passed {levels}. Valid levels are: {levelist}')

    if param:
        json_param = data[model][levtype]['param']
        if not all(elem in json_param for elem in param):
            raise ValueError(
                f'Check your list of parameters. Passed {param}. Valid parameters are: {json_param}')

    if step:
        json_step = data[model][levtype]['step']
        if not all(elem in json_step for elem in step):
            raise ValueError(
                f'Check your list of steps. Passed {step}. Valid parameters are: {json_step}')


def patch_mars_request(data, model, levtype, levels, param, step):
    mars_request = data[model][levtype].copy()
    if levels:
        mars_request['levelist'] = levels
    if param:
        mars_request['param'] = param
    if step:
        mars_request['step'] = step
    return mars_request
