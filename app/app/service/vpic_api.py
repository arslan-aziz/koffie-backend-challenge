from urllib.parse import urljoin, urlencode
import requests

from app import schemas
from app.service import ApiBase


class VpicApi(ApiBase):

    VIN_MAKE_ID = 26
    VIN_MODEL_ID = 28
    VIN_MODEL_YEAR_ID = 29
    VIN_BODY_CLASS_ID = 5

    def __init__(self, url):
        ApiBase.__init__(self, url, "vPIC API")

    def _parse_vin_data(self, vin_response):
        vin_make = list(
            filter(
                lambda x: x["VariableId"] == self.VIN_MAKE_ID, vin_response["Results"]
            )
        )[0]["Value"]
        vin_model = list(
            filter(
                lambda x: x["VariableId"] == self.VIN_MODEL_ID, vin_response["Results"]
            )
        )[0]["Value"]
        vin_model_year = list(
            filter(
                lambda x: x["VariableId"] == self.VIN_MODEL_YEAR_ID,
                vin_response["Results"],
            )
        )[0]["Value"]
        vin_body_class = list(
            filter(
                lambda x: x["VariableId"] == self.VIN_BODY_CLASS_ID,
                vin_response["Results"],
            )
        )[0]["Value"]

        return {
            "make": vin_make,
            "model": vin_model,
            "model_year": vin_model_year,
            "body_class": vin_body_class,
        }

    def decode_vin(self, vin: str) -> schemas.VinCreate:
        """Use vPIC API to decode vin to vehicle properties.

        :param vin: Vehicle identifier string.

        :return: VinCreate object with vehicle properties.
        """
        params = {"format": "json"}

        # make request to api
        endpoint = f"/api/vehicles/DecodeVin/{vin}"
        vin_data = self.get_request(endpoint, params)

        # parse vin data
        vin_data_parsed = self._parse_vin_data(vin_data)
        vin_data_parsed["vin"] = vin
        vin_create_obj = schemas.VinCreate(**vin_data_parsed)

        return vin_create_obj
