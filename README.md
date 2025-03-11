# Website Tester

A robust test automation framework for testing the [SauceDemo](https://www.saucedemo.com/) website, built with Python,
Selenium, and Playwright. This project demonstrates advanced automation techniques with a focus on scalability,
reliability, and performance.

## Features

- **50 Automated Tests**: Comprehensive coverage of login, inventory, cart, checkout, logout, error handling, social
  links, item details, sorting, and performance.
- **Multi-Browser Support**: Runs tests on Chrome, Firefox, and Edge for both Selenium and Playwright.
- **Dual Framework**: Supports Selenium and Playwright for flexibility and comparison.
- **Parallel Execution**: Speeds up test runs using `pytest-xdist` with configurable process counts.
- **Page Object Model**: Clean, maintainable design with a factory pattern for page abstraction.
- **Allure Reporting**: Detailed, visually appealing test reports with screenshots.
- **Logging**: Execution details logged to `logs/test_run.log` for debugging and traceability.
- **CI/CD**: GitHub Actions workflow for automated testing across frameworks and browsers.

## Project Structure

   ```txt
   website_tester/
   ├── src/
   │   ├── pages/           # Page objects and selectors
   │   ├── tests/           # 50 tests across 10 files
   │   ├── runners/         # Test runner script
   │   ├── config/          # Logging and configuration
   ├── logs/                # Test execution logs
   ├── allure-results/      # Allure report data
   ├── screenshots/         # Sample report images
   ├── requirements.txt     # Dependencies
   └── .github/workflows/   # CI/CD configuration
   ```

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/M-Hammad-Faisal/Website-Tester.git
   cd Website-Tester
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
    ```bash
   pip install -r requirements.txt
   playwright install
   playwright install firefox
   playwright install msedge
   ```
4. **Run tests**:
   ```bash
   # Selenium with Firefox, 4 parallel processes
   python -m src.runners.runner --framework=selenium --browser=firefox --numprocesses=4 --report=allure
   # Playwright with Edge, auto processes
   python -m src.runners.runner --framework=playwright --browser=edge --numprocesses=auto --report=allure
   # Single process (default)
   python -m src.runners.runner --framework=selenium --browser=chrome --report=allure
   # View Allure report
   allure serve allure-results/
   ```

## Test Suite

- Login: 6 tests
- Inventory: 5 tests
- Cart: 5 tests
- Checkout: 5 tests
- Logout: 5 tests
- Error Handling: 5 tests
- Social Links: 3 tests
- Item Details: 5 tests
- Sorting: 4 tests
- Performance: 7 tests

## CI/CD

Automated testing runs on every push or pull request via GitHub Actions. See the (workflow)[https://github.com/M-Hammad-Faisal/Website-Tester/.github/workflows/ci.yml] for details. Tests execute
across all frameworks and browsers in parallel.

### Sample Report

Generate a report and view it locally:

   ```bash
   python -m src.runners.runner --framework=playwright --browser=chrome --report=allure
   allure generate allure-results/ -o allure-report/ --clean
   allure open allure-report/
   ```

## Requirements

- Python: 3.12+
- Dependencies: Listed in requirements.txt
    - pytest, playwright, selenium, webdriver-manager, allure-pytest, pytest-retry, pytest-xdist

## Usage Examples

- Run with Selenium on Edge:

   ```bash
   python -m src.runners.runner --framework=selenium --browser=edge --numprocesses=2 --report=allure
   ```

- Run with Playwright on Firefox, single process:

   ```bash
   python -m src.runners.runner --framework=playwright --browser=firefox --report=allure
   ```

- Check logs:
   ```bash
   cat logs/test_run.log
   ```

## Development Notes
- Parallel Execution: Use --numprocesses to leverage pytest-xdist. Set to auto to use all CPU cores.
- Logging: Logs are stored in logs/ for each run, timestamped with execution details.
- Extensibility: Add new browsers (e.g., WebKit) or tests by updating runner.py and page objects.

## Contributing
Feel free to fork, submit PRs, or raise issues for enhancements!

## License
MIT License - free to use and modify.