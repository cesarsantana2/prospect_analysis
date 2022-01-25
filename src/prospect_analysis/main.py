import sys
import json
from diplomat import http_in

input_data = json.loads(sys.argv[1])


def main(input_data):
    http_in.prospect_analysis(input_data)


main(input_data)