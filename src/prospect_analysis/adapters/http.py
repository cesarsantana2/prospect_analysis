import jsonschema
import domain.schema as d_schema
import logic.national_records as l_natioanal_records


def wire_input_to_validate(input_data):
    try:
        jsonschema.validate(input_data, d_schema.lead_information_schema)
    except:
        raise

    return input_data


def prospect_analyzis_result_to_wire(prospect_analysis_result):

    result, context = prospect_analysis_result

    if result:
        message = "OK --\n\nProspect able to be approved"
        print(message)

        return True

    else:
        print(context)

        return False


def process_national_records_result(national_records_result):
    get_juducial_records_response_code = national_records_result[0].staus_code
    get_registry_by_social_number_response_code = national_records_result[1].status_code

    national_records_result_processed, context = l_natioanal_records.scenarios_matrix(get_juducial_records_response_code,
                                                                                      get_registry_by_social_number_response_code)

    return national_records_result_processed, context
