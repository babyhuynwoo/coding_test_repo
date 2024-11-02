
if __name__ == '__main__':

    # input_str = "1 3 2 3 2 4"
    input_str = "1 5 4 3 2 4 5 2"
    # input_str = "1 3 2 3 2"

    elements = input_str.split()

    element_counts = {}

    length = len(elements)

    for element in elements:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    result = 0
    accum = 0

    for key, count in element_counts.items():
        result += count * (length - count - accum)
        accum += count

    print(result)