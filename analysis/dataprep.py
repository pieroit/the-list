#!/usr/bin/python

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


if __name__ == '__main__':
    # load datasets
    refugees = pd.read_csv('../data/refugeesAndMigrants.csv')
    #sources_df  = pd.read_csv('../data/sources.csv')

    # loop over records
    for row in refugees.to_dict(orient='records'):
        print row

        # add separate columns for month and year
        row['found_dead_year']  = extract_year( row['found dead'] )
        row['found_dead_month'] = extract_month( row['found dead'] )

        # duplicate records so every row is a single death
        # TODO: here

        # add separate columns for
        #row['name'] = extract_name['name, gender, age']
        #row['name'] = extract_gender['name, gender, age']
        #row['name'] = extract_age['name, gender, age']

    print(refugees.head())