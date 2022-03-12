from abc import ABC, abstractmethod
from typing import Dict

from flask import Flask, Request, Response


class HttpPathHandler(ABC):

    @abstractmethod
    def process_request(self, incoming_request: Request):
        pass


class ServerAPI(Flask, ABC):

    def __init__(self, server_name: str, port: int, host_name: str, base_prefix: str):
        Flask.__init__(self, server_name)
        self._server_name = server_name
        self._port = port
        self._host = host_name
        self._http_path_handlers: Dict[str, HttpPathHandler] = {}
        self._base_prefix = base_prefix

        self.endpoints_creation()

    def _route_handler(self, incoming_request: Request):
        try:
            return self._http_path_handlers[incoming_request.path].process_request(incoming_request)
        except KeyError:
            return Response(f"Path '{incoming_request.path}' not found", status=404)
        except Exception as exc:
            return Response(f"Internal {self._server_name} server error : {exc}", status=401)

    @abstractmethod
    def endpoints_creation(self):
        ...

    def run_server(self):
        self.run(port=self._port, host=self._host)
        print('Server Finished!')

    def add_api_path_handler(self, path: str, handler: HttpPathHandler):
        self._http_path_handlers[f'{self._base_prefix}' + path] = handler
