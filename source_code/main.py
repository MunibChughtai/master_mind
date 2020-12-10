from source_code.game import Game


def main():
    my_game = Game()
    number_of_attempts = 60

    for attempt_number in range(number_of_attempts):
        user_input_colors = input('Please input comma separated colors: ')
        user_input_colors = [color.strip().upper() for color in user_input_colors.split(',')]
        result = master_mind(my_game, user_input_colors)
        print(result)
        if result == 'WON':
            break
    else:
        print(f'All {number_of_attempts} tries exhausted, you lost, try again!!!')


def master_mind(my_game, user_input_colors):
    if len(user_input_colors) != 4:
        return 'You should specify exactly 4 colors'

    invalid_colors = [color for color in user_input_colors if color not in my_game._color_range]
    if invalid_colors:
        return 'You have given an invalid color(s)!!!'

    matching_hint = my_game.check(user_input_colors)
    if set(matching_hint) == {'Black'}:
        return 'WON'
    else:
        return matching_hint


if __name__ == '__main__':
    main()
