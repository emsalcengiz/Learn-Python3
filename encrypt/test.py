from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print(key)
    encryption_type = Fernet(key)
    encrypted_message = encryption_type.encrypt("emsal")
 
    print(encrypted_message)