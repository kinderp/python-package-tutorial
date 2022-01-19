import sys

from imppkg.hello import say_hello
from pprint import pprint
from googletrans import LANGUAGES


def main():
    try:
        if len(sys.argv) != 2:
            print("You must specify a destination language in iso639-1")
            print("See down below for a list of all possible options")
            pprint(LANGUAGES)
            sys.exit()
        language = sys.argv[1]
    except ValueError:
        language = "IT"

    result = say_hello(language)
    print(result)


if __name__ == "__main__":
    main()
