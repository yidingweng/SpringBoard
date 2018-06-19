"""
1.Using Counter on lists
"""
# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)

"""
2.Finding most common elements
"""
# Import the Counter object
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))

"""
3.Creating dictionaries of an unknown structure
"""
# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))

# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])

"""
4.Safely appending to a key's value list
"""
# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)

# Print the first 10 items of the ridership dictionary
'''
### hard to figure out
'''
print(list(ridership.items())[:10])

"""
5.Working with OrderedDictionaries
"""
# Import OrderedDict from collections
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if not date in ridership_date:
        ridership_date[date] = 0

    # Add riders to the date key in ridership_date
    ridership_date[date] += riders

# Print the first 31 records
print(list(ridership_date.items())[:31])

"""
6.
"""
# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())

'''
7. Creating namedtuples for storing data
### Very challenging part
'''
# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries = DateDetails(date,stop,riders)
    entries.append(labeled_entries)

# Print the first 5 items in labeled_entries
print(labeled_entries[:5])
