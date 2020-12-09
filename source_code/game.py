import random


class Game:
    def __init__(self, colors):
        self._colors = colors
        # self.match_result=[]

    def _match_color_and_index(self, user_colors, colors, match_result):
        index = 0

        while index < len(user_colors):
            if user_colors[index] == colors[index]:
                del user_colors[index]
                del colors[index]
                match_result.append('Black')
            else:
                index += 1

    def _match_color(self, user_colors, colors, match_result):
        index = 0

        while index < len(user_colors):
            if user_colors[index] in colors:
                colors.remove(user_colors[index])
                del user_colors[index]
                match_result.append('White')
            else:
                index += 1

    def check(self, user_colors):
        colors = list(self._colors)
        match_result = []

        if len(user_colors) != 4:
            return ('You should specify exactly 4 colors')
        self._match_color_and_index(user_colors, colors, match_result)
        self._match_color(user_colors, colors, match_result)
        random.shuffle(match_result)
        return match_result
