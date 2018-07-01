#!/usr/bin/python
import copy
import pandas as pd

def extract_year(date):
    try:
        if '/' in date:
            date_parts = date.split('/')
            year = date_parts[2]
        elif ' ' in date:
            date_parts = date.split(' ')
            year = date_parts[1]
        else:
            year = date[2:]

        if int(year) > 90:
            year = '19' + year
        else:
            year = '20' + year
    except Exception:
        return None

    return int(year)

def extract_month(date):
    try:
        if '/' in date:
            date_parts = date.split('/')
            month_number = int( date_parts[1] )
            months_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            month = months_names[month_number-1]
        elif ' ' in date:
            date_parts = date.split(' ')
            month = date_parts[0]
        else:
            month = 'n.d.'
    except Exception:
        month = 'n.d'

    return month

def explode_casualties(casualty):

    # new_casualty['name'] = extract_name(casualty['name, gender, age'])
    # new_casualty['sex']  = extract_gender_age(casualty['name, gender, age'])

    # TODO: duplication HERE

    return [casualty]

def extract_name(name_gender_age):
    name = name_gender_age.split('(')
    return name[0].strip()

def extract_gender_age(name_gender_age):
    print('\n')
    print(name_gender_age)
    gender_age = name_gender_age.split('(')
    print gender_age
    if len(gender_age) < 2:
        return 'unknown'
    else:
        gender_age = gender_age[1].replace(')', '')
        print gender_age

    return name_gender_age


if __name__ == '__main__':
    # load datasets
    refugees = pd.read_csv('../data/refugeesAndMigrants.csv')
    #sources_df  = pd.read_csv('../data/sources.csv')

    # loop over records and create a new data structure with formatted data and a record for each casualty.
    # not using standard pandas methods (map, apply, etc.) because some records need to be duplicated
    formatted_extended_data = []
    for casualty in refugees.to_dict(orient='records'):
        #print row

        # add separate columns for month and year
        casualty['found_dead_year']  = extract_year(casualty['found dead'])
        casualty['found_dead_month'] = extract_month(casualty['found dead'])

        # duplicate records so every row is a single death with its own attributes
        casualty_array = explode_casualties(casualty)

        for i, cas in enumerate(casualty_array):

            # this record will finally count as one death
            cas['number'] = 1

            # add clean record to output dataset
            formatted_extended_data.append( cas )



