from random import choice
import string

def RandomPassword() :
    base_senha = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    senha_aleatoria = ""

    for i in range(8):
       senha_aleatoria += choice(base_senha)
    
    return senha_aleatoria