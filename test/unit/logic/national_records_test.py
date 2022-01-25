from ....src.prospect_analysis.logic import national_records


def test_scenarios_matrix():

    first_scenario_result = national_records.scenarios_matrix(200, 400)
    first_scenario_assertion = False, "The person related to this social number have judicial issues."

    second_scenario_result = national_records.scenarios_matrix(404, 404)
    second_scenario_assertion = False, "Social number not found at the national registries"

    third_scenario_result = national_records.scenarios_matrix(404, 200)
    third_scenario_assertion = True, "Prospect able to proceed"

    fourth_scenario_result = national_records.scenarios_matrix(201, 201)
    fourth_cenario_assertion = False, "Something wrong happened, please try again."

    assert first_scenario_result == first_scenario_assertion
    assert second_scenario_result == second_scenario_assertion
    assert third_scenario_result == third_scenario_assertion
    assert fourth_scenario_result == fourth_cenario_assertion

def test_qualification_check():

    approved = True, "Prospect is able to be approved"
    denied = False, "Prospect is unnable to be approved based on score qualification"

    first_case = national_records.prospect_qualification_check(60)
    second_case = national_records.prospect_qualification_check(61)
    
    assert first_case == denied
    assert second_case == approved

