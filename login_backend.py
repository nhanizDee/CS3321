from utils import check_credentials

def authenticate_user(username, password):
    """
    Authenticates the user and returns their role if successful.
    """
    # Check for blank fields
    if not username or not password:
        return None, "Username or password cannot be blank."

    # Verify credentials
    role = check_credentials(username, password)
    if role:
        return role, None
    else:
        return None, "Invalid username or password."
