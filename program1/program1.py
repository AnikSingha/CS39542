
"""
    Name: Anik Singha
    Email: anik.singha68@myhunter.cuny.edu
    Resources:
"""

def make_dictionary(data, kind = "min"):
    """
    Creating a dictionary with a key of the remote unit ID + turnstile unit number.
    Depending on kind, the resulting dictionary will store the minimum entry
    number seen (as an integer), the maximum entry number seen (as an integer),
    or the station name (as a string).
    Returns the resulting dictionary.

    Keyword arguments:
    kind -- kind of dictionary to be created:  min, max, station
    """
    new_dict = {}
    for i in data:
        line = i.split(',')
        key = line[1] + "," + line[2]
        if kind == "min":
            value = int(line[9])
        elif kind == "max":
            value = int(line[9])
        elif kind == "station":
            value = line[3]
        new_dict[key] = value

    return new_dict

def get_turnstiles(station_dict, stations = None):
    """
    If stations is None, returns the names of all the turnstiles stored as keys
    in the inputted dictionary.
    If non-null, returns the keys which have value from station in the inputed dictionary.
    Returns a list.

    Keyword arguments:
    stations -- None or list of station names.
    """
    if stations is None:
        return list(station_dict.keys())
    return [i for i in station_dict if station_dict[i] in stations]

def compute_ridership(min_dict,max_dict,turnstiles = None):
    """
    Takes as input two dictionaries and a list, possibly empty, of turnstiles.
    If no value is passed for turnstile, the default value of None is used
    (that is, the total ridership for every station in the dictionaries).
    Returns the ridership (the difference between the minimum and maximum values)
    across all turnstiles specified.

    Keyword arguments:
    turnstiles -- None or list of turnstile names.
    """

    if turnstiles is None:
        return max([max_dict[i] - min_dict[i] for i in min_dict])
    return max([max_dict[i] - min_dict[i] for i in min_dict if i in turnstiles])

def main():
    """
    Opens a data file and computes ridership, using functions above.
    """
    file_name = 'turnstile_220611.txt'
    #Store the file contents in data:
    with open(file_name,encoding='UTF-8') as file_d:
        lines = file_d.readlines()
    #Discard first line with headers:
    data = lines[1:]

    #Set up the three dictionaries:
    min_dict = make_dictionary(data, kind = "min")
    max_dict = make_dictionary(data, kind = "max")
    station_dict = make_dictionary(data, kind = "station")

    #Print out the station names, alphabetically, without duplicates:
    print(f'All stations: {sorted(list(set(station_dict.values())))}')

    #All the turnstiles from the data:
    print(f'All turnstiles: {get_turnstiles(station_dict)}')
    #Only those for Hunter & Roosevelt Island stations:
    print(get_turnstiles(station_dict, stations = ['68ST-HUNTER CO','ROOSEVELT ISLND']))

    #Checking the ridership for a single turnstile
    ridership = compute_ridership(min_dict,max_dict,turnstiles=["R051,02-00-00"])
    print(f'Ridership for turnstile, R051,02-00-00:  {ridership}.')

    #Checking the ridership for a station
    hunter_turns = get_turnstiles(station_dict, stations = ['68ST-HUNTER CO'])
    ridership = compute_ridership(min_dict,max_dict,turnstiles=hunter_turns)
    print(f'Ridership for Hunter College: {ridership}.')

if __name__ == "__main__":
    main()
