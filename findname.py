def findname(name, name_list, starting_index = 0, char = 0, match_count = 0, matching_list = []):
    if name_list == []:
        return matching_list

    name_length = len(name)
    game = name_list[0]

    while True:

        print(f'\nMatch count:', {match_count}, 'Name length:', {name_length}, 'Char:', {char}, 'Starting index', {starting_index}, 'Game:', {game}, 'Game length:', {len(game)})
        # print(f'Comparing {name[char]}')   
        # print(f'To {game[starting_index].lower()}')

        # If exhausts all characters on game but matches with last character
        if starting_index + 1 == len(game) and name[char].lower() != game[starting_index].lower():
            print(f'{name} doesn\'t match {game}, moving to next game in the list: {name_list[1]}')
            name_list.pop(0)
            findname(name, name_list, matching_list = matching_list)
            break

        # If gets to last character, gets a match but not with the whole search pattern
        elif starting_index + 1 == len(game) and name[char].lower() == game[starting_index].lower() and match_count != name_length:
            if name_list != []:
                name_list.pop(0)
            findname(name, name_list, matching_list = matching_list)
            break

        # If there is a match
        elif name[char].lower() == game[starting_index].lower():
            print(f'Found a match at index {starting_index}')
            match_count += 1

            if match_count == name_length:
                print(f'\nMoving to next game in the list')
                name_list.pop(0)
                matching_list.append(game)
                print(f'Added {game} to the match list: {matching_list}')
                print(f'Search list is now {name_list}')
                findname(name, name_list, matching_list = matching_list)
                break
            else:
                char += 1
                starting_index += 1

        # If there isn't a match and search isn't over for current game
        else:
            char = 0
            match_count = 0
            starting_index += 1
    
    return matching_list