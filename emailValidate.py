
from email_validator import validate_email, EmailNotValidError
import sys


'''
It accepts only one command line parameter which is the email address to validate. It will return true or false.
'''

if len(sys.argv) == 1:
  email = ""
else:
  email = sys.argv[1]

def check(email):
    try:
      # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v.normalized
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        return False

print(check(email))

