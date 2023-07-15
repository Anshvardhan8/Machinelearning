import pandas as pd
from data_description import data_description

class imputation: 

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    tasks  = ["\n1. Show number of Null Value" 
              , "2. Remove Columns" 
              , "3. Fill Null Values with Mean" 
              , "4. Fill Null Values with Median"
              , "5. Fill Null Values with Mode"
              , "6. Show the Dataset"] # List of tasks that can be performed
    
    def __init__(self , data):
        self.data = data

    def showColumns(self , data): # Show all column names with a separator
        print("\nColumns in the dataset are: ")
        for col in data.columns.values:
            print(col , end = " | ")
        return
    
    def printNullValues(self): # Print number of null values in each column
        print("\nNull Values in the dataset are: ")
        for col in self.data.columns.values: # Loop through each column
            print('{0: <20}'.format(col) + '{0: <5}'.format(sum(pd.isnull(self.data[col])))) # Print column name and number of null values along with formatting into 20 and 5 spaces respectively
            print("") # Print a new line
            return
        
    def removeColumns(self): # Remove columns with null values
        self.showColumns(self.data) # Show all column names
        while(1):
            columns = input("\nEnter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to delete (Press -1 to go back)  ").lower()

            if columns == "-1":
                break
            choice = input("Are you sure you want to delete these columns? (Y/N) ")
            if choice == 'Y' or choice == 'y':
                try:
                    self.data.drop(columns.split() , axis = 1 , inplace = True) # Drop the columns
                except KeyError:
                    print("One or more columns do not exist")
                    continue
                print("Columns Deleted")
                break
            elif choice == 'N' or choice == 'n':
                print("Columns not deleted")
                break
        return  
    

    def fillNullValueswithMean(self): # Fill null values with mean , median or mode
        self.showColumns(self.data) # Show all column names
        while(1):
            column = input("\nEnter the column name you want to fill (Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure you want to fill null values in this column? (Y/N) ")
            if choice == 'Y' or choice == 'y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean()) # Fill null values with mean
                except KeyError:
                    print("Column does not exist")
                    continue
                except TypeError:
                    print("Imputation cannot be done on this column")
                    continue
                print("Null Values Filled")
                break
            elif choice == 'N' or choice == 'n':
                print("Null Values not filled")
        
        return
    
    def fillNullValueswithMedian(self): # Fill null values with mean , median or mode
        self.showColumns(self.data) # Show all column names
        while(1):
            column = input("\nEnter the column name you want to fill (Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure you want to fill null values in this column? (Y/N) ")
            if choice == 'Y' or choice == 'y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median()) # Fill null values with median
                except KeyError:
                    print("Column does not exist")
                    continue
                except TypeError:
                    print("Imputation cannot be done on this column")
                    continue
                print("Null Values Filled")
                break
            elif choice == 'N' or choice == 'n':
                print("Null Values not filled")
        return
    
    def fillNullValueswithMode(self): # Fill null values with mean , median or mode
        self.showColumns(self.data) # Show all column names
        while(1):
            column = input("\nEnter the column name you want to fill (Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure you want to fill null values in this column? (Y/N) ")
            if choice == 'Y' or choice == 'y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mode()) # Fill null values with mode
                except KeyError:
                    print("Column does not exist")
                    continue
                except TypeError:
                    print("Imputation cannot be done on this column")
                    continue
                print("Null Values Filled")
                break
            elif choice == 'N' or choice == 'n':
                print("Null Values not filled")
        return
    
    def imputer(self):
        while(1):
            print("Imputation Tasks: ")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\nEnter your choice (Press -1 to go back)  "))
                except ValueError:
                    print("Integer Value Expected")
                    continue
                break

            if choice == -1:
                break

            if choice == 1:
                self.printNullValues()

            elif choice == 2:
                self.removeColumns()

            elif choice == 3:
                self.fillNullValueswithMean()

            elif choice == 4:
                self.fillNullValueswithMedian()

            elif choice == 5:
                self.fillNullValueswithMode()

            else:
                print("Invalid Choice")
        return self.data


        
