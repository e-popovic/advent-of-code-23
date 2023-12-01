# find a sum of double-digit numbers made from the first and last digit in each string
def main(input_file):
    final_sum = 0

    # read strings
    with open(input_file) as f:
        lines = f.readlines()

    # find digits and add each new number
    for line in lines:
        res = [int(i) for i in line if i.isdigit()]
        value = res[0] * 10 + res[-1]
        final_sum += value

    print(final_sum)


if __name__ == '__main__':
    main('input.txt')
