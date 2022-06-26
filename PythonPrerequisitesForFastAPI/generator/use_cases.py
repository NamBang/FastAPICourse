def fetch_users():
    start = 1
    
    while start <= 10000000:
        yield start
        start += 1

def send_email(user_name):
    print(user_name)

users = fetch_users()

for user in users:
    send_email(user)
