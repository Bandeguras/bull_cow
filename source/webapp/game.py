from random import sample


def generate_numbers(n):
    return sample(range(1,10), n)

secret_nums = generate_numbers(4)
round_number = 0


def guess_numbers(secret, actual):
    global round_number
    try:
        actual = [int(s) for s in actual]
    except ValueError:
        return 'enter only integers'

    if len(actual) != 4:
        return 'there should be four integers'

    if len(set(actual)) != len(actual):
        return 'the integers must be unique'

    for i in actual:
        if i > 9 or i < 0:
            return 'the integers must be from 1 to 9'

    bulls = 0
    cows = 0

    for i in range(4):
        if actual[i] == secret[i]:
            bulls += 1
        elif actual[i] in secret:
            cows += 1
    round_number += 1

    if bulls == 4:
        secret_nums[:] = generate_numbers(4)
        round_number = 0
        return "You got it right!"


    return f'''You got {bulls} bulls, {cows} cows. Round: {round_number}'''
