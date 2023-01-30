import csv
import math

# Specify the file being read
filename = "dataexample.txt"

def stress_amp(data): 
    # Open the file in read mode
    with open(data, "r") as file:
        contents = file.read()

        # Split the contents by newline
        lines = contents.split("\n")

        # Create an emtpy list to store the lists of column values
        columns_list = []

        # Iterate through the lines
        for line in lines:
            values = line.split(",")
            columns_list.append(values)

        # Testing: print the lists to test
        # print(columns_list[1])

        return columns_list
    # Stress amplitude
    S_a = 1

    # Mean stress
    S_m = 2

    # Equivalent fully reversed stress amplitude using Smith-Watson-Topper's 
    # model for mean stress effect

    S_ar = sqrt((S_a + S_m)S_a)