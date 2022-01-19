import sys

from imppkg.hello import say_hello


def main():

    try:
        language = sys.argv[1]
    except ValueError:
        language = "IT"

    result = say_hello(language)
    print(result)
