def findname(name, name_list, starting_index = 0, char = 0, match_count = 0, matching_list = []):
    if name_list == []:
        return matching_list

    name_length = len(name)
    game = name_list[0]

    if starting_index + 1 == len(game):
        name_list.pop(0)
        findname(name, name_list, matching_list = matching_list)

    # print(f'\nMatch count:', {match_count}, 'Char:', {char}, 'Starting index', {starting_index})
    # print(f'Comparing {name[char]}')   
    # print(f'To {game[starting_index].lower()}')

    if name[char].lower() == game[starting_index].lower():
        # print(f'Found a match at index {starting_index}')
        match_count += 1
            
        if match_count == name_length:
            # print(f'\nMoving to next game in the list')
            name_list.pop(0)
            matching_list.append(game)
            findname(name, name_list, matching_list = matching_list)
        else:
            char += 1
            findname(name, name_list, (starting_index + 1), char, match_count, matching_list = matching_list)
    
    else:
        findname(name, name_list, (starting_index + 1), matching_list = matching_list)
    
    return matching_list