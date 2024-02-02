import getpass
letras_User = []
ganhou = False

def jogo():
    palavra = getpass.getpass("Enforcador, qual a palavra? ")
    chanches = 5
    while True:

        for letra in palavra:
            if letra.lower() in letras_User:
                print(letra, end=" ") 
            else:
                print("_", end=" ")
        print(f"Você tem {chanches} tentativas")
        tentativa = input("Adivinhe a letra: ")
        letras_User.append(tentativa.lower())
        if tentativa.lower() not in palavra.lower():
            chanches -= 1

        ganhou = True
        for letra in palavra:
            if letra.lower() not in letras_User:
                ganhou = False

        if chanches == 0 or ganhou:
            break
                
    if ganhou:
        print(f"Vitória! A palavra era: {palavra}")
    else:
        print(f"Derrota! A palavra era: {palavra}")

while True:
    retry = input("Começar? (s/n): ").lower()
        
    if retry == "s":
        letras_User = []
        chanches = 5  
        call = jogo()

    else:
        print("Tchau!")
        break
