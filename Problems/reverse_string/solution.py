
def minimun_reverse(string: str):

    set_1 = 0
    set_0 = 0

    for _ in sample.split('1'):
        if _ == "":
            set_1 += 1
        else:
            set_0 += 1

    answer = min(set_1, set_0)

    return answer

if __name__ == "__main__":

    sample = "010011001110"

    sample_2 = "101100110001"

    answer = minimun_reverse(sample)
    print(answer)

    answer = minimun_reverse(sample_2)
    print(answer)
