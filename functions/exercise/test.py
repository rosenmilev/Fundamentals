def current_condition(people, state, capacity):
    final_state = []
    people_left = people
    for wagon in state:
        if wagon < 4 and 0 < people_left < 4 - wagon:
            final_state.append(wagon + people_left)
            people_left = 0
        elif wagon < 4 and people_left >= 4 - wagon:
            people_left -= 4 - wagon
            final_state.append(4)
        else:
            final_state.append(wagon)
    final_state = " ".join(list(map(str, final_state)))
    return final_state


curr_people = int(input())
curr_state = input().split()

curr_state = list(map(int, curr_state))
curr_free_capacity = (len(curr_state) * 4) - sum(curr_state)

if curr_people < curr_free_capacity:
    print("The lift has empty spots!")
    print(current_condition(curr_people, curr_state, curr_free_capacity))
elif curr_people > curr_free_capacity:
    print(f"There isn't enough space! {curr_people - curr_free_capacity} people in a queue!")
    print(current_condition(curr_people, curr_state, curr_free_capacity))
else:
    print(current_condition(curr_people, curr_state, curr_free_capacity))
