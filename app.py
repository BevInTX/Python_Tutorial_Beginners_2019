import random


class Dice:

    def __init__(self, number_of_sides):
        try:
            if number_of_sides > 3:
                self.number_of_sides = number_of_sides
            else:
                raise ValueError
        except ValueError:
            print('Dice must have at least 4 sides!')

    # ----------------------------------------------------------------------

    def roll(self, number_of_rolls):
        rolls = []
        for i in range(number_of_rolls):
            rolls.append(random.randint(1, self.number_of_sides))
        return tuple(rolls)


def main():
    six_sided_dice = Dice(6)
    print(six_sided_dice.roll(2))


if __name__ == "__main__":
    main()
