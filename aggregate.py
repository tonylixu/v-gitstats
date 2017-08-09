from __future__ import print_function
from __future__ import absolute_import

import csv, os, re, sys

# To prevent csv file that contains huge fields, we proactively set
# the maximum field size.
# sys.maxsize: The largest positive integer supported by the platform.
csv.field_size_limit(sys.maxsize)

def generateAggregate(arrToTSV):
    """Generate and returns JSON data for the 'Aggregate' page for a
    given project.

    Arguments:
        arrToTSV { [str] }: relative paths to the 'general.tsv' for each sub-project under
    a main project,
    ex: ['/static/data/TUT/DataWedge/general.tsv','/static/data/TUT/ardvarc/general.tsv']

    Return:
        dict of data ready for 'Aggregate' page
    """

    def processName(projData, master):
        """Processes the names of a subproject and writes it to master

        Arguments:
            projData {dict}: Contains this project's name string
            master {dict}: the master data container

        Return:
            The master dict
        """
        print("PROCESSING {0}".format(projData['data']))
        proj_name = projData['data']
        master['projects'].append(proj_name)
        return master

    # Defaults, this json gets passed to each function
    master = {
        "projects": [],
        "report_period": {"youngest":0, "oldest": 0},
        "age": {"total_days": 0, "active_days": 0, "percent_active": 0},
        "total_files": 0,
        "loc": {"total": 0, "added" : 0, "removed": 0},
        "commits" : {"commits": 0, "avg_commits_active": 0, "avg_commits_all": 0},
        "authors": {"total": 0, "avg_commits_author": 0},
    }

    for tsv in arrToTSV:
        print("PROCESSING A TSV: {0}".format(tsv))
        with open(tsv, 'r') as tsvFile:
            print("RUNNING FILE {0}".format(tsv))
            tsvIn = csv.reader(tsvFile, delimiter='\t')
            # We skip the headers
            tsvIn.next()
            keeper = []
            for row in tsvIn:
                keeper.append({
                    "header": row[0],
                    "data": row[1]
                })

            master = processName(keeper[0], master)

    return master