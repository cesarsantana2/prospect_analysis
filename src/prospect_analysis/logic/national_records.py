def scenarios_matrix(juducial_records_response_code,
                     registry_by_social_number_response_code):

    if juducial_records_response_code == 200:
        context = "The person related to this social number have judicial issues."
        return False, context

    if registry_by_social_number_response_code == 404:
        context = "Social number not found at the national registries"
        return False, context

    if juducial_records_response_code == 404 and registry_by_social_number_response_code == 200:
        context = "Prospect able to proceed"
        return True, context

    context = "Something wrong happened, please try again."
    return False, context


def prospect_qualification_check(prospect_score):
    if prospect_score > 60:
        context = "Prospect is able to be approved"
        return True, context
    else:
        context = "Prospect is unnable to be approved based on score qualification"
        return False, context
