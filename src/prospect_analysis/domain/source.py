from diplomat.http_out import get_prospect_score


def __prospect_qualification_check(first_name, last_name) -> bool:
    prospect_score = get_prospect_score(first_name,last_name)
    if prospect_score > 60:
        return True
    else:
        return False

# def prospect_analysis(social_number, first_name, last_name):
#     (social_number)
    
#     prospect_score = __prospect_qualification_check(first_name, last_name)

#     return regristry_response, judicial_records_response, prospect_score


