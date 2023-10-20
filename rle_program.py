def to_hex_string(data):  # method 1

    hex_string = ""

    for num in data:
        hexa_conversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e",
                           "f"]  # hexadecimal to decimal conversion table
        hex_string += hexa_conversion[num]

    return hex_string


def count_runs(flat_data):  # method 2

    current = flat_data[0]
    count = 1
    equal_nums = 0

    for item in flat_data[1:]:

        if current == item:  # determines equal numbers
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

    for item in flat_data:  # goes through every element in flat data

        if item != previous_current:  # determines if item and previous current are equal

            if previous_current:  # first half of list
                res += [count, previous_current]

            if previous_current == 0:  # second half of list
                res += [count, previous_current]

            previous_current = item
            count = 1

        else:  # if item = previous current count += 1
            count += 1

        if count >= 15:  # special case if count is greater than 15
            res += [count, previous_current]
            count = 0

    res += [count, previous_current]

    return res


def get_decoded_length(rle_data):  # method 4

    sum_even = 0

    for index, item in enumerate(rle_data):  # gives index and number/item

        if index % 2 == 0:  # if index is even add number to the list
            sum_even += item

    return sum_even


def decode_rle(rle_data):  # method 5

    res = []
    count = 0
    current = 0

    for i in rle_data:  # for each item in rle data
        count += 1

        if count % 2 != 0:  # if index is odd append num
            current = i

        else:  # if index is even repeat next number in list by current number
            i = str(i)
            res = res + (current * [i])

    for i in range(len(res)):
        res[i] = int(res[i])

    return res


def string_to_data(data_string):  # method 6

    res = []

    for i in data_string:  # converts any hexadecimal values in the string and appends all values into a list
        current = int(i, 16)
        res = res + [current]

    return res


def to_rle_string(rle_data):  # method 7

    res = ""

    for index, num in enumerate(rle_data):
        if index % 2 == 0:  # if index is even
            res += str(num)

        else:
            # if index is odd convert hexadecimal to decimal and add that number as well as a delimiter into the result
            hexa_conversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]  #
            num = (hexa_conversion[num])
            res += str(num)
            res += ":"

    return res[:len(res) - 1]


def string_to_rle(rle_string):  # method 8

    res = rle_string.split(":")
    new_res = []  # new list

    for item in res:

        if len(str(item)) == 3:
            # if length is 3 then append count and length
            count = (int(item[1]) + 10)
            length = int(item[2], 16)
            new_res.append(count)
            new_res.append(length)

        if len(str(item)) == 2:
            # if length is 2 then append count and length while converting length to decimal
            count = int(item[0])
            length = int(item[1], 16)
            new_res.append(count)
            new_res.append(length)

    return new_res


if __name__ == '__main__':

    from console_gfx import ConsoleGfx

    print("Welcome to the RLE image encoder!")
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    # ConsoleGfx.display_image(ConsoleGfx.test_image)
    rle_image = True

    while rle_image:
        # prompt for the user input for menu choice
        print("\nRLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")
        option = int(input("Select a Menu Option: "))

        if option == 0:
            rle_image = False
            # exits program

        elif option == 1:  # load image data from file
            file_name = input("Enter name of file to load: ")
            ConsoleGfx.load_file(file_name)  # read the image data from file
            image_data = ConsoleGfx.load_file(file_name)  # assign ConsoleGfx.load_file(filename) to image_data
            # store the image data in the image_data variable

        elif option == 2:  # load image data from test_image
            print("Test image data loaded.")
            image_data = ConsoleGfx.test_image
            # assign ConsoleGfx.test_image to image_data

        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_string1 = string_to_rle(rle_string)
            rle_string2 = decode_rle(rle_string1)
            image_data = rle_string2
            # rle string to rle byte data to flat byte data
            # store flat byte data as image data

        elif option == 4:
            hex_rle_data = input("Enter the hex string holding RLE data: ")
            hex_rle_data1 = string_to_data(hex_rle_data)
            image_data = decode_rle(hex_rle_data1)
            # rle hex string to rle byte data to flat byte data
            # store flat byte data as image data

        elif option == 5:
            hex_flat_data = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_flat_data)
            # flat string to flat byte data
            # store flat byte data as image data

        elif option == 6:
            # display the image
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)

        elif option == 7:
            rle_representation = encode_rle(image_data)
            rle_representation1 = to_rle_string(rle_representation)
            print(f"RLE representation: {rle_representation1} ")
            # flat byte data to rle byte data to rle string
            # print rle string

        elif option == 8:
            rle_hex_values = encode_rle(image_data)
            rle_hex_values1 = to_hex_string(rle_hex_values)
            print(f"RLE hex values: {rle_hex_values1} ")
            # flat byte data to rle byte data to rle hex string
            # print rle hex string

        elif option == 9:
            flat_hex_values = to_hex_string(image_data)
            print(f"Flat hex values: {flat_hex_values}  ")
            # flat byte data to flat string
            # print flat string

        else:  # If user inputs any other menu option
            print("Error! Invalid input.")
