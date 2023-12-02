# check if the number of cubes in proposed game is higher than the set amount of cubes
def check_cubes(input_file):
    id_sum = 0
    RED = 12
    GREEN = 13
    BLUE = 14

    # read data
    with open(input_file) as f:
        lines = f.readlines()

    for line in lines:
        counts = True
        split_help = line.split(':')
        game_id = split_help[0].split(' ')[1]
        sets = split_help[1].split(';')

        # check if sets are valid
        for offered_set in sets:
            divided_by_colors = [x.strip() for x in offered_set.split(',')]
            for amount_color in divided_by_colors:
                amount_color_array = amount_color.split(' ')

                # check if the number of cubes is higher than possible,
                # disable the adding to final sum if needed
                if ((amount_color_array[1] == 'red' and int(amount_color_array[0]) > RED) or
                        (amount_color_array[1] == 'green' and int(amount_color_array[0]) > GREEN) or
                        (amount_color_array[1] == 'blue' and int(amount_color_array[0]) > BLUE)):
                    counts = False
                    break

        if counts:
            id_sum += int(game_id)

    print(id_sum)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_cubes('input.txt')
