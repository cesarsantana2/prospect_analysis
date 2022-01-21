import diplomat.http_out as d_http_out
import logic.national_records as l_national_records
import adapters.http as a_http
import asyncio


def __prospect_qualification_check(first_name, last_name) -> bool:
    prospect_score_response = d_http_out.get_prospect_score(
        first_name, last_name)
    score_value = a_http.prospect_score_response_to_value(
        prospect_score_response)
    check_result, context = l_national_records.prospect_qualification_check(
        score_value)

    return check_result, context


def __get_national_records(social_number):
    national_records_result = asyncio.run(
        d_http_out.get_national_records_coroutines(social_number))

    return national_records_result


def prospect_analysis(social_number, first_name, last_name):

    national_records_result = __get_national_records(social_number)
    national_records_result_processed, context = a_http.process_national_records_result(
        national_records_result)

    if national_records_result_processed:

        check_result, context = __prospect_qualification_check(
            first_name, last_name)

        return check_result, context

    return national_records_result_processed, context
