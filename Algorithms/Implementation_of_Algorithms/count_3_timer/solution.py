def count_three_in_timer(N):

    count_three_in_60 = 0
    total_count = 0

    for _ in range(60):
        one = _ % 10
        ten = _ // 10
        if one == 3 or ten == 3:
            count_three_in_60 += 1

    count_three_out_60 = 60 - count_three_in_60

    for hour in range(N+1):
        one = hour % 10
        ten = hour // 10
        if one == 3 or ten == 3:
            total_count += 60 * 60
        else:
            total_count += count_three_in_60 * 60 + count_three_out_60 * count_three_in_60

    return total_count