"""
This module provides information on system services employed by a given range of ports.
"""

import socket

def port_services(start_port, end_port):
    """
    Return name of service provided by each port in\
    range [start_port, end_port] (inclusive).
    """
    # Initialize empty dict for (key, value) pairs of (port, service).
    port_service_dict = dict()

    # Loop through port range and add to port_service_dict
    for i in range(int(start_port), int(end_port) + 1):
        try:
            port_service_dict[i] = socket.getservbyport(i)
        except OSError:
            port_service_dict[i] = "     " # Shows that port is not in use

    return port_service_dict

def print_dict(dict_input):
    '''Prints port/service key/value pairs from dict_input'''
    # Header row
    print('PORT : SERVICE')

    # Loop through dict items and print port:service
    for key, value in dict_input.items():
        print(f'{key} : {value}')

