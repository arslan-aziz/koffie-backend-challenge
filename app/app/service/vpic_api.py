from urllib.parse import urljoin, urlencode
import requests

from app import schemas


class VpicApi:
    def __init__(self, api_url):
        self.api_url = api_url

    def decode_vin(self, vin: str) -> schemas.VinCreate:
        """Use VPIC API to decode vin to vehicle properties.

        :param vin: Vehicle identifier string.

        :return: VinCreate object with vehicle properties.
        """
        def _parse_vin_data(vin_response):
            VIN_MAKE_ID = 26
            VIN_MODEL_ID = 28
            VIN_MODEL_YEAR_ID = 29
            VIN_BODY_CLASS_ID = 5
            vin_make = list(filter(lambda x: x['VariableId'] == VIN_MAKE_ID, vin_response['Results']))[0]['Value']
            vin_model = list(filter(lambda x: x['VariableId'] == VIN_MODEL_ID, vin_response['Results']))[0]['Value']
            vin_model_year = list(filter(lambda x: x['VariableId'] == VIN_MODEL_YEAR_ID, vin_response['Results']))[0]['Value']
            vin_body_class = list(filter(lambda x: x['VariableId'] == VIN_BODY_CLASS_ID, vin_response['Results']))[0]['Value']
            return {
                'make': vin_make,
                'model': vin_model,
                'model_year': vin_model_year,
                'body_class': vin_body_class
            }

        params = urlencode({
            'format': 'json',
        })
        endpoint = '/api/vehicles/DecodeVin/{}?{}'.format(
            vin,
            params
        )
        full_url = urljoin(self.api_url, endpoint)

        r = requests.get(full_url)
        r.raise_for_status()
        vin_data = r.json()
        vin_data_parsed = _parse_vin_data(vin_data)
        vin_data_parsed['vin'] = vin

        print(vin_data_parsed)

        vin_create_obj = schemas.VinCreate(**vin_data_parsed)
        return vin_create_obj