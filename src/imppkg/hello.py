from googletrans import Translator

translator = Translator()


def say_hello(language):
    # TODO: cal here google translate
    return translator.translate("Hello World", dest=language)
