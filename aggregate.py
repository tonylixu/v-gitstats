from __future__ import print_function
from __future__ import absolute_import

import csv, os, re, sys

# To prevent csv file that contains huge fields, we proactively set
# the maximum field size.
# sys.maxsize: The largest positive integer supported by the platform.
csv.field_size_limit(sys.maxsize)