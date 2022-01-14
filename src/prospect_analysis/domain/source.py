from diplomat.http_out import get_juducial_records_by_social_number, get_registry_by_social_number, get_prospect_score

def __registry_identification_analysis(social_number) -> bool:
    registry_response = get_registry_by_social_number(social_number)
    if registry_response.status_code == 404:
        return False
    else:
        return True

def __judicial_records_analysis(social_number) -> bool:
    judicial_records_response = get_juducial_records_by_social_number(social_number)
    if judicial_records_response == 200:
        return False
    else: 
        return True

def __prospect_qualification_check(first_name, last_name) -> bool:
    prospect_score = get_prospect_score(first_name,last_name)
    if prospect_score > 60:
        return True
    else:
        return False

def prospect_analysis(social_number, first_name, last_name):
    regristry_response = __registry_identification_analysis(social_number)
    judicial_records_response = __judicial_records_analysis(social_number)
    prospect_score = __prospect_qualification_check(first_name, last_name)

    return regristry_response, judicial_records_response, prospect_score


