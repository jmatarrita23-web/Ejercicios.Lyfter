def print_info(function):

    def wrapper(*args):

        print("Parameters:", args)

        result = function(*args)

        print("Return:", result)

        return result

    return wrapper


@print_info
def add(*args):
    return sum(args)


add(5, 3)
