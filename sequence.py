def is_sum_sequence_o_n_3(arr):
    if arr[0] != 1:
        return False

    for i in range(1, len(arr)):
        found_sum = False

        for j in range(i):
            for k in range(j, i):
                if arr[i] == arr[j] + arr[k]:
                    found_sum = True
                    break
            if found_sum:
                break

        if not found_sum:
            return False

    return True


def is_sum_sequence_o_n_2(arr):
    if len(arr) < 2 or arr[0] != 1:
        return False

    possible_sums = set()

    possible_sums.add(arr[0] + arr[0])

    for i in range(1, len(arr)):
        if arr[i] not in possible_sums:
            return False

        for j in range(i + 1):
            possible_sums.add(arr[j] + arr[i])

    return True


if __name__ == "__main__":
    print(is_sum_sequence_o_n_2([1, 2, 3, 5, 8]))
    print(is_sum_sequence_o_n_2([1, 2, 4, 5, 3]))
    print(is_sum_sequence_o_n_2([1, 2, 3, 11]))
    print(is_sum_sequence_o_n_2([1, 1, 2]))

    print(is_sum_sequence_o_n_3([1, 2, 3, 5, 8]))
    print(is_sum_sequence_o_n_3([1, 2, 4, 5, 3]))
    print(is_sum_sequence_o_n_3([1, 2, 3, 11]))
    print(is_sum_sequence_o_n_3([1, 1, 2]))