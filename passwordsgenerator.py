import random

print('Hello,Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of passwords to generate:')
number = int(number)

length = input('Your password length:')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
