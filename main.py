from alphabet import items_list


def caesar(start_message, shift_amount, shift_direction):
    end_message = ""
    if shift_direction == "decode":
        shift_amount *= -1
    for char in start_message:
        if char in items_list:
            position = items_list.index(char)
            new_position = position + shift_amount
            end_message += items_list[new_position]
        else:
            end_message += char
    print(f"The {shift_direction}d message is {end_message}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # To avoid brute force attack/trying all the 26 numbers to get the message
    caesar(start_message=message, shift_amount=shift, shift_direction=direction)


    restart = input("Do you want to continue? Type 'yes' to continue. Otherwise Type 'no':\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye")



