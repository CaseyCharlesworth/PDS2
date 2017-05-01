from settings import *
import pandas as pd


class DocumentCollection:
    document_map = {}

    def __init__(self):
        pass

    def populate_map(self):
        """
        Populate a document map to store the collection of data for referencing
        :return: Populated collection hash table
        """
        # Declare constants for CSV parsing
        header =["id", "author", "date", "content", "class"]

        # Read data into document map
        for filename in os.listdir(DATA_ROOT):
            # Ensure the file is a CSV file
            if filename.endswith(".csv"):
                # Create path and key for hash table
                file_path = DATA_ROOT+"/"+filename
                file_key = os.path.splitext(filename)[0]
                self.document_map[file_key] = pd.read_csv(file_path, sep=',', names=header)

    def print_collection(self):
        """
        Pretty print the collection of data
        :return: Pretty print to stdout
        """
        for key, value in self.document_map.iteritems():
            print value.to_string()