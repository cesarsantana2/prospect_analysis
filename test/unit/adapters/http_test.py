import unittest
from .. import http


def test_wire_input_to_validate():

    assertion = (1001, "cesar", "santana")
    payload = '{"national_id_number" : 1001, "first_name" : "cesar", "last_name" : "santana"}'

    result = http.wire_input_to_validate(payload)

    unittest.assertEqual(assertion, result)
