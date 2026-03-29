#Criptografia simétrica
# Criptografar: mensagem -> func(mensagem, chave) -> cifra
# Descriptografar: cifra -> func(cifra, chav) -> menssagem

# criptografia eXclusive OR (XOR)
# sintaxe XOR: a ^ b

from os import urandom

def gen_key(lengt: int) -> bytes:
    return urandom(lengt)

def xor(b1: bytes, b2: bytes):
    return bytes(a ^ b for a,b in zip(b1,b2))

if __name__ == "__main__":
    message = input(b"digite a mensagem a ser criptografada com a operacao xor: ")
    print(f"Mensagem: {message}")

    key = gen_key(len(message))
    print(f"Chave: {key} ")

    cipher = xor(message.encode('utf-8'),key)
    print(f"Cifra: {cipher}")

    if xor(cipher, key).decode('utf-8') == message:
        print("[+] - Teste passou.")
    else:
        print("[-] - Teste falhou")
 