usernames = ['Betsy', 'David', 'Hector', 'Jacob', 'Felicia', 'admin']

username = 'admin'

if usernames:
    for username in usernames:
        if username is 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")