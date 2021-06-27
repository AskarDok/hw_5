import re
with open("./src/data_phone.json", "r") as text:
    num_of_phone_e164= 0
    num_of_cell_phones = 0

    for line in text:
        found_e164 = re.findall(r'"\+\d{13}"', line)
        found_cell_phones = re.findall(r'"\([0-6][0-9][0-9]\)\s(\d{3})-(\d{4})"', line)
        if found_e164:
            num_of_phone_e164 += 1
        if found_cell_phones:
            num_of_cell_phones += 1

print(f"Total amount of phone numbers with 13 digits: {num_of_phone_e164}")
print(f"Total amount of cell phones: {num_of_cell_phones}")

