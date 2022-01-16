import requests
import requests_mock 
import fixtures
import json

def get_juducial_records_by_social_number(social_number):

    url = format('http://nationaljudicialrecords/check?id=%s' %social_number)
    record, record_index = fixtures.check_national_judicial_data_mock(social_number)

    if record == None:
        with requests_mock.Mocker(real_http=True) as m:
            m.get(url, text="NOT FOUND", status_code=404)
            response = requests.get(url).text
            return response
    else:
        with requests_mock.Mocker(real_http=True) as m:
            text = json.dumps(fixtures.national_judicial_redords[record_index])
            m.get(url, text=text, status_code=200)
            response = requests.get(url).text
            return response
    

def get_registry_by_social_number(social_number):
    
    url = format('https://nationalregistryidentification/check?id=%s' %social_number)
    record, record_index = fixtures.check_national_registry_data_mock(social_number)

    if record == None:
        with requests_mock.Mocker(real_http=True) as m:
            m.get(url, text="NOT FOUND", status_code=404)
            response = requests.get(url).text
            return response
    else:
        with requests_mock.Mocker(real_http=True) as m:
            text = json.dumps(fixtures.national_registry_records[record_index])
            m.get(url, text=text, status_code=200)
            response = requests.get(url).text
            return response

def get_prospect_score(first_name, last_name):
    response = requests.get('https://google.com')
    return response 