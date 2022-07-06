import re

def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
    if(re.search(regex,email)):   
        return True  
    else:   
        return False
    
"""
email recognition lib

email-validator 1.0.5
pylsEmail 1.3.2
py3-validate-email

Given below are some of the Email Validation APIs:
Mailboxlayer
Isitrealemail
Sendgrid’s Email Validation API
"""