import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    return stored_hash == hash_password(password)

# Exemple d'utilisation
stored_hash = hash_password("securePassword123")
print("Hachage du mot de passe:", stored_hash)
print("Vérification du mot de passe:", verify_password(stored_hash, "securePassword123"))
