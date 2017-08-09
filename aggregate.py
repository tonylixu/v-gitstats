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
    a main project, ex: ['/static/data/TUT/DataWedge/general.tsv','/static/data/TUT/ardvarc/general.tsv']

    Return:
        dict of data ready for 'Aggregate' page
    """
