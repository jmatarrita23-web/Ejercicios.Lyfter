class FlyMixin:
    def fly(self):
        print("Volando")


class SwimMixin:
    def swim(self):
        print("Nadando")


class AttackMixin:
    def attack(self):
        print("Atacando")
        

class Dragon(FlyMixin, SwimMixin, AttackMixin):
    pass