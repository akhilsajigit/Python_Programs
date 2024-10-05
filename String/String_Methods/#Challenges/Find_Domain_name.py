email = input("Enter your email : ")
loc = email.find('@')
print('User name : ',email[:loc])
print('Domain name : ',email[loc+1:])
