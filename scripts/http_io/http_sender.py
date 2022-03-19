import requests
from pydantic import BaseModel
from requests import Response

class HttpSender:

    def __init__(self, host_address: str, port: int, message_type: str, station_id: int, domain: str):
        self.ip_address = host_address
        self.port = port
        self.message_type = message_type
        self.url_address = 'http://{0}:{1}/{2}/{3}'.format(self.ip_address, self.port, domain, self.message_type)
        print(self.url_address)
        self.station_id = station_id
        self.station_id_str = 'station_id'

    def additional_checking(self, response: requests.Response, *args, **kwargs) -> None:
        pass

    def wrong_connection_service(self, response: requests.Response) -> None:
        pass

    def check_response_is_ok(self, response: requests.Response) -> None:
        if not response.ok:
            self.wrong_connection_service(response)
            raise ConnectionError(f'Something went wrong with http connection! {response.status_code}'
                                  f'{response.content}')

        self.additional_checking(response)

    def send_message(self, data: BaseModel) -> Response:
        response = requests.post(url=self.url_address, json=data.dict())
        self.check_response_is_ok(response)
        return response
