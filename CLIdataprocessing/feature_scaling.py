import pandas as pd
from data_description import data_description
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class feature_scaling:

    tasks = [
        "\n1. Perform Normalization (Min-Max Scaling)",
        "2. Perform Standardization (Standard Scaling)",
        "3. Show the Dataset",
    ]

    tasks_normalization = [
        "\n1. Normalize a single column",
        "2. Normalize all columns",
        "3. Show the Dataset",
    ]

    tasks_standardization = [
        "\n1. Standardize a single column",
        "2. Standardize all columns",
        "3. Show the Dataset",
    ]

    def __init__(self, data):
        self.data = data
    
    def normalization(self):
        while(1):
            print("Tasks that can be performed are: ")
            for task in self.tasks_normalization:
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

            elif choice == 1:
                print(self.data.dtypes) # Print the data types of all columns
                columns = input("\nEnter the column name you want to normalize (Press -1 to go back)  ").lower()
                if columns == "-1":
                    break
                for column in columns.split():
                    try:
                        minValue = self.data[column].min() # Get the minimum value of the column
                        maxValue = self.data[column].max() # Get the maximum value of the column
                        self.data[column] = (self.data[column] - minValue) / (maxValue - minValue) # Normalize the column
                    except:
                        print("Not Possible")
                print("Column(s) Normalized")

            elif choice == 2:
                try:
                    self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data)) # Normalize all columns by passing the dataframe to the fit_transform() function
                    print("Columns Normalized")

                except:
                    print("Invalid Operation")

            elif choice == 3:
                data_description.showDataset(self)

            else:
                print("Invalid Choice")

            return
        
    def standardization(self):
        while(1):
            print("Tasks that can be performed are: ")
            for task in self.tasks_standardization:
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
            
            elif choice == 1:
                print(self.data.dtypes) # Print the data types of all columns
                columns = input("\nEnter the column name you want to standardize (Press -1 to go back)  ").lower()
                if columns == "-1":
                    break
                for column in columns.split():
                    try:
                        mean = self.data[column].mean() # Get the mean value of the column
                        std = self.data[column].std() # Get the standard deviation of the column
                        self.data[column] = (self.data[column] - mean) / std # Standardize the column
                    except:
                        print("Not Possible")
                print("Column(s) Standardized")

            elif choice == 2:
                try:
                    self.data = pd.DataFrame(StandardScaler().fit_transform(self.data)) # Standardize all columns by passing the dataframe to the fit_transform() function
                    print("Columns Standardized")

                except:
                    print("Invalid Operation")
                break

            elif choice == 3:
                data_description.showDataset(self)

            else:
                print("Invalid Choice")
        return
    
    def featureScaling(self):
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

            elif choice == 1:
                self.normalization()

            elif choice == 2:
                self.standardization()

            elif choice == 3:
                data_description.showDataset(self)

            else:
                print("Invalid Choice")
        return