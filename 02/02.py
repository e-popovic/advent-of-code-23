# check if the number of cubes in proposed game is higher than the set amount of cubes
def check_cubes(input_file):
    cubes_sum = 0

    # read data
    with open(input_file) as f:
        lines = f.readlines()

    for line in lines:
        min_red, min_green, min_blue = 0, 0, 0
        split_help = line.split(':')
        sets = split_help[1].split(';')

        # check if sets are valid
        for offered_set in sets:
            divided_by_colors = [x.strip() for x in offered_set.split(',')]
            for amount_color in divided_by_colors:
                amount_color_array = amount_color.split(' ')

                # if new number is higher than current minimum, update minimum
                if amount_color_array[1] == 'red' and int(amount_color_array[0]) > min_red:
                    min_red = int(amount_color_array[0])
                if amount_color_array[1] == 'green' and int(amount_color_array[0]) > min_green:
                    min_green = int(amount_color_array[0])
                if amount_color_array[1] == 'blue' and int(amount_color_array[0]) > min_blue:
                    min_blue = int(amount_color_array[0])

        cubes_sum += min_red * min_green * min_blue

    print(cubes_sum)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_cubes('input.txt')
