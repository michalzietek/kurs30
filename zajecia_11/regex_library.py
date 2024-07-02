import re

pattern = r"^[\S]+@[\w]+.[\S]{2,}$"
address_email = "michalzietkowski@gmail.com"

def match_address(email):
    if re.match(pattern, email):
        return True
    return False


check = match_address("michalzietkowski")
if check:
    print("Mozesz sie zarejestrowac")
else:
    print("Adres email jest niepoprawny")