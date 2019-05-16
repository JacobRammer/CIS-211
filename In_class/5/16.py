"""
Jacob Rammer

"""
import re

email = re.compile(r''
                   r'[a-z0-9_.+]+'  # Name. one or more
                   r'@'
                   r'[a-z0-9_.+]+'  # domain name
                   '', re.VERBOSE | re.IGNORECASE)


def find_email(string):
    return email.findall(string)


test = "jrammer101@gmail.com"

print(find_email(test))
