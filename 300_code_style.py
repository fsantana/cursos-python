# https://peps.python.org/pep-0008/

# Contants
CONSTANTE = 1


# Class PascalCase
# two line breaks after class definition or 1 between methods definition

class Foo1:
    pass


class Bar1:
    def bar(self, arg1, arg2, arg3):
        result = arg1 + arg2
        return result

    def foo(self, arg1, arg2, arg3):
        result = arg1 + arg2 / arg3
        return result


def foo(arg1, arg2, arg3):
    result = arg1 + arg2 / arg3
    return result

# variables , proporties , functions and methods: lower_snake_case


# Indetetion : Four spaces

# Comment inline

'''
    Block Comment (docstirng)
    https://peps.python.org/pep-0257/

'''

# Doc String


class Foo:
    def set_name(self, name):
        """_summary_

        Args:
            name (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self
