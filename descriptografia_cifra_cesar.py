texto_plano = input("Digite a menssagem a ser descriptografada: ")
deslocamento = int(input("Qual a chave de deslocamento? "))
texto_cifrado = '' 
for caractere in texto_plano:
    pos = ord(caractere)
    if (48 <= pos <=57):
        nova_pos = (pos - 48 - deslocamento) % 10 + 48
    elif (65 <= pos <= 90):
        nova_pos = (pos - 65 - deslocamento) % 26 + 65
    elif (97 <= pos <=122):
        nova_pos = (pos - 97 - deslocamento) % 26 + 97
    else:
        nova_pos = pos
    texto_cifrado += chr(nova_pos)
print(f"Menssagem criptografada com a cifra de César: {texto_cifrado}")