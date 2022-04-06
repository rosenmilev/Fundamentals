def uninterrupted_times(ticket_to_check):
    sequence = 1
    uninterrupted = [0, ""]

    for i in range(1, len(ticket_to_check)):
        if ticket_to_check[i - 1] == ticket_to_check[i]:
            sequence += 1
        else:
            sequence = 1

        if sequence > uninterrupted[0] and ticket_to_check[i - 1] in winning_symbols:
            uninterrupted[0] = sequence
            uninterrupted[1] = ticket_to_check[i - 1]

    return uninterrupted


data = input().split(", ")
winning_symbols = "@#$^"

for ticket in data:
    ticket = ticket.strip()

    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    first_half = ticket[:10]
    second_half = ticket[10:]

    first = uninterrupted_times(first_half)
    second = uninterrupted_times(second_half)

    if first[0] == second[0] == 10 and first[1] == second[1]:
        print(f'ticket "{ticket}" - {10}{ticket[0]} Jackpot!')

    elif first[1] == second[1] and first[0] >= 6 and second[0] >= 6:
        print(f'ticket "{ticket}" - {min(first[0], second[0])}{first[1]}')

    else:
        print(f'ticket "{ticket}" - no match')
