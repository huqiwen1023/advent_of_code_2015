def day6_part1(input_text):
    xy = [[0] * 1000 for n in range(1000)]
    for i in range(1000):
        for j in range(1000):
            xy[i][j] = 0
    words = []
    lines = input_text.splitlines()
    for line in lines:
        words.append(line.split(","))
    for a in range(len(words)):
        x_begin = int(words[a][0].split(" ")[-1])
        y_begin = int(words[a][1].split(" ")[0])
        x_end = int(words[a][1].split(" ")[-1])
        y_end = int(words[a][2])

        if words[a][0].split(" ")[1] == "on":
            for i in range(x_begin, x_end+1):
                for j in range(y_begin, y_end+1):
                    xy[i][j] = 1
        elif words[a][0].split(" ")[1] == "off":
            for i in range(x_begin, x_end+1):
                for j in range(y_begin, y_end+1):
                    xy[i][j] = 0
        else:
            for i in range(x_begin, x_end+1):
                for j in range(y_begin, y_end+1):
                    if xy[i][j] == 0:
                        xy[i][j] = 1
                    else:
                        xy[i][j] = 0
    count_on = 0
    for i in range(1000):
        for j in range(1000):
            if xy[i][j] == 1:
                count_on += 1
    return count_on

def day6_part2(input_text):
    xy = [[0] * 1000 for n in range(1000)]
    for i in range(1000):
        for j in range(1000):
            xy[i][j] = 0
    words = []
    lines = input_text.splitlines()
    for line in lines:
        words.append(line.split(","))
    for a in range(len(words)):
        x_begin = int(words[a][0].split(" ")[-1])
        y_begin = int(words[a][1].split(" ")[0])
        x_end = int(words[a][1].split(" ")[-1])
        y_end = int(words[a][2])

        if words[a][0].split(" ")[1] == "on":
            for i in range(x_begin, x_end+1):
                for j in range(y_begin, y_end+1):
                    xy[i][j] += 1
        elif words[a][0].split(" ")[1] == "off":
            for i in range(x_begin, x_end+1):
                for j in range(y_begin, y_end+1):
                    if xy[i][j] > 0:
                        xy[i][j] -= 1
        else:
            for i in range(x_begin, x_end+1):
                for j in range(y_begin, y_end+1):
                    xy[i][j] += 2
    brightness = 0
    for i in range(1000):
        for j in range(1000):
            brightness += xy[i][j]
    return brightness

if __name__ == '__main__':
    with open('day_06.txt', 'r') as file_obj:
        input_text = file_obj.read()
    print(day6_part1(input_text))
    print(day6_part2(input_text))