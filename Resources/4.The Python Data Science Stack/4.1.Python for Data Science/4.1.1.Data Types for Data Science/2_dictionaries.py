"""
1.Creating and looping through dictionaries
"""

# Create an empty dictionary: names
names = {}

# Loop over the girl names
for name,rank in female_baby_names_2012:
    ## got mistake, in the following line of updating a dictionary
    # Add each name to the names dictionary using rank as the key
    names[rank]=name

print(names)
# Sort the names list by rank in descending order and slice the first 10 items
for rank in sorted(names,reverse = True)[:10]:
    # Print each item
    print(names[rank])


"""
2.Safely finding by key
"""
# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
### No idea how to get it

print(names.get(105, 'Not Found'))

"""
3.Dealing with nested data
"""

# Print a list of keys from the boy_names dictionary
#for eachkey in boy_names.keys():
    #print(eachkey)
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
###the following line took forever

print(boy_names[2013].keys())
# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))

"""
4.Adding and extending dictionaries
"""
# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
'''
## did not figure out, get stucked because of using {} instead of []
'''
boy_names[2012].update([(1,'Casey'), (2,'Aiden')])

# Loop over the boy_names dictionary
## not sure I can do or not.

for year in boy_names:
    # Loop over and sort the data for each year by descending rank
    for rank in sorted(boy_names[year], reverse=True)[:1]:
        # Check that you have a rank
        if not rank:
            print(year, 'No Data Available')
        # Safely print the year and the least popular name or 'Not Available'
        print(year, boy_names[year].get(rank, 'Not Available'))

"""
5.Popping and deleting from dictionaries
"""
# Remove 2011 and store it: female_names_2011

female_names_2011 = female_names.pop(2011)

# Safely remove 2015 with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015,{})

# Delete 2012
del female_names[2012]

# Print female_names
print(female_names)

"""
6.Working with dictionaries more pythonically
"""
# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)

# Iterate over the 2012 nested dictionary
for rank, name in baby_names[2012].items():
    # Print rank and name
    print(rank, name)

"""
7.Checking dictionaries for data
"""
# Check to see if 2011 is in baby_names
if '2011' in baby_names.values():
    # Print 'Found 2011'
    print('Found 2011')

# Check to see if rank 1 is in 2012
'''
### cannot put '1'
'''
if 1 in baby_names[2012]:
    # Print 'Found Rank 1 in 2012' if found
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')

# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
   # Print 'Found Rank 5'
   print('Found Rank 5')

"""
8. Reading from a file using CSV reader
"""

# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('baby_names.csv','r')

# Loop over a csv reader on the file object
'''
###csv.reader very crucial
'''
for row in csv.reader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]

# Print the dictionary keys
print(baby_names.keys())

"""
9.Creating a dictionary from a file
"""

# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv','r')

# Loop over a DictReader on the file
'''
### hard to remember
'''
for row in csv.DictReader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary: baby_names
    # Add the rank and name to the dictionary
    ### did not figure out the following step(when it is a dictionaary)
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary
print(baby_names.keys())
