import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def pad_message_aes(message: bytes) -> bytes:
    """Ajoute le padding nécessaire pour AES."""
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    return padder.update(message) + padder.finalize()

def unpad_message_aes(padded_message: bytes) -> bytes:
    """Retire le padding du message."""
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(padded_message) + unpadder.finalize()

def encrypt_message_aes(message: str, encoded_key: str) -> str:
    """Chiffre un message en utilisant AES."""
    iv = os.urandom(16)
    key = base64.b64decode(encoded_key)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = pad_message_aes(message.encode('utf-8'))
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt_message_aes(encoded_ciphertext: str, encoded_key: str) -> str:
    """Déchiffre un message en utilisant AES."""
    ciphertext = base64.b64decode(encoded_ciphertext)
    key = base64.b64decode(encoded_key)
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return unpad_message_aes(padded_message).decode('utf-8')