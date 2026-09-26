def verify_card_number(card_number):
    digits = [int(d) for d in card_number if d.isdigit()]

    total = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return "VALID!" if total % 10 == 0 else "INVALID!"   