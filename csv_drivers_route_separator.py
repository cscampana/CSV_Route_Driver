"""
Created by @ccampana_

This code has the objective of gathering two CSV containing information about zipcodes and drivers assigned to them
and a list of clients with: name, address, zip code, and phone number. The program sorts and outputs into different
text files each route, such that drivers are separated and can follow it.

Version: 0.1 

"""

import csv
from datetime import date
import sys


def csv_to_list(file, type_of_data):
    """
    This method parses a CSV into a list so that the program can read it and use its algorithm to sort it.
    :param file: It is the file to be read from the system.
    :param type_of_data: Defines whether it is a route file or a client list file. Accepts two parameters 'DRIVER'
                         or 'CLIENT'
    :return: dictonary_clean_data
    :rtype: dict
    """
    data_csv_reader = csv.DictReader(open(file, encoding='utf-8', newline=''))
    list_data = []
    for row in data_csv_reader:
        list_data.append(row)

    dictonary_clean_data = []
    if type_of_data.upper() == 'CLIENT':
        for row in list_data:
            name = row['\ufeffName']
            zip_code = row['Postcode (Shipping)']
            address = row['Address 1 (Shipping)']
            phone = row['Phone (Billing)']
            dictonary_clean_data.append({'Name': name, 'Zip Code': zip_code, 'Address': address, 'Phone': phone})
    elif type_of_data.upper() == 'ROUTE':
        for row in list_data:
            name = row['\ufeffName']
            zip_code = row['Zipcodes']
            dictonary_clean_data.append({'Name': name, 'Zip Code': zip_code})

    return dictonary_clean_data


def write_to_file(name, zip_code, address, phone, route_name):
    """
    This method writes to the file the result of the sorting, in such way that it helps the readability of the text
    output
    Parameters: name, zip_code, address, phone, driver_name.
    :param name: The name of the client.
    :param zip_code: The name of the client.
    :param address: The address of the client.
    :param phone: The phone of the client.
    :param route_name: The name of the route assigned to that client. It serves to name the file and be easily sortable.
    :type name: string
    :type zip_code: string
    :type address: string
    :type phone: string
    :type route_name: string
    :return: void

    note:: This method is made to only output the information of the route, the header was split in order to make the
           code more modular.
    """
    file_object = open(route_name + ".txt", "a+")
    file_object.write(
        '{} - {} - {} - {}\n'.format(name, zip_code, address,
                                     phone))


def file_header(route_name):
    """
    This is a method that creates the file header for each text file.

    :param route_name: The name of the route assigned to that client.
    :return: void
    """
    file_object = open(route_name + ".txt", "a+")
    file_object.write('--------{} - Route: {}-------- \n\n'.format(date.today(), route_name))


def main():
    """
    The main method, it defines all the logic of the program.
    """
    print("-------------------------Drivers Route Separator---------------------")
    print("-------------------------Created by ccampana-------------------------")

    if len(sys.argv) < 3:
        print('Not enough arguments, use the format client_data.csv route_data.csv')
        sys.exit(0)
    else:
        client_data = csv_to_list(sys.argv[1], 'client')
        route_data = csv_to_list(sys.argv[2], 'route')

    for route in range(0, len(route_data)):
        # As the CSV has a multiplicity of values for the route name, we have to separate each route, therefore this if
        # checks for those edge cases.
        if route_data[route]['Name'] != route_data[route - 1]['Name']:
            file_header(route_data[route]['Name'])

        for client in range(0, len(client_data)):
            if route_data[route]['Zip Code'] == client_data[client]['Zip Code']:
                write_to_file(client_data[client]['Name'], client_data[client]['Zip Code'], client_data[client]['Address'],
                              client_data[client]['Phone'], route_data[route]['Name'])


if __name__ == "__main__":
    main()
