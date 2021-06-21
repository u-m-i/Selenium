from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTest
from tubesearch import TubeTest
from register_new_user import RegisterNewUser

# Get our test from another file, with the unittest modules.through the TestLoader method : loadTestsFromTestCase.
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)
tube_test = TestLoader().loadTestsFromTestCase(TubeTest)
new_user = TestLoader().loadTestsFromTestCase(RegisterNewUser)

# Make a list to execute our testing files

smoke_test = TestSuite([assertions_test, search_test, tube_test, new_user])

# And create a dicctinary to give the kwargs to our HTMLTestRunner

kwargs = {
    "output" : 'search_report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

