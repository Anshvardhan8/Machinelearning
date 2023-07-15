from data_description import data_description
from datainput import datainput
from imputation import imputation
from download import download
from categorical import categorical
from feature_scaling import feature_scaling

class Preprocessor:

    tasks = [
        "1. Data Description",
        "2. Handling Missing Values",
        "3. Encoding Categorical Data",
        "4. Feature Scaling",
        "5. Download Dataset",

    ]

    data = 0

    def __init__(self):
        self.data = datainput().input_function()
        print("\n\n Welcome to Preprocessor")

    def removeColumns(self):
        print("\nColumns in the dataset are: ")
        for col in self.data.columns.values:
            print(col)
        
        while(1):
            column = input("\nEnter the column name you want to remove (Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure you want to remove this column? (Y/N)  ")
            if choice == 'Y' or choice == 'y':
                try:
                    self.data.drop(column , axis = 1 , inplace = True)
                except KeyError:
                    print("Column does not exist")
                    continue
                print("Column Removed")
                break
            elif choice == 'N' or choice == 'n':
                print("Column not removed")
                break
        return
    
    def printdata(self):
        print(self.data)
        return
    
    def preprocessormain(self):
        self.removeColumns()
        while(1):
            print("\n\nWhat do you want to do?")
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
                exit()

            if choice == 1:
                data_description(self.data).describe()

            elif choice == 2:
                self.data = imputation(self.data).imputer()

            elif choice == 3:
                self.data = categorical(self.data).categoricalmain()
            
            elif choice == 4:
                self.data = feature_scaling(self.data).featureScaling()
            
            elif choice == 5:
                download(self.data).download()

            else:
                print("Invalid Choice")
                continue
obj = Preprocessor()
obj.preprocessormain()