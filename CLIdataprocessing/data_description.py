import pandas as pd

class data_description:
    tasks = [ # List of tasks that can be performed
        '\n1. Describe a specific Column',
        '2. Show Properties of Each Column',
        '3. Show the Dataset'
    ]

    def __init__(self , data):
        self.data = data # Store the data in the class variable

    def showDataset(self):
        while(1): # Loop until a valid input is entered
            try: 
                rows = int(input("Enter number of rows to display or Press -1 to go back ")) 
                if rows == -1: # If user wants to go back
                    break
                if rows <=0: # If user enters a negative number
                    print("Enter a positive integer")
                    continue
                print(self.data.head(rows)) # Display the dataset
            except ValueError: # If user enters a non-numeric value
                print("Enter a Numeric Value")
                continue
            break
        return
    
    def showColumn(self):
        for col in self.data.columns.values:
            print(col , end = " | ") # Print all column names with a separator

    def describe(self):
        while(1):
            print("\n\nWhat do you want to do?\n")
            for task in self.tasks:
                print(task)

            while(1): # Loop until a valid input is entered
                try:
                    choice = int(input("\nEnter your choice or Press -1 to go back")) # Get user choice

                except ValueError:
                    print("Enter a Numeric Value")
                    continue
                break
            if choice == -1:
                break
            if choice == 1:
                self.showColumn() # Show all column names
                while(1): # Loop until a valid input is entered
                    column = input("\nEnter the column name ") # Get column name from user
                    try:
                        print(self.data[column].describe()) # Describe the column
                    except KeyError: # If column name is invalid
                        print("Invalid Column Name")
                        continue
                    break
            elif choice == 2: # Show properties of each column
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice == 3: # Show the dataset
                self.showDataset()
            else:
                print("Invalid Choice")
                continue
