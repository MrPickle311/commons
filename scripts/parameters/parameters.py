from hashlib import new
import imp
from typing import Dict
from enums.params import Params

import rospy
import os

import yaml


class ParametersConfigurator:

    def __init__(self, params_file_destination) -> None:
        self.params_file_destination = params_file_destination
        self.update_params()

    def get_dynamic_params_from_file(self) -> Dict[str, any]:
        dict = {}
        with open(self.params_file_destination, "r") as params_file:
            try:
                dict = yaml.safe_load(params_file)
            except yaml.YAMLError as exc:
                print('Cannot open parameters file!!')
        return dict

    def update_params(self) -> None:
        for param_name, param_value in self.get_dynamic_params_from_file().items():
            rospy.set_param(param_name=param_name, param_value=param_value)

    def save_params_to_file(self, new_params: Dict[str, any]) -> None:
        with open(self.params_file_destination, 'w') as params_file:
            yaml.dump(new_params, params_file)

    def apply_new_params(self, new_params: Dict[str, any]):
        self.save_params_to_file(new_params)
        self.update_params()
