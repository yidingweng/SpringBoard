"""
1. Manipulating lists for fun and profit
"""

In [1]: # Create a list containing the names: baby_names
        baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

        # Extend baby_names with 'Rowen' and 'Sandeep'
        #baby_names.extend('Rowen')
        #baby_names.extend('Sandeep')
        baby_names.extend(['Rowen','Sandeep'])
        # Print baby_names
        print(baby_names)
        for i in baby_names:
            print(i)

        # Find the position of 'Aliza': position
        position = baby_names.index('Aliza')

        # Remove 'Aliza' from baby_names
        baby_names.pop(position)

        # Print baby_names
        print(baby_names)
['Ximena', 'Aliza', 'Ayden', 'Calvin', 'Rowen', 'Sandeep']
Ximena
Aliza
Ayden
Calvin
Rowen
Sandeep
['Ximena', 'Ayden', 'Calvin', 'Rowen', 'Sandeep']


"""
2. Looping over lists
"""
# Create the empty list: baby_names
baby_names = []

# Loop over records
for row in records:
    # Add the name to the list
    baby_names.append(row[3])

# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)

"""
3.Using and unpacking tuples

Use the zip() function to pair up girl_names and boy_names into a variable called pairs.
Use a for loop to loop through pairs, using enumerate() to keep track of your position. Unpack pairs into the variables idx and pair.
Inside the for loop:
Unpack pair into the variables girl_name and boy_name.
Print the rank, girl name, and boy name, in that order. The rank is contained in idx
"""
# Pair up the boy and girl names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))

Rank 0: GRACE and Noah
Rank 1: GENESIS and Benjamin
Rank 2: Chana and Moshe
Rank 3: SARAH and Mason
Rank 4: TIFFANY and Carter
Rank 5: Ava and Dylan
Rank 6: Serenity and MUHAMMAD
Rank 7: OLIVIA and David
Rank 8: ESTHER and JACOB
Rank 9: CHAYA and JOSIAH
Rank 10: ISABELLA and LUCAS
Rank 11: Rachel and Alexander
Rank 12: SOFIA and DAVID
Rank 13: Sophia and AIDEN
Rank 14: Ashley and Joseph
Rank 15: KAYLA and Ethan
Rank 16: Victoria and Jack
Rank 17: CHANA and JAYDEN
Rank 18: Miriam and ALEXANDER
Rank 19: Claire and JOSEPH
Rank 20: MIRIAM and Josiah
Rank 21: Brielle and TYLER
Rank 22: CHLOE and Muhammad
Rank 23: Anna and Daniel
Rank 24: SERENITY and RYAN
Rank 25: RACHEL and Liam
Rank 26: London and Joshua
Rank 27: Sofia and Sebastian
Rank 28: CAMILA and Samuel
Rank 29: NEVAEH and James
Rank 30: ELLA and JUSTIN
Rank 31: Zoe and ERIC
Rank 32: LEAH and NOAH
Rank 33: SOPHIA and Aiden
Rank 34: AVA and Jayden
Rank 35: Emily and Angel
Rank 36: ASHLEY and JAMES
Rank 37: EMMA and MICHAEL
Rank 38: HAILEY and CHRISTIAN
Rank 39: Camila and MOSHE
Rank 40: FIONA and Jacob
Rank 41: Angela and ISAIAH
Rank 42: Taylor and ANGEL
Rank 43: AALIYAH and SEBASTIAN
Rank 44: Alina and ELIJAH
Rank 45: Samantha and MATTHEW
Rank 46: Sarah and JOSHUA
Rank 47: Mia and Lucas
Rank 48: Valentina and ETHAN
Rank 49: ABIGAIL and JEREMIAH
Rank 50: GABRIELLE and BENJAMIN
Rank 51: EMILY and Jeremiah
Rank 52: Isabella and DANIEL
Rank 53: ANGELA and CHRISTOPHER
Rank 54: Fatoumata and Ryan
Rank 55: MADISON and KEVIN
Rank 56: Leah and MASON
Rank 57: Esther and Michael
Rank 58: Mariam and JASON
Rank 59: Chloe and William
Rank 60: Skylar and ANTHONY
Rank 61: Emma and JACK
Rank 62: MAKAYLA and SAMUEL
Rank 63: Madison and Matthew
Rank 64: TAYLOR and Jason
Rank 65: LONDON and Elijah
Rank 66: Grace and Amir
Rank 67: Aaliyah and Eric

"""
4. Making tuples by accident

Create a variable named normal and set it equal to 'simple'.
Create a variable named error and set it equal 'trailing comma',.
Print the type of the normal and error variables.
"""
In [1]: # Create the normal variable: normal
        normal = 'simple'

        # Create the mistaken variable: error
        error = 'trailing comma',

        # Print the types of the variables
        print(type(normal))
        print(type(error))

<class 'str'>
<class 'tuple'>

"""
5. Finding all the data and the overlapping data between sets

Combine all the names in baby_names_2011 and baby_names_2014 by computing their union. Store the result as all_names.
Print the number of names that occur in all_names. You can use the len() function to compute the number of names in all_names.
Find all the names that occur in both baby_names_2011 and baby_names_2014 by computing their intersection. Store the result as overlapping_names.
Print the number of names that occur in overlapping_names.
"""

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))

<script.py> output:
    1460
    987

"""
6. Determining set differences

Create an empty set called baby_names_2011. You can do this using set().
Use a for loop to iterate over each row in records:
    If the first column of each row in records is '2011', add its fourth column to baby_names_2011. Remember that Python is 0-indexed!
Find the difference between baby_names_2011 and baby_names_2014. Store the result as differences.
Print the differences. This has been done for you, so hit 'Submit Answer' to see the result!
"""

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0]=='2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)
