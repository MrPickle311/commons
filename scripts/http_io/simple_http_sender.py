from .http_sender import HttpSender
from pydantic import BaseModel
from abc import abstractmethod
import datetime


class SimpleMessage(BaseModel):
    station_id: int


# TODO: aggregate host_address . port , station_id into 1 class
# TODO: change message_type -> message_path

class SimpleHttpSender(HttpSender):
    def __init__(self, host_address: str, port: int, station_id: int, message_type: str):
        HttpSender.__init__(self, host_address, port, message_type, station_id)

    @abstractmethod
    def _create_message(self, *args) -> SimpleMessage: ...

    def send_simple_message(self, *args) -> None:
        data = self._create_message(*args)
        self.send_message(data)
