# core/data_quality_base.py

from abc import ABC, abstractmethod

class DataQualityBase(ABC):
    def __init__(self):
        self.results = []

    @abstractmethod
    def validate(self, config):
        pass

    @abstractmethod
    def test(self, config):
        pass

    @abstractmethod
    def report(self, config):
        pass

    def get_results(self):
        return self.results
