# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_content = letter.read()
    with open("Input/Names/invited_names.txt", mode="r") as names_lst:
        names = names_lst.readlines()
        for all_name in names:
            name = all_name.strip("\n")
            final_letter = letter_content.replace("[name]", f"{name}")
            changed_letter = final_letter.replace("Angela", "Manya")
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as mail:
                mail.write(changed_letter)
