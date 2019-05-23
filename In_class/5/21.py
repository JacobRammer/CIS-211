"""
Jacob Rammer

"""

import re
from typing import Pattern

email_list_pat = re.compile("""
(
    (?P<e>[a-z]+)
    (, \s* (?P<e>)
    
)?
""", re.VERBOSE | re.IGNORECASE)
