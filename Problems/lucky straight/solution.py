
def cal_score():
    score = input("점수를 입력하세요: ")

    half_length = int(len(score) / 2)

    left_part = right_part = 0

    for i in range(half_length):

        left_part += int(score[i])

        right_part += int(score[i+half_length])

    if left_part == right_part:
        print("LUCKY")
    else:
        print("READY")

if __name__ == '__main__':
    
    cal_score()