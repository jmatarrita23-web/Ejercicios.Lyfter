from datetime import date


class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1

        return age


def adult_age(func):

    def wrapper(user):

        if user.age < 18:
            raise ValueError("Es menor de edad")

        return func(user)

    return wrapper


@adult_age
def enter_bar(user):
    print("Puedes entrar al bar")


ninoraro = User(date(2012, 5, 10))

enter_bar(ninoraro)