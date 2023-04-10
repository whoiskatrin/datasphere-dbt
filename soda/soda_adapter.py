
from core.data_quality_base import DataQualityBase

class SodaAdapter(DataQualityBase):

    def validate(self, config):
        self.results = validation_results

    def test(self, config):
        self.results = test_results

    def report(self, config):
        pass
