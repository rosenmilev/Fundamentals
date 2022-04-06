class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        message = ""
        if self.bullets > 0:
            message = "shooting..."
            self.bullets -= 1
        else:
            message = "no bullets left"

        return message

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

# Test code:
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
