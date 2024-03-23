def main():
    chars = {}
    with open('snow.txt') as file:
        line = file.readline()
        i = 0
        while True:
            i = line.find('WB', i)
            if i == -1:
                break
            if i > 0:
                c = line[i - 1]
                if c in chars:
                    chars[c] += 1
                else:
                    chars[c] = 1
            i += len("WB")
    max_item = list(sorted(chars, key=lambda x: chars[x], reverse=True))[0]
    chars_list = list(sorted(chars, key=lambda x: x))
    for c in chars_list:
        if chars[c] == chars[max_item]:
            print(c)
            break
