# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def find_similar_destinations():
    print("These are the destinations both airlines go to:")
    print(our_routes.intersection(competitor_routes))


def find_our_unique():
    print("These are the destinations unique to out airline:")
    print(our_routes.difference(competitor_routes))


def find_all_unique():
    print("These are the destinations unique to each airline:")
    print(our_routes.symmetric_difference(competitor_routes))

find_similar_destinations()
find_our_unique()
find_all_unique()