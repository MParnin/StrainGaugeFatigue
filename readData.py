import csv

# Specify the file being read
filename = "dataexample.txt"

# Open the file in read mode
with open(filename, "r") as file:
    contents = file.read()

# Split the contents by newline
lines = contents.split("\n")

# Create an emtpy list to store the lists of column values
columns_list = []

# Iterate through the lines
for line in lines:
    values = line.split(",")
    columns_list.append(values)

# Print the lists to test
print(columns_list[1])