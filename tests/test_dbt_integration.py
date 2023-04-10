# test_dbt_integration.py

from core.dbt_integration import run_data_quality_checks

if __name__ == "__main__":
    config_path = "data_quality_config.yaml"
    run_data_quality_checks(config_path)
