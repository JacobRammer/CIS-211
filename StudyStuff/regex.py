"""
Regex syntax:
* = 0 or more
+ = one or more
? = zero or 1 repetitions
$ = matches the end of a string just before the newline
\s = [ \t\n\r\f\v]
\w = [0-9a-zA-Z_]
"""
import re

"""
Email regex
"""

email_pat = re.compile(r"""
                \s*
                (?P<user>
                [\w]+  # + means that there is more than 1 character
                )
                @
                (?P<host>
                (\w+\.)*(\w+)
                )
                \s*
                """, re.VERBOSE)

address_pat = re.compile(r"""
                \s*
                (?P<street_number>
                [0-9]+
                )
                \s
                (?P<street_name>
                ([A-Z0-9]\w*\s)+([A-Z0-9]\w*\s+)
                )
                (?P<town>
                ([A-Z])+([a-z]+)
                )
                ,
                (?P<state>
                [\s*A-Z]+
                )
                (?P<zip>
                [0-9]+
                )
                \s*
                """, re.VERBOSE)


def open_email_file(fname: str) -> list:
    email_list = []

    with open(fname) as email_data:
        email_data.readline()

        for line in email_data:
            email = line.strip()
            email_list.append(email)

    return email_list


def loop_emails(emails):
    email_list = []

    for email in emails:
        matched_emails = email_pat.search(email)
        em = matched_emails.groupdict()
        email_list.append(em)
    return email_list


def open_address_file(fname):
    raw_address_list = []

    with open(fname) as address_data:
        for line in address_data:
            address = line.strip()
            raw_address_list.append(address)
    return raw_address_list


def address_loop(address_list):
    add_list = []
    for address in address_list:
        matched_address = address_pat.search(address)
        add = matched_address.groupdict()
        add_list.append(add)

    return add_list


#
# test = "jrammer101@gmail.com"
# address = "8685 Trenton St Williamsburg, VA 23185"

# address_match = address_pat.search(address)
# add = address_match.groupdict()
# print(add)

# match = email_pat.search(test)
# emails = match.groupdict()
# print(emails)
# emails = open_email_file("C:\\Users\\Jacob\\Documents\\CIS211\\StudyStuff\\dataJun-2-2019.csv")
# print(loop_emails(emails))

# addresses = open_address_file("C:\\Users\\Jacob\\Documents\\CIS211\\StudyStuff\\address.txt")
# # print(addresses)
# address_search = address_loop(addresses)
# # print(address_search)
#
# for i in address_search:
#     print(i)

date_pattern = re.compile(r"""
\s* test \s*
\(  # ignore the (
(?P<month>
[A-Za-z]* 
)
\)  # end ignore
\s
(?P<day>
[0-9]*
), 
\s
(?P<year>
[0-9]*
)
""", re.VERBOSE)

date = " test (April) 18, 2015"

date_match = date_pattern.search(date)
test = date_match.groupdict()
print(test)
