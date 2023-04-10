# core/dbt_integration.py

from soda.soda_adapter import SodaAdapter
from core.config_parser import read_config, parse_config
from great_expectations.great_expectations_adapter import GreatExpectationsAdapter
from datadiff.datadiff_adapter import DataDiffAdapter

def consolidate_results(adapters):
    consolidated_results = {}
    for adapter_name, adapter in adapters.items():
        consolidated_results[adapter_name] = adapter.get_results()
    return consolidated_results

def generate_html_report(consolidated_results):
    html_string = "<html><head><title>Data Quality Report</title></head><body>"
    html_string += "<h1>Data Quality Report</h1>"

    for framework, results in consolidated_results.items():
        html_string += f"<h2>{framework.capitalize()}</h2>"
        html_string += "<ul>"
        for result in results:
            html_string += f"<li>{result}</li>"
        html_string += "</ul>"

    html_string += "</body></html>"

    with open("data_quality_report.html", "w") as report_file:
        report_file.write(html_string)

def generate_report(consolidated_results):
    generate_html_report(consolidated_results)

def run_data_quality_checks(config_path):
    config = read_config(config_path)
    parsed_config = parse_config(config)

    soda_adapter = SodaAdapter()
    great_expectations_adapter = GreatExpectationsAdapter()
    datadiff_adapter = DataDiffAdapter()

    adapters = {
        'soda': soda_adapter,
        'great_expectations': great_expectations_adapter,
        'datadiff': datadiff_adapter,
    }

    for adapter_name, adapter in adapters.items():
        adapter.validate(parsed_config[adapter_name])
        adapter.test(parsed_config[adapter_name])
        adapter.report(parsed_config[adapter_name])

    consolidated_results = consolidate_results(adapters)
    generate_report(consolidated_results)
