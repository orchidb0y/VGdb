# This search algorithm will use recursion to return a list of games that match a search pattern.
# For example, is the search pattern is "god", it will append to the matching list all games that contain the pattern "god",
# such as the game "God of War".

def findname(name, name_list, starting_index = 0, char = 0, match_count = 0, matching_list = []):
    if name_list == []:
        return matching_list

    name_length = len(name)
    game = name_list[0]

    while True:

        # No match on last character
        if starting_index + 1 == len(game) and name[char].lower() != game[starting_index].lower():
            name_list.pop(0)
            findname(name, name_list, matching_list = matching_list)
            break

        # Match on current character
        elif name[char].lower() == game[starting_index].lower():
            match_count += 1

            # If it has found a match for the whole pattern
            if match_count == name_length:
                name_list.pop(0)
                matching_list.append(game)
                findname(name, name_list, matching_list = matching_list)
                break
            # If it gets to last character of the game's name and it hasn't matched with the whole pattern
            elif starting_index + 1 == len(game) and match_count != name_length:
                if name_list != []:
                    name_list.pop(0)
                findname(name, name_list, matching_list = matching_list)
                break
            # If it hasn't gotten to the last character yet
            else:
                char += 1
                starting_index += 1

        # If there isn't a match and search isn't over for current game
        else:
            char = 0
            match_count = 0
            starting_index += 1
    
    return matching_list