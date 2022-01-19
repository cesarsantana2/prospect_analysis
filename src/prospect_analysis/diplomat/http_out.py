import requests
import requests_mock 
import fixtures
import json
import random
import time
import asyncio


result = []

async def __get_juducial_records_by_social_number(social_number):

    url = format('http://nationaljudicialrecords/check?id=%s' %social_number)
    record, record_index = fixtures.check_national_judicial_data_mock(social_number)

    # mock_latance = random.randrange(0,5,2)

    if record == None:
        with requests_mock.Mocker(real_http=True) as m:
            m.get(url, text="NOT FOUND", status_code=404)
            response = requests.get(url, timeout=5).text
            result.append(response)
            return response
    else:
        with requests_mock.Mocker(real_http=True) as m:
            text = json.dumps(fixtures.national_judicial_redords[record_index])
            m.get(url, text=text, status_code=200)
            response = requests.get(url, timeout=5).text
            result.append(response)
            return response
    

async def __get_registry_by_social_number(social_number):
    
    url = format('https://nationalregistryidentification/check?id=%s' %social_number)
    record, record_index = fixtures.check_national_registry_data_mock(social_number)

    if record == None:
        with requests_mock.Mocker(real_http=True) as m:
            m.get(url, text="NOT FOUND", status_code=404)
            response = requests.get(url, timeout=5).text
            result.append(response)
            return response
    else:
        with requests_mock.Mocker(real_http=True) as m:
            text = json.dumps(fixtures.national_registry_records[record_index])
            m.get(url, text=text, status_code=200)
            response = requests.get(url, timeout=5).text
            result.append(response)
            return response

async def get_national_records_threading(social_number):

    result = await asyncio.gather(
        __get_juducial_records_by_social_number(social_number),
        __get_registry_by_social_number(social_number)
    )
    return result

def get_prospect_score(first_name, last_name):
    response = requests.get('https://google.com')
    return response     


result = asyncio.run(get_national_records_threading(1001))
print(result)