#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:45:19 2019

@author: sean
"""
from typing import Dict, List

dict_example= {'key1': 1, 'key2': 2, 'key3' : 3, 'key4': 4}
list_example = [1, 2, 3, 4, 555555 , 678, 9, 0 , 234]
string_example = 'this is a string' 

def long_function(input_dictionary: Dict[str, int], list_of_numbers: List[int], a_text_variable: str, another_variable:int) ->None:
    """This is a function with arguments and documentation that exceeds PEP 8's recommended maximum line length."""
    return None