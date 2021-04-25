from random import randint
import const


def input_dices():
    const.dice = input(const.type_dice)
    const.mod = input(const.mode_dice)


def normal_roll():
    const.result = int(randint(1, int(const.dice)))


def advantage():
    const.result = min(int(randint(1, int(const.dice))), int(randint(1, int(const.dice))))


def hindrance():
    const.result = max(int(randint(1, int(const.dice))), int(randint(1, int(const.dice))))


def main():
    print(const.welcome)
    input_dices()
    if int(const.dice) in const.dice_list and int(const.mod) in const.roll_mod_list:
        if const.mod == '1':
            normal_roll()
        elif const.mod == '2':
            hindrance()
        elif const.mod == '3':
            advantage()
        else:
            print(const.error_message)
    else:
        print(const.error_message)
    print('Выпало ' + str(const.result) + '!\n')


if __name__ == "__main__":
    while True:
        main()
