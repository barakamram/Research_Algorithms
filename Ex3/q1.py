import re
import doctest
# take from geeksforgeeks with a little bit change:
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
regex = r'([A-Za-z0-9]+[._%+-])*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}'


def validation(email):
    """
    :param email: email
    :return if email is valid True
            else False
    >>> validation('abc-def.aaa@mail.com')
    True
    >>> validation('abc.def-aaa@mail.com')
    True
    >>> validation('abc.def.aaa@mail.com')
    True
    >>> validation('abc.def_aaa@msmail.co.il')
    True
    >>> validation('abc_def+aaa@ma-il.com')
    True
    >>> validation('abc.def..aaa@mail.com')
    False
    >>> validation('abc.def-aaa@mail.c')
    False
    >>> validation('abc.def-aa@a@mail.com')
    False
    >>> validation('abc.def_aaa@msmail.l')
    False
    >>> validation('abc_def+aaa@ma-il-com')
    False
    >>> validation('abc_def+aaa@')
    False
    >>> validation('abc_def.com')
    False
    """
    if re.match(regex, email):
        return True
    return False


def search_in_file(fn):
    """
    print 2 lists, one of valid emails and one of invalid email
    :param fn: file name
    """
    valid_ems, invalid_ems = [], []
    with open(fn, "r") as file:
        fr = file.read()
        em_lst = list(fr.split("\n"))
        for em in em_lst:
            valid_ems.append(em) if validation(em) else invalid_ems.append(em)
    print(f'------ valid ------\n{valid_ems}\n----- invalid -----\n{invalid_ems}')


if __name__ == '__main__':
    doctest.testmod()
    search_in_file('valid_email_format')
