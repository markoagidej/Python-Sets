1. Python Sets Adventure
Objective:
The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

Task 1: Flight Route Comparison
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
2. Set Operations in Data Analysis
Objective:
The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

Task 1: Duplicate Entries Cleanup
You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
Expected Outcome:
A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

3. Music Festival Playlist Organization
Objective:
The aim of this assignment is to develop your skills in using Python loops with sets, particularly for organizing and managing playlists for a music festival. You will work with sets to handle various artists and genres, ensuring no duplicates and maintaining a well-organized collection.

Task 1: Artist Lineup Compilation
You are provided with a list of artist names scheduled to perform at different stages of the music festival. Using a loop, compile these artist names into a set to create a unique lineup without duplicates.

Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
Expected Outcome:
A set containing unique artist names, such as {'The Lumineers', 'Tame Impala', 'Billie Eilish', 'Arctic Monkeys'}.

Task 2: Genre Sorting
You have a list of genres associated with each artist. Using a loop with sets, categorize artists by their genres, creating a set for each genre.

Example Code:

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}
Expected Outcome:
A categorization of artists by genres, such as Genre: Folk, Artists: The Lumineers.

Task 3: Playlist Duplication Check
Create a Python script that takes multiple playlist sets and checks if any playlist is a duplicate of another (i.e., contains the same set of songs).

Example Code:

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]
Expected Outcome:
A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True.