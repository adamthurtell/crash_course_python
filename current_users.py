current_users = ['betsy', 'david', 'hector', 'jacob', 'felicia', 'admin']

new_users = ['Betsy', 'Bruce', 'Horace', 'david', 'Max']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry " + new_user.title() +", that username has been taken, please choose another username.")
    else:
        print("Congrats, " + new_user.title() + ", that username is available.")