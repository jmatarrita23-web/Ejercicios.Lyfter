import csv


def add_games():

    amount = int(input("¿Cuántos videojuegos desea ingresar?: "))

    with open(r"C:\Users\jmata\OneDrive\Desktop\videojuegos_tab.txt", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file, delimiter="\t")

        writer.writerow([
            "Nombre",
            "Género",
            "desarrollador",
            "Clasificación ESRB",
        ])

        for i in range(amount):

            print(f"\ncaso #{i + 1}")

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

    print("\nInformación guardada correctamente.")


add_games()
