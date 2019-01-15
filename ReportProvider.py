import requests

class ReportProvider:

    def __init__(self, artifact_id):

        url = f"https://gitlab.com/ChonJi1983/TestRun/-/jobs/{artifact_id}/artifacts/raw/results.xml"
        response = requests.get(url)
        with open('actual_report.xml', 'wb') as output:
            output.write(response.content)
















