''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''
import random
import itertools

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of cities with random x and y coordinates.
    """

    #Fail saves
    #If given 0 or negative # of cities, return empty list
    if n_cities <= 0: 
        return []

    #If given 0 or negative size for map, return empty list
    if size[0] <= 0:
        if size[1] <= 0:
            return []

    #Create empty city list
    citylist = []

    #Coordinate of individual city in pair (x,y)
    citycoord = (0,0)

    #Constructing city list
    i = 1
    while i <= n_cities:
        #Generate random coord within map size for city
        #Consider the condition where x size and y size are different
        citycoord = (random.randint(0,size[0]-1), random.randint(0,size[1]-1))

        #Add city to list after coord is set
        citylist.append(citycoord)

        #Next iteration
        i=i+1

    #Return completed city list
    return citylist

    pass

def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of city names
    :return: A list of tuples representing all possible links between cities/ pairs of cities, 
            each item in the list (a link) represents a route between two cities.
    """

    #Create empty route list
    routelist = []

    #Generate all posible connections between city names using itertools.combinations, store all posibilities to route list
    routelist = itertools.combinations(city_names,2)

    #Return completed route list
    return routelist

    pass


# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    cities = get_randomly_spread_cities((100, 200), len(city_names))
    routes = get_routes(city_names)
    print('Cities:')
    for i, city in enumerate(cities):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')
