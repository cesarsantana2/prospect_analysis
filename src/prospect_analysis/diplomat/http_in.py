import domain.source as d_source
import adapters.http as a_http


def prospect_analysis(input_data):

    national_id_number, first_name, last_name = a_http.wire_input_to_validate(
        input_data)
    prospect_analysis_result = d_source.prospect_analysis(
        national_id_number, first_name, last_name)
    a_http.prospect_analyzis_result_to_wire(prospect_analysis_result)
