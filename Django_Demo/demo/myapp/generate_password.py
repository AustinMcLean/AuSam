from django.contrib.auth.hashers import make_password

plain_password = 'Glausten'
hashed_password = make_password(plain_password)
print(hashed_password)