
def process_string(input_string):
    letters = []
    total_sum = 0

    for char in input_string: 
        if char.isdigit():
            total_sum += int(char)  
        else:
            letters.append(char)  

    letters.sort()  
    if total_sum > 0:
        letters.append(str(total_sum))  

    return ''.join(letters)  

if __name__ == '__main__':

    string = input("문자열을 입력하세요: ")

    answer = []
    result = 0

    for i in string:
        ascii_num = ord(i)
        if ascii_num < 65:
            result += int(i)
        else:
            answer.append(i)

    answer.sort()
    answer.append(str(result))

    result = ''.join(answer)
    print(result)