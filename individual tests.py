def to_hex_string(data):  # method 1

    hex_string = ""

    for num in data:
        hexa_conversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        hex_string += hexa_conversion[num]

    return hex_string


def count_runs(flat_data):  # method 2

    current = flat_data[0]
    count = 1
    equal_nums = 0

    for item in flat_data[1:]:

        if current == item:
            equal_nums += 1

        else:  # item = 2, current = 3
            count += 1
            equal_nums = 0
            current = item

        if equal_nums >= 15:  # special case, there are no more than 15 elements in a group
            count += 1
            equal_nums = 0

    return count


def encode_rle(flat_data):  # method 3

    res = []
    count = 1
    previous_current = ""

    for item in flat_data:

        if item != previous_current:

            if previous_current:
                res += [count, previous_current]

            if previous_current == 0:
                res += [count, previous_current]

            previous_current = item
            count = 1

        else:
            count += 1

        if count >= 15:
            res += [count, previous_current]
            count = 0

    res += [count, previous_current]

    return res


def get_decoded_length(rle_data):  # method 4

    sum_odd = 0

    for index, item in enumerate(rle_data):

        if index % 2 == 0:
            sum_odd += item

    return sum_odd


def decode_rle(rle_data):  # method 5

    res = []
    count = 0
    current = 0

    for i in rle_data:
        count += 1

        if count % 2 != 0:
            current = i

        else:
            i = str(i)
            res = res + (current * [i])

    for i in range(len(res)):
        res[i] = int(res[i])

    return res


def string_to_data(data_string):  # method 6

    res = []

    for i in data_string:
        current = int(i, 16)
        res += [current]

    return res


def to_rle_string(rle_data):  # method 7
    res = ""

    for index, num in enumerate(rle_data):
        if index % 2 == 0:
            res += str(num)

        else:
            hexa_conversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
            num = (hexa_conversion[num])
            res += str(num)
            res += ":"

    return res[:len(res) - 1]


def string_to_rle(rle_string):  # method 8

    res = rle_string.split(":")
    new_res = []

    for item in res:

        if len(str(item)) == 3:
            count = (int(item[1]) + 10)
            length = int(item[2], 16)
            new_res.append(count)
            new_res.append(length)

        if len(str(item)) == 2:
            count = int(item[0])
            length = int(item[1])
            new_res.append(count)
            new_res.append(length)

    return new_res

    string = "15f"
    string[0:2] = "15"
    string[2] = "f"
    [15, 15]
    # if len = 3
    # append count integer
    # convert length to hexa

    # if len = 2
    # slice
    # append



# rle_string = "15f:64:1a:14b"
# strings = rle_string.split(":")
# iterate through strings
# use slicing to separate 15 f, 6 4, 1 a, 14 b
# print(strings)
