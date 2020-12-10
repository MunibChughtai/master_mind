import random


class Game:
    def __init__(self, random_colors=False):
        self._random_colors = random_colors
        self._color_range = ['RED', 'BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'YELLOW']
        if not self._random_colors:
            self._random_colors = self.get_random_colors_from_color_list()

    def get_random_colors_from_color_list(self):
        random_colors = [random.choice(self._color_range).upper() for iteration in range(5)]
        return random_colors

    def check(self, user_input_colors):
        random_colors = list(self._random_colors)
        matching_hint = []

        self._match_colors_at_same_index(user_input_colors, random_colors, matching_hint)
        self._match_color(user_input_colors, random_colors, matching_hint)
        random.shuffle(matching_hint)
        return matching_hint

    def _match_colors_at_same_index(self, user_input_colors, random_colors, matching_hint):
        index = 0

        while index < len(user_input_colors):
            if user_input_colors[index] == random_colors[index]:
                del user_input_colors[index]
                del random_colors[index]
                matching_hint.append('Black')
            else:
                index += 1

    def _match_color(self, user_input_colors, random_colors, matching_hint):
        index = 0

        while index < len(user_input_colors):
            if user_input_colors[index] in random_colors:
                random_colors.remove(user_input_colors[index])
                del user_input_colors[index]
                matching_hint.append('White')
            else:
                index += 1
