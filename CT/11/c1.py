def solution(phone_numbers, phone_owners, number):
    phone_dict = dict()

    for i in range(len(phone_numbers)):
        phone_number = phone_numbers[i]
        phone_owner = phone_owners[i]
        phone_dict[phone_number] = phone_owner

    if number in phone_dict:
        return phone_dict[number]
    else:
        return number