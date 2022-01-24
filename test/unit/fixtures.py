import requests_mock
import requests


first_url_mock = "https://first_mock.com"
second_url_mock = "https://second_mock.com"
national_records_result_mock = []


def mocking_judicial_records_response():
    with requests_mock.Mocker(real_http=True) as m:
        m.get(first_url_mock, text="NOT FOUND", status_code=404)

        response = requests.get(first_url_mock)

        return response


def mocking_national_registry_response():
    with requests_mock.Mocker(real_http=True) as m:
        m.get(second_url_mock, text="Mock text", status_code=200)

        response = requests.get(second_url_mock)

        return response


def generate_national_records_result():

    judicial_records_mock_response = mocking_judicial_records_response()
    national_registry_mock_response = mocking_national_registry_response()

    national_records_result_mock.append(judicial_records_mock_response)
    national_records_result_mock.append(national_registry_mock_response)

    return national_records_result_mock


result = generate_national_records_result()
print(result)
