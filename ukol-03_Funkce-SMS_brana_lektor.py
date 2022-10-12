import math


def check_phone_number(phone_number):
    phone_number = phone_number.replace(" ", "")  # BONUS
    is_valid = False
    if len(phone_number) == 13:
        if phone_number[0:4] == "+420":
            is_valid = True
    elif len(phone_number) == 9:
        is_valid = True
    return is_valid


def get_message_price(message):
    price_per_unit = 3
    max_characters_per_unit = 180
    count_units = len(message) / max_characters_per_unit
    total_price = math.ceil(count_units) * price_per_unit
    return total_price


phone_number_input = input("Phone number: ")
if check_phone_number(phone_number_input):
    message_text_input = input("Your message: ")
    message_price = get_message_price(message_text_input)
    print(f"Message price is {message_price} CZK.")
else:
    print(f"Phone number is invalid.")
