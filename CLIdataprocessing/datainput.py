from os import path
import sys
import pandas as pd

class datainput:

    file_extensions = ['.csv'] # Add more file extensions here

    def change_to_lower_case(self , data): # Change all column names to lower case so that they can be accessed easily
        for col in data.columns.values:
            data.rename(columns={col:col.lower()}, inplace=True)
        return data
    
    def input_function(self):
        try:
            filename , file_extension = path.splitext(sys.argv[1]) # Get file name and extension from command line arguments
            if file_extension == "": # If no file extension is provided
                raise SystemExit("No file extension provided")
            
            if file_extension not in self.file_extensions: # If file extension is not supported
                raise SystemExit("Invalid file extension")
            
        except IndexError: # If no file name is provided
            raise SystemExit("No file name provided")

        try:
            data = pd.read_csv(filename + file_extension) # Read the file

        except pd.errors.EmptyDataError: # If file is empty
            raise SystemExit("File is empty")

        except FileNotFoundError: # If file is not found in the directory
            raise SystemExit("File not found")

        data = self.change_to_lower_case(data) # Change all column names to lower case so that they can be accessed easily

        return data   