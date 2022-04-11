text = input()

line_commands = input()

while not line_commands == "For Azeroth":
    commands = line_commands.split()

    if commands[0] == "GladiatorStance":
        text = text.upper()
        print(text)
    elif commands[0] == "DefensiveStance":
        text = text.lower()
        print(text)
    elif commands[0] == "Dispel":
        index = int(commands[1])
        letter = commands[2]
        if 0 < index < len(text):
            first_part = text[:index]
            last_part = text[index + 1:]
            text = first_part + letter + last_part
            print("Success!")
        else:
            print("Dispel too weak.")
    elif commands[0] == "Target" and commands[1] == "Change":
        matches = commands[2]
        replacement = commands[3]
        text = text.replace(matches, replacement)
        print(text)
    elif commands[0] == "Target" and commands[1] == "Remove":
        substring = commands[2]
        if substring in text:
            text = text.replace(substring, "")
            print(text)

    else:
        print("Command doesn't exist!")

    line_commands = input()
