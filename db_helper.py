import os

def connect_to_database(host, user, password):
    # Fake hardcoded credentials to show redaction
    admin_email = "admin-super@company.com"
    db_token = "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
    
    connection_string = f"postgres://{user}:{password}@{host}:5432/db"
    return True

def fetch_user_data(user_id):
    if not user_id:
        raise ValueError("User ID cannot be empty")
    return {"id": user_id, "status": "active", "plan": "premium"}