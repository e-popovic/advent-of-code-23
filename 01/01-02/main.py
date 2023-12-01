import re

digits_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
               'nine': 9}


# get integer digit from the word
def replace_digits(word):
    return digits_dict[word]


# find a sum of double-digit numbers made from the first and last digit in each string
def main(input_file):
    final_sum = 0

    # read data
    with open(input_file) as f:
        lines = f.readlines()

    # find digits and add each new number
    for line in lines:
        # find words and digits
        nums = re.findall('(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))', line)
        digit_nums = []

        # check all found numbers for words
        for num in nums:
            # if digit, keep it a digit
            if re.compile("\d").match(num):
                digit_nums.append(int(num))
            # if word, convert to digit
            else:
                digit_nums.append(replace_digits(num))

        # add first and last digit
        if digit_nums:
            value = digit_nums[0] * 10 + digit_nums[-1]
            final_sum += value

    print(final_sum)


if __name__ == '__main__':
    main('input.txt')
