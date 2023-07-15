import pandas as pd
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from data_description import data_description

class categorical:

    tasks = ['\n1. Show Categorical Columns',
             '2. Perform One Hot Encoding',
             '3. Show the Dataset',]
    
    def __init__(self , data):
        self.data = data

    def categoricalColumn(self):
        print('\n{0: <20}'.format("Categorical Column") + '{0: <5}'.format("Unique Values")) # Print column name and number of null values along with formatting into 20 and 5 spaces respectively

        for col in self.data.columns.values(include = 'object'): # Loop through each column which has categorical values only
            print('{0: <20}'.format(col) + '{0: <5}'.format(self.data[col].nunique())) # Print column name and number of null values along with formatting into 20 and 5 spaces respectively

    def encoding(self):
        categoricalColumn  = self.data.select_dtypes(include = 'object').columns.values  # Select all columns with categorical values only
        while (1):
            column = input("\nEnter the column name you want to encode (Press -1 to go back)  ").lower()
            if column == "-1":
                break
            if column  in categoricalColumn:
                self.data = pd.get_dummies(self.data , columns = [column]) # Perform one hot encoding by passing the column name in the columns parameter
                print("Column Encoded")

                choice = input("Do you want to encode more columns? (Y/N) ")
                if choice == 'Y' or choice == 'y':
                    continue
                elif choice == 'N' or choice == 'n':
                    self.categoricalColumn()
                    break
            else:
                print("Column does not exist")
                continue
        
    def categoricalmain(self):
        while(1):
            print("Tasks that can be performed are: ")
            for task in self.tasks:
                print(task)
            
            while(1):
                try:
                    choice = int(input("\nEnter your choice (Press -1 to go back)  "))
                except ValueError:
                    print("Integer value expected")
                    continue
                break

            if choice == -1:
                break

            if choice == 1:
                self.categoricalColumn()

            elif choice == 2:
                self.categoricalColumn()
                self.encoding()

            elif choice == 3:
                data_description.showDataset(self)

            else:
                print("Invalid Choice")
                continue
        return self.data                  


        
