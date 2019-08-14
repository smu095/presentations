#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:12:27 2019

@author: sean
"""

def hello(text: str, caps: bool) -> str:
    """ Returns text in all caps if caps = True, else returns text capitalised."""
    if caps:
        return text.upper()
    else:
        return text.capitalize()

print(hello("Hello my friend!", caps=True))
print(hello("Hello my friend!", caps="True"))