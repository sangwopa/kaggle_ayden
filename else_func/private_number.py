import re

def compute_private_number_recognition(self, data):
    special = re.compile(r'\d{2}([0]\d|[1][0-2])([0][1-9]|[1-2]\d|[3][0-1])[-]*[1-4]\d{6}')
    
    con_tmp = bool(special.match(data))
    
    return con_tmp