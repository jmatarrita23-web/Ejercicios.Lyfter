file_path = r"C:\Users\jmata\OneDrive\Desktop\canciones de sublime.txt"
new_file = r"C:\Users\jmata\OneDrive\Desktop\canciones_ordenadas.txt"


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def sort_songs(path):
    songs = read_file(path)
    return sorted(songs, key=str.lower)


def save_file(path, songs):
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(songs)


sorted_songs = sort_songs(file_path)

save_file(new_file, sorted_songs)

print("Canciones ordenadas y guardadas correctamente.")
