# dbt Datasphere Plugin

The dbt Datasphere Plugin is a powerful and flexible solution for integrating multiple open-source data quality frameworks into your dbt projects. It unifies Soda SQL, Great Expectations, Datafold, providing a single interface to configure and run data quality checks.

## Features

- Unified interface to configure and run data quality checks
- Support for Soda SQL, Great Expectations, Datafold
- Consolidated results from all frameworks
- Customizable reporting

## Installation

Install the plugin using pip:

`pip install [TBD]`

## Usage

Configure data quality checks for each framework in a YAML configuration file (e.g., data_quality_config.yaml). Consult the documentation of each framework for specific configuration settings and rules.

Run data quality checks using the run_data_quality_checks function in the dbt_integration.py file:

```from core.dbt_integration import run_data_quality_checks

if __name__ == "__main__":
    config_path = "data_quality_config.yaml"
    run_data_quality_checks(config_path)
```

Check the generated report (e.g., data_quality_report.html) for the consolidated results from all frameworks.

## Configuration

The configuration file (data_quality_config.yaml) should include settings and rules for each data quality framework. Here's a sample structure:

```
soda:
  # Soda SQL configuration settings and rules

great_expectations:
  # Great Expectations configuration settings and rules

datadiff:
  # Datafold configuration settings and rules

```

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request, open an issue, or reach out to the maintainers.

## License

This project is licensed under the MIT License.
