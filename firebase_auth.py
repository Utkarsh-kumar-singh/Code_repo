import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\UTKARSH KUMAR SINGH\Downloads\authentication-27979-firebase-adminsdk-gzspn-dd93c22384.json")
firebase_admin.initialize_app(cred)

# Function to authenticate the user
def authenticate_user(email, password): 
    try:
        user = auth.get_user_by_email(email)
        auth.verify_password(password, user.password_hash)
        return user
    except ValueError as e:
        print(f"Authentication error: {str(e)}")
        return None

# API endpoint for login
def login(email, password):
    user = authenticate_user(email, password)
    if user:
        # Login successful
        # Perform additional actions or return a success response
        print("Login successful")
    else:
        # Login failed
        # Return an error response
        print("Invalid email or password")

# API endpoint for logout
def logout():
    # Perform any logout actions
    print("Logout successful")

# Usage examples
login("huzifa@gmail.com", "dfhvjhabsi")
logout()
