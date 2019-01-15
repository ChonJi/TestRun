import Checker
from ReportProvider import ReportProvider
import xml.etree.ElementTree as element_tree

class Parser:

    def get_actual_failures(self):

        test_cases_list = []
        ReportProvider(Checker.ARTIFACT_ID)
        tree = element_tree.parse('actual_report.xml')
        for parent in tree.findall('.//failure/..'):
            test_cases_list.append(parent.attrib['name'])
        return test_cases_list

    def get_accepted_failures(self):

        accepted_failures_list = []
        tree = element_tree.parse('can_fail_list.xml')
        root = tree.getroot()
        for failure in root.iter('testcase'):
            accepted_failures_list.append(failure.text)
        return accepted_failures_list

    def check_status(self):

        differences_list = []

        for element in self.get_actual_failures():
            if element not in self.get_accepted_failures():
                differences_list.append(element)

        return differences_list

# parser = Parser()
# for failure in parser.get_actual_failures():
#     print(failure)
#
# print('***************************')
#
# for accepted_failure in parser.get_accepted_failures():
#     print(accepted_failure)
#
# print('*****************************')