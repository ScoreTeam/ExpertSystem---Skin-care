# -*- coding: utf-8 -*-
from typing import Union

def process_input(value: Union[int, str]) -> str:
    # Function to process input based on its type
    if isinstance(value, int):
        return "Processing an integer: {}".format(value)
    elif isinstance(value, str):
        return "Processing a string: {}".format(value)
