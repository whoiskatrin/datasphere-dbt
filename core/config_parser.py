# core/config_parser.py

import yaml

def read_config(config_path):
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def parse_config(config):
    soda_config = config.get('soda', {})
    great_expectations_config = config.get('great_expectations', {})
    elementary_config = config.get('elementary', {})
    re_data_config = config.get('re_data', {})
    data_diff_config = config.get('data_diff', {})

    return {
        'soda': soda_config,
        'great_expectations': great_expectations_config,
        'elementary': elementary_config,
        're_data': re_data_config,
        'data_diff': data_diff_config,
    }
