lead_information_schema = {
    "type" : "object",
    "properties" : {
        "national_id_number" : {"type" : "number"},
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"}
    }
}

national_identification_response = {
    "type" : "object",
    "properties" : {
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"},
        "national_id_number" : {"type" : "number"},
        "marital_status" : {"type" : "str"},
        "age" : {"type" : "number"},
        "gender" : {"type" : "string"}
    }
}
    
national_judicial_response = {
    "type" : "object",
    "properties" : {
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"},
        "national_id_number" : {"type" : "number"},
        "cases_id" : {"type" :  ["number"]}
    }
}
