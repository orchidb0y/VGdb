# VGdb
Videogame database and recommendation software

## Purpose
This program was developed by me as the final project for CS102.
The assignment was to create a search program that would use a simple database to return results
based on the user's intentions, with at least:
* A search algorithm that would match a string to a pattern
* Data structures taught in the 102 module, such as Linked Lists and Hash Maps.

## Instructions
The program runs on `main.py`, and using it is very simple.

1. Search by name:
Enter a string at least three characters long. The program will return a list of games with names that match that search string.

2. Search by rating:
Enter a number between 1 and 100 (inclusive). The program will return a list of at most 10 games with ratings that match that rating or more.

3. Search by release year:
Enter a year between 1980 and 2022 (inclusive). The program will return a list of at most 10 games that were released that year or later.

4. Search by genre:
Choose a genre from the list that will be provided and enter it (not case sensitive). The program will return a list of at most 10 games that match the chosen genre.

5. Search by platform:
Choose a platform from the list that will be provided and enter it (not case sensitive). The program will return a list of at most 10 games that run on the chosen platform.

## Search results completeness
The database of games used by the program is hundreds of games long. This means that restricting the search results to 10 games could prevent the program from showing new games to the user should they repeat the search with the same parameters.

In order to go around that problem, the program will shuffle the list of results and pick the 10 first games, so that every search returns a different result.

## Workings of each file

### datemap.py
Datemap is a class that builds an array of linked lists. Each index in the array references a year from 1980 to 2022, so that Index 0 = 1980, and Index 44 = 2022. As the search by release year is called, games from the database are dumped to a Datemap object. Games relased in the same year share an array index by being stored in a linked list.

Upon receiving a desired year, Datemap will fetch all games from the year's linked list and return it to main.py as a list. If the list is 10 or more games long, the search is over. If not, it will search the next year and so on, until the search has fetched a total of 10 games.

### findname.py
Findname.py contaisn a search function that looks to match a search pattern of strings to the names of the games in the database. It is coded in a way that it can look for a match in any part of the name of the game. Entering "god" will return "God of War" games (and any other game containing "god"); entering "last" will return "The Last of Us" games (same as before), etc.

The function is fed with the search pattern string and a list of games' names built by main.py before calling findname(). It then returns the list of games' names that matched the search pattern.

### games.py
This module builds the list of dictionaries used by the program and it's classes and functions: the games list of dicts. It parses through the games.csv database, processes each row into a dictionary and each value in order to make them readable by main.py and the other modules.

### hashmap.py
This contains a regular hash map class. It stores the games from the database using their names as keys and the dictionary's listed values as values. It is built when calling the search by name option, and then used with findname()'s list of matches.

### ratingmap.py
It contains a class very much like datemap.py, which the only difference being that it stores games in an array with 100 indexes which represent a metacritic score (1 to 100), which each array index containing a linked list that stores games with the same rating.

### linkedlist.py
A module containing a node class and a linked list class. It only contains the necessary methods to build the list and then traverse through it. It is used by datemap.py and ratingmap.py as well as by the search by genre and search by platform methods over at main.py