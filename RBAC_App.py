#These are the usernames and roles for my login simulation.
users = {
    "ginna_admin": "admin",
    "ginna_user": "user"
}

def admin_action(role):
    #This checks if this person is an admin
    if role == "admin":
        print("Access granted: Welcome to the admin dashboard!")
    else:
        print("Access denied: You do not have permission to access the admin dashboard.")

def user_action(role):
    #Checks if this person has the user role
    if role == "user":
        print("Access granted: Welcome to the user dashboard!")
    else:
        print("Access denied: You do not have permission to access the user dashboard.")

#This is the account I am testing.
username = "ginna_admin"  # Change this to test different usernames

#This checks if the username exists before giving access
if username in users:
    role = users[username]
    print(f"Logged in as {username}. Role; {role}")

    admin_action(role)
    user_action(role)   
else:
    print("Login failed: Username not found.")
#This shows Confindentiality because each person can only open the dashboard that their role gives them access to.