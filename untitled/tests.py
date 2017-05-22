def delete_nulls(list):

    count = 0

    for i in range(0, len(list)):
        if list[i] != 0:
           list[count] = list[i]
           count += 1
    num_zeroes = (len(list)) - count

    for i in range(num_zeroes):
        list.pop()

    print(list)


listik = [0, 1, 2, 3, 0, 4, 0, 0, 19, 0, 8]
delete_nulls(listik)

