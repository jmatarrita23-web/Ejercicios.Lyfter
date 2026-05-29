phrase=input("Introduce una frase separada por guiones: ")
def phrase_order(phrase):  
    list_phrase= phrase.split("-")
    sort_phrase= sorted(list_phrase)
    print("-".join(sort_phrase))
phrase_order(phrase)