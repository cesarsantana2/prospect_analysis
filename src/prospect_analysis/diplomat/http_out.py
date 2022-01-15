import requests
import requests_mock 

def get_juducial_records_by_social_number(social_number):

    session = requests.Session()
    mock_adapter = requests_mock.Adapter()
    session.mount('https://', mock_adapter)

    mock_adapter.register_uri('GET', 'http://nationaljudicialrecords/search=1', )

    response = requests.get('https://google.com')
    return response 

def get_registry_by_social_number(social_number):
    response = requests.get('https://google.com')
    return response 

def get_prospect_score(first_name, last_name):
    response = requests.get('https://google.com')
    return response 