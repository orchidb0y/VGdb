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
