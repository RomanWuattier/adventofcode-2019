puzzle_input = '367479-893698'    


def is_increasing(num):
    digits = list(str(num))
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True


def has_double(num):
    digits = list(str(num))
    return len(set(digits)) < len(digits)


def group(num):
    digits = list(str(num))
    count = 0
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            count += 1
        elif count != 1:
            count = 0
        else:
            return True
    return False or count == 1


if __name__ == '__main__':
    minimum, maximun = puzzle_input.split('-')
    arr = [num for num in range(int(minimum), int(maximun)) if is_increasing(num) and has_double(num)]
    # Part 1
    print(len(arr))
    # Part 2
    print(len([a for a in arr if group(a)]))
