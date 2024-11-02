def parsor(list, length, num):

    result = []

    for i in range(0, length, num):
        result.append(list[i:i+num])

    return result

def get_min_string(list, length, unit):

    parsed_list = parsor(list, length, unit)

    answer = []

    count = 1

    before = None

    for i in parsed_list:
        if i == before:
            count += 1
        else:
            if count != 1:
                answer.append(before)
                answer.insert(-1, str(count))
                count = 1
            else:
                if before != None:
                    answer.append(before)
        before = i

    if count != 1:
        answer.append(str(count))
    answer.append(before)

    answer = ''.join(answer)

    return answer

def get_length(list):
    result = []
    for i in list:
        result.append(len(i))

    return result

if __name__ == '__main__':

    list = "aabbacc"

    length  = len(list)

    parse_list = []

    for i in range(1, length):
        parse_list.append(get_min_string(list, length, i))

    answer = min(get_length(parse_list))

    print(answer)
