from django.contrib.auth.hashers import make_password

plain_password = '' # Enter desired password here
hashed_password = make_password(plain_password)
print(hashed_password)