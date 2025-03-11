import allure


class AllureReporter:
    @staticmethod
    def generate(results):
        for result in results:
            with allure.step(f"Test: {result['test']}"):
                if result["status"] == "Pass":
                    allure.attach(f"{result['test']} passed", name="Result",
                                  attachment_type=allure.attachment_type.TEXT)
                else:
                    allure.attach(f"Error: {result['error']}", name="Result",
                                  attachment_type=allure.attachment_type.TEXT)
                    allure.severity(allure.severity_level.CRITICAL)
