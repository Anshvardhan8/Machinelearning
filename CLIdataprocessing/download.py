import pandas as pd

class download:

    def __init__(self, data):
        self.data = data
    
    def download(self):
        tobedownload = {}

        for column in self.data.columns.values: # Loop through each column
            tobedownload[column] = self.data[column] # Add the column to the dictionary

        newfilename = input("Enter the new filename (Press -1 to go back)  ")
        if newfilename == "-1":
            return
        
        newfilename = newfilename + ".csv"
        pd.DataFrame(self.data).to_csv(newfilename, index = False) # Convert the dictionary to a dataframe and save it as a csv file

        print("File Downloaded")

        if input("Do you want to exit? (Y/N)  ").lower() == 'y':
            print("Thank you for using our service")
            exit(0)
        else:
            return