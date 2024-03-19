from code.text_file_reader import TextFileReader


file_reader = TextFileReader("data\input_data.txt")

digits = file_reader.first_and_last_digit()

if digits:
    sum_of_new_numbers = 0
    for digit_pair in digits:
        new_number = int(digit_pair[0] + digit_pair[1])
        sum_of_new_numbers += new_number