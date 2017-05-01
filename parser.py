"""
s3436993     Max Yendall
s3132392     Casey-Ann Charlesworth

Assignment 2 - Practical Data Science
Assignment due 18 May 2017
"""

import csv
import sklearn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from include.DocumentCollection import *


def parse_data_collection():
    collection = DocumentCollection()
    collection.populate_map()
    collection.print_collection()

if __name__ == "__main__": parse_data_collection()
