import re
with open("./src/data_corey.txt", "r") as text:
    num_nums = 0
    end_7 = 0
    for line in text:
        find = re.compile(r"[\d]{3}-[\d]{3}-[\d]{4}")
        num_7 = re.compile(r"[\d]{3}-[\d]{3}-[\d]{3}7$")
        found = re.search(find, line)
        found7 = re.search(num_7, line)
        if found:
            num_nums += 1
        if found7:
            end_7 += 1


print(f"Total amount of phone numbers: {num_nums}")
print(f"Total amount of phone numbers with ending 7: {end_7}")
text = text.close()

