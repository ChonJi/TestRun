import unittest
import xmlrunner


class ExampleTestSuite(unittest.TestCase):

    def test_tc1(self):
        assert True == False

    def test_tc2(self):
        assert True == True

    def test_tc3(self):
        assert True == True

    def test_tc4(self):
        assert True == False

    def test_tc5(self):
        assert True == True

    print("I've been trying for all day long!")

if __name__ == "__main__":
    if __name__ == '__main__':
        with open('results.xml', 'wb') as output:unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)