import unittest
import allure
import xmlrunner


class ExampleTestSuite(unittest.TestCase):

    @allure.story('Your Story here')
    @allure.feature('Your Feature here')

    @allure.testcase("Test case one.")
    def test_tc1(self):
        assert True == True

    @allure.testcase("Test case two.")
    def test_tc2(self):
        assert True == True

    @allure.testcase("Test case three.")
    def test_tc3(self):
        assert True == False

    @allure.testcase("Test case four.")
    def test_tc4(self):
        assert True == False

    @allure.testcase("Test case five.")
    def test_tc5(self):
        assert True == True

if __name__ == "__main__":
    with open('results.xml', 'wb') as output: unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output),
                                                            failfast=False, buffer=False, catchbreak=False)
