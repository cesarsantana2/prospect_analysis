from . import fixtures
import requests
import requests_mock
import json
import random
import time
import asyncio


async def __get_juducial_records_by_social_number(social_number):

    url = format('http://nationaljudicialrecords/check?id=%s' % social_number)
    record, record_index = fixtures.check_national_judicial_data_mock(
        social_number)

    mock_latance = random.randrange(0, 7, 2)

    time.sleep(mock_latance)

    if record == None:
        with requests_mock.Mocker(real_http=True) as m:
            m.get(url, text="NOT FOUND", status_code=404)
            response = requests.get(url)

            return response
    else:
        with requests_mock.Mocker(real_http=True) as m:
            text = json.dumps(fixtures.national_judicial_redords[record_index])
            m.get(url, text=text, status_code=200)
            response = requests.get(url)

            return response


async def __get_registry_by_social_number(social_number):

    url = format(
        'https://nationalregistryidentification/check?id=%s' % social_number)
    record, record_index = fixtures.check_national_registry_data_mock(
        social_number)

    mock_latance = random.randrange(0, 7, 2)

    time.sleep(mock_latance)

    if record == None:
        with requests_mock.Mocker(real_http=True) as m:
            m.get(url, text="NOT FOUND", status_code=404)
            response = requests.get(url)

            return response
    else:
        with requests_mock.Mocker(real_http=True) as m:
            text = json.dumps(fixtures.national_registry_records[record_index])
            m.get(url, text=text, status_code=200)
            response = requests.get(url)

            return response


async def get_national_records_coroutines(social_number):

    result = await asyncio.gather(
        __get_juducial_records_by_social_number(social_number),
        __get_registry_by_social_number(social_number)
    )
    return result


def get_prospect_score(first_name, last_name):

    url = format(
        "https://prospectqualification.internal.com/check?firstname={first_name}&lastname={last_name}")
    mock_prospect_score = str(random.randrange(30, 101, 10))

    with requests_mock.Mocker(real_http=True) as m:
        m.get(url, text=mock_prospect_score, status_code=200)
        response = requests.get(url)

        return response
