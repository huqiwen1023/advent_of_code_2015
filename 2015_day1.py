def day1_part1(input_text):
    count = 0
    for s in input_text:
        if s == '(':
            count += 1
        elif s == ')':
            count -= 1
    return count

def day1_part2(input_text):
    count = 0
    position = 0
    for s in input_text:
        if count >= 0:
            if s == '(':
                count += 1
            elif s == ')':
                count -= 1
        else:
            break
        position += 1
    return position

if __name__ == '__main__':
    with open('day_01.txt', 'r') as file_obj:
        input_text = file_obj.read()
    #print(input_text)
    print(day1_part1(input_text))
    print(day1_part2(input_text))