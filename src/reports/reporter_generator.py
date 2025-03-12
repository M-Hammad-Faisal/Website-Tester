from .allure_reporter import AllureReporter
from .html_reporter import HTMLReporter
from .reporters import Reporters


class ReportGenerator:
    @staticmethod
    def generate(report_type, results):
        if report_type == Reporters.ALLURE:
            AllureReporter.generate(results)
        elif report_type == Reporters.HTML:
            HTMLReporter.generate(results)
        raise Exception("Unknown report type: {}".format(report_type))
