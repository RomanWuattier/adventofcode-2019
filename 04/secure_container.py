puzzle_input = '367479-893698'    

def is_password(num):
    digits = list(int(d) for d in str(num))
    prev = 0
    group = 0
    is_adj = False
    for d in digits:
        if d < prev:
            return False
        elif d == prev:
            group += 1
        else:
            if group == 1:
                is_adj = True
            group = 0

        prev = d
    return is_adj or group == 1


if __name__ == '__main__':
    minimum, maximun = puzzle_input.split('-')
    print(len([num for num in range(int(minimum), int(maximun)) if (is_password(num))]))
