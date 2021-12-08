with open("day-8-input.txt") as file:
    instructions = file.readlines()


def part_1(instructions):
    numbers = []
    for line in range(len(instructions)):
        split_instructions = instructions[line].split("| ")
        numbers.append(split_instructions[1])

    total = 0
    for code in numbers:
        individual_codes = code.split()
        for word in individual_codes:
            if len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7:
                total += 1
                print(f"{word} is {total}")

    print(total)


part_1(instructions)
