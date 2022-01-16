national_judicial_redords = [{'first_name': 'Charlie', 'last_name': 'Shread', 'national_id_number': 1001, 'cases_id': [123, 431]},
{'first_name': 'Cesar', 'last_name': 'Silva', 'national_id_number': 1002, 'cases_id': [4332, 4321, 1231]},
{'first_name': 'Maju', 'last_name': 'Silva', 'national_id_number': 1003, 'cases_id': [3222]},
{'first_name': 'Mari', 'last_name': 'Shread', 'national_id_number': 1004, 'cases_id': [392]},
{'first_name': 'Murilo', 'last_name': 'Santana', 'national_id_number': 1005, 'cases_id': [22]}]

national_registry_records = [
    {'first_name': 'Charlie', 'last_name': 'Shread', 'national_id_number': 1001, 'marital_status': 'Married', 'age': 33, 'gender': 'Masculine'},
    {'first_name': 'Cesar', 'last_name': 'Silva', 'national_id_number': 1002, 'marital_status': 'Married', 'age': 29, 'gender': 'Masculine'},
    {'first_name': 'Maju', 'last_name': 'Silva', 'national_id_number': 1003, 'marital_status': 'Married', 'age': 30, 'gender': 'Feminine'},
    {'first_name': 'Mari', 'last_name': 'Shread', 'national_id_number': 1004, 'marital_status': 'Married', 'age': 32, 'gender': 'Feminine'},
    {'first_name': 'Murilo', 'last_name': 'Santana', 'national_id_number': 1005, 'marital_status': 'Married', 'age': 60, 'gender': 'Masculine'},
    {'first_name': 'Marci', 'last_name': 'Carvalho', 'national_id_number': 1006, 'marital_status': 'Married', 'age': 61, 'gender': 'Feminine'},
    {'first_name': 'Isac', 'last_name': 'Santos', 'national_id_number': 1007, 'marital_status': 'Single', 'age': 22, 'gender': 'Masculine'},
    {'first_name': 'Guilherme', 'last_name': 'Barreto', 'national_id_number': 1008, 'marital_status': 'Single', 'age': 20, 'gender': 'Masculine'},
    {'first_name': 'Cecilia', 'last_name': 'Muniz', 'national_id_number': 1009, 'marital_status': 'Single', 'age': 18, 'gender': 'Feminine'},
    {'first_name': 'Clarice', 'last_name': 'Lispector', 'national_id_number': 1010, 'marital_status': 'Single', 'age': 18, 'gender': 'Feminine'}
]

def check_national_judicial_data_mock(social_number):
    for record in national_judicial_redords:
        if record['national_id_number'] == social_number:
            return record, national_judicial_redords.index(record)
    return None, None

def check_national_registry_data_mock(social_number):
    for record in national_registry_records:
        if record['national_id_number'] == social_number:
            return record, national_registry_records.index(record)
    return None, None
