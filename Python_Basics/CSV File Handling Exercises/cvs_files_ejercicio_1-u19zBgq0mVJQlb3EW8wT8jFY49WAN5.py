import csv

def add_games():

    amount = int(input("¿Cuántos videojuegos desea ingresar?: "))

    with open("videojuegos.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Nombre",
            "Género",
            "Desarrollador",
            "Clasificación ESRB"
        ])

        for i in range(amount):

            print(f"\nVideojuego #{i + 1}")

            name = input("Nombre: ")
            genre = input("Género: ")
            developer = input("Desarrollador: ")
            esrb = input("Clasificación ESRB: ")

            writer.writerow([
                name,
                genre,
                developer,
                esrb
            ])

    print("\nInformación guardada en videojuegos.csv")


add_games()