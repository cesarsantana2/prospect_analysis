from src.prospect_analysis.adapters import http
from test.unit import fixtures


def test_wire_input_to_validate():

    assertion = [1001, "cesar", "santana"]
    payload = {"national_id_number": 1001,
               "first_name": "cesar", "last_name": "santana"}

    result = http.wire_input_to_validate(payload)

    assert assertion == result


def test_prospect_score_response_to_value():

    first_result = http.prospect_score_response_to_value("80")
    second_result = http.prospect_score_response_to_value("90")
    third_result = http.prospect_score_response_to_value("40")

    assert first_result == 80
    assert second_result == 90
    assert third_result == 40


def test_prospect_analyzis_result_to_wire():

    first_payload = False, "Context"
    second_payload = True, "Context"

    assert http.prospect_analyzis_result_to_wire(first_payload) == False
    assert http.prospect_analyzis_result_to_wire(second_payload) == True


def test_process_national_records_result():

    national_records_mock = fixtures.generate_national_records_result()
    assertion = True, "Prospect able to proceed"
    response = http.process_national_records_result(national_records_mock)

    assert response == assertion
