#!/usr/bin/python3
""" This module imports two functions, save_to_json_file
    and load_from_json_file and use them to add all arguments
    to a python list and then save them to a file
"""
from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

save_file = "add_item.json"
try:
    file_content = load_from_json_file(save_file)
except FileNotFoundError:
    file_content = []

save_to_json_file(file_content + argv[1:], save_file)
