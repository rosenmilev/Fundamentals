def adding_heroes(heroes, current_hero):
    current_hero = current_hero.split(" ")
    hero_name = current_hero[0]
    hp = int(current_hero[1])
    mp = int(current_hero[2])

    heroes[hero_name] = [hp, mp]

    return heroes


heroes = {}

number_of_heroes = int(input())

for _ in range(number_of_heroes):
    current_hero = input()
    heroes = adding_heroes(heroes, current_hero)

command = input()

while True:
    if command == "End":
        break
    command = command.split(" - ")
    action = command[0]
    hero = command[1]
    current_hp = heroes[hero][0]
    current_mp = heroes[hero][1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
 
        if current_mp >= mp_needed:
            current_mp -= mp_needed
            heroes[hero][1] = current_mp
            print(f"{hero} has successfully cast {spell_name} and now has {current_mp} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage_to_take = int(command[2])
        attacker = command[3]

        if current_hp > damage_to_take:
            current_hp -= damage_to_take
            heroes[hero][0] = current_hp
            print(f"{hero} was hit for {damage_to_take} HP by {attacker} and now has {current_hp} HP left!")

        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif action == "Recharge":
        mp_to_recharge = int(command[2])

        if mp_to_recharge + current_mp > 200:
            recharged_mp = 200 - current_mp
            heroes[hero][1] = 200

        else:
            recharged_mp = mp_to_recharge
            current_mp += recharged_mp
            heroes[hero][1] = current_mp

        print(f"{hero} recharged for {recharged_mp} MP!")

    elif action == "Heal":
        hp_to_recharge = int(command[2])

        if hp_to_recharge + current_hp > 100:
            recharged_hp = 100 - current_hp
            heroes[hero][0] = 100

        else:
            recharged_hp = hp_to_recharge
            current_hp += recharged_hp
            heroes[hero][0] = current_hp

        print(f"{hero} healed for {recharged_hp} HP!")

    command = input()


for key in heroes:
    print(key)
    print(f"  HP: {heroes[key][0]}")
    print(f"  MP: {heroes[key][1]}")
