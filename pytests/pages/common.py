import random
import string


class Common:

    # Método para gerar valores inválidos
    @staticmethod
    def values_change(value):
        if ".to_i" in value:
            return str(value.split('.')[0])
        elif value == "None":
            return str(None)
        elif value == "number_negative":
            return str(-1)
        elif value == "boolean_true":
            return str(True)
        elif value == "boolean_false":
            return str(False)
        elif ".characters_type_string" in value:
            letters = string.ascii_lowercase
            number = int(value.split('.')[0])
            return str(( ''.join(random.choice(letters) for i in range(number)) ))
        elif ".characters_type_numbers" in value:
            number = int(value.split('.')[0])
            return str(( ''.join(random.choice("123456789") for i in range(number)) ))
        elif value == "Array":
            return str([])
        elif value == "Hash":
            return str({})
        else:
            return value