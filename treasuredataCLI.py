#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import tdclient
import tabulate
import csv
import datetime
import re
import os

#validate Engine
def validate_engine(enginevalue):
    ENGINE = {'HIVE': 1, 'PRESTO': 2}
    if enginevalue.upper() in ENGINE.keys():
        return True
    else:
        return False

#validate timestamp

def validate_timestamp(min, max):
    isValid = False
    if (re.match(r"[0-9]{10}", min) or min.upper() == 'NULL') \
        and (re.match(r"[0-9]{10}", max) or max.upper() == 'NULL'):

        isValid = True

        if min.isdigit() and max.isdigit():
            if min < max:
                isValid = True
            else:
                isValid = False

    return isValid

#validate limit
def validate_limit(limitvalue):
    return str(limitvalue).isdigit()

#validate format
def validate_format(formatvalue):
    FORMAT = {'TABULAR': 1, 'CSV': 2}
    if formatvalue.upper() in FORMAT.keys():
        return True
    else:
        return False

#validate columns
def validate_column(columns):
    if re.match(r"(\*|^\'(\w+)\'$|^\'(\w+)(\,\w+)*(\,\w+\'$))",
                columns):
        return True
    else:
        return False

#validate dbname
def validate_db(dbname):
    if re.match(r"(\*|\0|[0-9]|\s)", dbname):
        return False
    else:
        return True

#validate tablename
def validate_tbl(tablename):
    if re.match(r"(\*|\0|\s)", tablename):
        return False
    else:
        return True



@click.command()

@click.argument('query', nargs=1)

@click.option(
    '-f',
    '--format',
    'format',
    default='tabular',
    help='Currently supports csv and tabular format and defaults to tabular'
        ,
    type=str,
    )
@click.option(
    '-e',
    '--engine',
    'engine',
    default='hive',
    help='Currently supports Presto and Hive and defaults to Hive',
    type=str,
    )
@click.option(
    '-c',
    '--columns',
    'columns',
    default='*',
    help='Enter the column names with comma seperator',
    type=str,
    )
@click.option(
    '-m',
    '--min',
    'min_time',
    default='NULL',
    help='Minimum time stamp  to filter data from (unix timestamp format)'
        ,
    type=str,
    )
@click.option(
    '-M',
    '--MAX',
    'max_time',
    default='NULL',
    help='Maximum time stamp to filter data( unix time stamp format)',
    type=str,
    )
@click.option(
    '-l',
    '--limit',
    'limit',
    default='100',
    help='Used to limit the number of rows and defaults to 100',
    type=str,
    )
@click.argument('db', nargs=1)
@click.argument('table', nargs=1)
def executequery(
    query,
    format,
    engine,
    columns,
    min_time,
    max_time,
    limit,
    db,
    table,
    ):

    API_KEY='9552/902f8ac1761c8d38e625ae9544868a1dcda516f0'
    check_format = validate_format(format)
    check_engine = validate_engine(engine)
    check_limit = validate_limit(limit)
    check_columns = validate_column(columns)
    check_database = validate_db(db)
    check_db_tbl = validate_tbl(table)
    check_timestamp = validate_timestamp(min_time, max_time)

    if query.upper()!='QUERY':
          click.echo(click.style("start the command with the term 'Query' ",fg='red',bold=True) )
          return -1


    if check_format is False:

        click.echo(click.style('Check the file format.supports csv or tabular format'
                   , fg='red', bold=True))
        return -1

    if check_limit is False:
        click.echo(click.style('Check the limit value. Only numeric value is allowed and defaults to 100'
                   , fg='red', bold=True))
        return -1

    if check_engine is False:
        click.echo(click.style('Supports Hive and Presto engine',
                   fg='red', bold=True))
        return -1

    if check_columns is False:
        click.echo(click.style("Enter columns in following pattern 'column_a,column_b,column_c'"
                   , fg='red', bold=True))
        return -1
    else:

        columns = columns.strip("'")

    if check_database is False:
        click.echo(click.style('Enter the valid database name', fg='red'
                   , bold=True))
        return -1

    if check_db_tbl is False:

        click.echo(click.style('Enter the valid table name', fg='red',
                   bold=True))

        return -1

    if check_timestamp is False:

        # print("Enter the valid  time stamp and  time range in unix time format ")

        click.echo(click.style('Enter the valid  time stamp and  time range in unix time format'
                   , fg='red', bold=True))

        return -1

    try:
        client = tdclient.Client(API_KEY)
        query = \
            'SELECT  %s FROM %s WHERE TD_TIME_RANGE(time, %s, %s) LIMIT %s' \
            % (columns, table, min_time, max_time, limit)

        job = client.query(db, q=query, type=engine)
        job.wait()
        if format == 'csv':
            csvfile = csv.writer(open('treasure_data_query_%s.csv'
                                 % str(datetime.datetime.now()), 'w'))
            for row in job.result():
                csvfile.writerow(row)

            click.echo(click.style('csv file generated', fg='green',
                       bold=True))
        else:
             #Generate the Tabular Form
            click.echo(click.style(tabulate.tabulate(job.result(),
                       tablefmt='fancy_grid'), fg='green'))
    except:

        click.echo(click.style('Error occured in executing query',
                   fg='red', bold=True))
        return -1

if __name__ == '__main__':
    executequery()
