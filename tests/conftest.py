def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    print("Configuration Check", config)


def pytest_sessionstart():
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    print("Starting to run all tests")


def pytest_sessionfinish(exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    print(f"All tests have been completed with Exit Status: {exitstatus}")
