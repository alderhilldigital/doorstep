"""Boundary checking (improved)

This function will (hopefully!) find if data in a csv file is contained within Northern Ireland.
If not so, this will be reported back to the user.
For now, please make sure that the second geojson in the argument is a boundary of Northern Ireland.

"""

from geojson_utils import point_in_multipolygon
import logging
import json
import pandas as p
import csv



def find_ni_data(first_file, ni_data):
    report = {}

    # If csv file has these attributes then...
    if ['Latitude', 'Longitude'] in p.read_csv(first_file):

        # TODO: could put a check here if file is csv or geojson... need to do this later.

        # Feed csv file into convert_csv_json in order to convert it into json...
        convert_csv_json(first_file)

        # This var becomes the converted json file that we want to compare to the NI data.
        data_to_compare =  p.read_json(first_file)

        # This is the second geojson file that should be NI boundaries. This is what we are comparing the first csv/json file to.
        ni_compare_data = p.read_json(ni_data)

        # This var contains the output of the function point_in_multipolygon. This should contain a bool.
        check=point_in_multipolygon(data_to_compare, ni_compare_data)

        # If the points in the csv data match/are contained in the NI data json, do this...
        if check = True :
            # Reports back to the user that data is in NI
            report['location_found'] = ('Location is in Northern Ireland', logging.INFO)
        # If data in the first csv file are not contained in the second NI geojson file do this...
        elif check = False :
            # Report dict warns user that location is not in NI
            report['location_not_found'] = ('Location NOT in Northern Ireland', logging.WARNING)
        # Default message in case something goes horribly wrong with first CSV file. Should not be called.
        else:
            report['invalid'] = ('Default error message', logging.WARNING)
    # If the csv file does not have any location data....
    else:
        report['no_loc_data_found'] = ('No location data found! Please make sure that you have read the right file', logging.WARNING)


"""Below function should convert csv files to json files in order for use for above function
 Taken from : https://stackoverflow.com/questions/46091769/convert-csv-to-json-using-python"""
def convert_csv_json(file):
    data = []
    with open(file) as f:
        for row in csv.DictReader(f):
            data.append(row)

    json_data = json.dumps(data)
    return json_data
