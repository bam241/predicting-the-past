import csv
import sqlite3 as sql


def import_csv(in_csv, delimit):
    """ Imports contents of a comma delimited csv file
    to a 2D list.
    Parameters
    ---------
    in_csv: str
        csv file name.
    delimit: str
        delimiter of the csv file
    Returns
    -------
    data_list: list
        list with fleetcomp data.
    """
    with open(in_csv, encoding='utf-8') as source:
        sourcereader = csv.reader(source, delimiter=delimit)
        data_list = []
        for row in sourcereader:
            data_list.append(row)

    return data_list


def get_cursor(file_name):
    """ Connects and returns a cursor to an sqlite output file

    Parameters
    ----------
    file_name: str
        name of the sqlite file

    Returns
    -------
    sqlite cursor3
    """
    con = lite.connect(file_name)
    con.row_factory = lite.Row
    return con.cursor()


def 