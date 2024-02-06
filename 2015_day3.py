def move(s, x, y):
    if s == '^':
        x += 1
    elif s == 'v':
        x -= 1
    elif s == '>':
        y += 1
    else:
        y -= 1
    return x, y

def day3_part1(input_text):
    x = 0
    y = 0
    houses = []
    for s in input_text:
        (x, y) = move(s, x, y)
        houses.append((x,y))
    return len(set(houses))

def day3_part2(input_text):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    step = 0
    houses = []
    for s in input_text:
        step += 1
        if step % 2 ==1:
            (x1, y1) = move(s, x1, y1)
            houses.append((x1, y1))
        else:
            (x2, y2) = move(s, x2, y2)
            houses.append((x2, y2))
    return len(set(houses))


if __name__ == '__main__':
    with open('day_03.txt', 'r') as file_obj:
        input_text = file_obj.read()
    #print(input_text)
    print(day3_part1(input_text))
    print(day3_part2(input_text))