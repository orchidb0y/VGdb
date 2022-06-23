def findname(name, name_list, starting_index = 0, char = 0, match_count = 0, names = []):
    if name_list == []:
        return names

    name_length = len(name)
    game = name_list[0]

    if starting_index + 1 == len(game):
        name_list.pop(0)
        findname(name, name_list, names = names)

    # print(f'\nMatch count:', {match_count}, 'Char:', {char}, 'Starting index', {starting_index})
    # print(f'Comparing {name[char]}')   
    # print(f'To {game[starting_index].lower()}')

    if name[char].lower() == game[starting_index].lower():
        # print(f'Found a match at index {starting_index}')
        match_count += 1
            
        if match_count == name_length:
            # print(f'\nMoving to next game in the list')
            name_list.pop(0)
            names.append(game)
            findname(name, name_list, names = names)
        else:
            char += 1
            findname(name, name_list, (starting_index + 1), char, match_count, names = names)
    
    else:
        findname(name, name_list, (starting_index + 1), names = names)
    
    return names