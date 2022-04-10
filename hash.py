import hashlib
from hashlib import md5, blake2b
class HASH:
    def generaHash(h):
        digest=h.hexdigest()
        return digest

    print("-----------------------------------------------------------------------------------")
    print("Elige el algoritmo hash a utilizar:")
    print("1- MD5")
    print("2- SHA256")
    print("3- SHA512")
    print("4- Blake2b ")
    print("5- Blake2s")
    print("6- Salir")
    print("-----------------------------------------------------------------------------------")

x=0

while x!=6:

    nAlgoritmo=int(input())

    algoritmo = ""
    
    if nAlgoritmo !=6:

        print("Ingrese texto a cifrar: ")
        datos=input()

        if nAlgoritmo == 1:
            algoritmo="md5"

        if nAlgoritmo == 2:
            algoritmo="sha256"

        if nAlgoritmo == 3:
            algoritmo = "sha512"

        if nAlgoritmo == 4:
            algoritmo = "blake2b"
        
        if nAlgoritmo == 5:
            algoritmo = "blake2s"

        bdatos = bytes(datos, 'utf-8')
        h = hashlib.new(algoritmo,bdatos)
        hash1=HASH.generaHash(h)
        print()
        print("El texto cifrado en",algoritmo,"es:",hash1)
        print("-----------------------------------------------------------------------------------")
        print(" 1- MD5 \n 2- SHA256 \n 3- SHA512 \n 4- Blake2b \n 5- Blake2s \n 6- Salir")
        x=0

    elif nAlgoritmo == 6:
            print("Presione una tecla para salir...")