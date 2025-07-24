import random
import string

import datetime

def hash_encryption(s1, s2, v):
    triple_of_values = (s1, v, s2)
    hash_value = hash(triple_of_values)

    return hash_value

def generate_random_string():
    rand_str = ''
    number_of_chars = random.randint(7,15)
    
    # Chars = Letters(lower- and upper case) + digits + special characters
    chars = string.ascii_letters + string.digits + string.punctuation

    for i in range(number_of_chars):
        index = random.randint(0, len(chars)-1)
        rand_str += chars[index]

    return rand_str

def create_log_file(name, efrom, eto, str1, hash_val, guessed_val, str2, coin_flip_val):
    f = open('log.txt', 'a')

    send_date = datetime.datetime.now()
    send_date = send_date.strftime('%d.%m.%Y %H:%M:%S')

    # TODO
    # send_date = date.today()
    if name == "Alice":
        protocol = '[' + name + ']\n' + \
            'Send date: ' + send_date + '\n' + \
            'From: ' + efrom + '\n' + \
            'To: ' + eto +'\n' + \
            'String 1: ' + str1 + '\n'  \
            'Hash value: ' + hash_val + '\n' + \
            '==================================\n'
    elif name == "Bob":
        protocol = '[' + name + ']\n' + \
            'Send date: ' + send_date + '\n' + \
            'From: ' + efrom + '\n' + \
            'To: ' + eto +'\n' + \
            'guessed value: ' + guessed_val + '\n'  \
            '==================================\n'
    elif name == "Alice 2":
        protocol = '[' + name + ']\n' + \
            'Send date: ' + send_date + '\n' + \
            'From: ' + efrom + '\n' + \
            'To: ' + eto +'\n' + \
            'String 1: ' + str1 + '\n'  \
            'String 2: ' + str2 + '\n'  \
            'Coin flip value: ' + coin_flip_val + '\n' + \
            '==================================\n'

    
    f.write(protocol)
    f.close()

    # Info
    print('Log file has been written')
