import domain.schema as d_schema
import domain.source as d_source
import adapters.secundary as a_secundary
import jsonschema

def prospect_analysis(input_data):
   
    try:
        jsonschema.validate(input_data, d_schema.lead_information_schema)
    except:
        raise 

    national_id_number, first_name, last_name = input_data
    prospect_analysis_restul = d_source.prospect_analysis(national_id_number, first_name, last_name)
    a_secundary.prospect_result_adapted(prospect_analysis_restul)
