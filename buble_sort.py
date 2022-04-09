list = [24, 12, 31, 10, 47, 5, 41, 3, 75, 15]
print("OK: ", list)

# last_e_index = len(list) - 1
# print(0, list)
# for idx in range(last_e_index):
#     if list[idx] > list[idx+1]:
#         list[idx], list[idx+1] = list[idx+1], list[idx]
#         print(idx+1, list)


def bubble_sort(list):
    last_e_index = len(list) - 1
    for passNO in range(last_e_index, 0, -1):
        for idx in range(passNO):
            print("Pass No: ", passNO, "Idx:  ", idx)
            if list[idx] > list[idx + 1]:
                print("Idx: ", list[idx], "Next: ", list[idx + 1])
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
                print(idx, "  ", list)
            else:
                print("Idx: ", list[idx], "Next: ", list[idx + 1])
                print(idx, "  ", list)

    return list


print("Result: ", bubble_sort(list))
