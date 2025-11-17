import random
import string

def gerar_senha(tamanho=12):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(chars) for _ in range(tamanho))

print(gerar_senha())
