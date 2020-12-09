from source_code.game import Game


def main():
    master_mind = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    number_of_attempts = 3

    for game_number in range(number_of_attempts):
        user_colors = input('Please input comma separated colors: ')
        user_colors = [color.strip().upper() for color in user_colors.split(',')]
        result = master_mind.check(user_colors)
        print(result)
        if len(result) == 4:
            print('Won')
            break
        else:
            print('Try again')
    else:
        print(f'All {number_of_attempts} tries exhausted, you lost, try again!!!')


if __name__ == '__main__':
    main()
