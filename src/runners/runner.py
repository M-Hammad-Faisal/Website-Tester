import argparse
import sys
import pytest

from src.browsers import Browser
from src.config import Config, setup_logging, Framework
from src.reports import Reporters

logger = setup_logging()


def main():
    parser = argparse.ArgumentParser(description="Website Tester Runner")
    parser.add_argument(
        "--framework",
        choices=[Framework.PLAYWRIGHT, Framework.SELENIUM],
        default=Framework.PLAYWRIGHT,
        help=f"Framework: {Framework.PLAYWRIGHT} or {Framework.SELENIUM}"
    )
    parser.add_argument(
        "--browser",
        choices=[Browser.CHROME, Browser.FIREFOX, Browser.MSEDGE],
        default=Browser.CHROME,
        help=f"Browser: {Browser.CHROME}, {Browser.FIREFOX}, or {Browser.MSEDGE}"
    )
    parser.add_argument(
        "--report",
        choices=[Reporters.ALLURE, Reporters.HTML],
        default=Reporters.ALLURE,
        help=f"Reporter: {Reporters.ALLURE} or {Reporters.HTML}"
    )
    parser.add_argument(
        "--tests",
        default="src/tests"
    )
    parser.add_argument(
        "--retries",
        default="3"
    )
    parser.add_argument(
        "--numprocesses",
        type=int,
        default=1,
        help="Number of parallel processes (use 'auto' for CPU count)"
    )

    args, unknown = parser.parse_known_args()

    pytest_args = [
        args.tests,
        f"--framework={args.framework}",
        f"--browser={args.browser}",
        "-v",
        "--retries", args.retries
    ]

    if args.report == Reporters.ALLURE:
        pytest_args.append("--alluredir={}".format(Config.ALLURE_RESULTS_DIR))

    if args.numprocesses != "1":
        try:
            num = int(args.numprocesses)
            if num > 1:
                pytest_args.extend(["-n", str(num)])
        except ValueError:
            if args.numprocesses.lower() == "auto":
                pytest_args.extend(["-n", "auto"])
            else:
                logger.error(f"Invalid --numprocesses value: {args.numprocesses}. Use a number or 'auto'.")
                sys.exit(1)

    pytest_args.extend(unknown)

    logger.info(f"Starting test run with args: {pytest_args}")
    result = pytest.main(pytest_args)
    logger.info(f"Test run completed with exit code: {result}")
    print(f"pytest exit code: {result}")

    sys.exit(result)


if __name__ == "__main__":
    main()
