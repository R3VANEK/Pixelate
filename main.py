from PIL import Image
from PixelBox import PixelBox
import os, random
from palettes.palettes import choosePalette


"""
    Dzień dobry, witam w programie do piskelizacji zdjęć. Idąc za ciosem steganografii, chciałem się jeszcze jakoś pobawić
    modułem pillow i zrobiłem taki programik. W tym przypadku widac różnice w zdjęciach :) Podajemy nazwę obrazka umieszczonego w
    folderze pictures, paletę kolorów z której chcemy skorzystać, stopień pikselizacji i powstaje nowe zdjęcie na takiej bazie.
    Jak to działa? Załóżmy, że stopień pikselizacji to 4. Program docina zdjęcie żeby jego wymiary były podzielne przez 4. Potem 
    przechodzimy sobie po pikselach wycinając kwadraty 4x4. Zczytujemy z nich średni kolor i zastępujemy najbliższym kolorem z podanej
    palety. 

    Uwagi:

    - Program korzysta z relatywnych ścieżek do folderów, więc najlepiej jest uruchomić go z poziomu tego folderu

    - Przy większych zdjeciach albo małym stopniu pikselizacji, konwersja może troche zająć, musze kiedyś to zoptymalizować,
      może generatory się tutaj przydadzą ? :)

    - Palety, które widać w folderze palettes nie sa moje, ja tylko napisałem skrypt, który je wykorzystuje. Można 
      je pobrać ze strony https://lospec.com/palette-list w formacie .hex i będą tutaj dostępne do używania

    - Do testowania konwersji używałem obrazów ze strony wallHaven.org, można znaleźć tam znaleźć też fajne tapety na komputer :)

"""


cont = True
while cont:
    os.system("cls")
    print("-------------------------------------------------------------------------------------------------------------")
    print("Witam w programie do pikselizacji zdjęć. Aby zacząć wpisz nazwę zdjęcia w folderze pictures")
    print('\n')
    pic = input("")

    try:
        newImage = Image.open('./pictures/'+pic)
    except IOError:
        print("Nie można otworzyć takiego pliku !")
        dec = input("Kontynuować ? <T/N> : ")
        if dec != 'T':
            cont = False
            continue

    os.system("cls")
    print("Wybrano " + pic)
    print("")

    #ustawienie palety kolorów
    PixelBox.palette = choosePalette() 
    os.system("cls")
    
    #ustawienie wymiaru pojedyńczego piksela, wymiar 16 oznacza podzielenie zdjęcia na kwadraty 16x16 pikseli
    size = int(input("Podaj wymiar piskelizacji (liczba od 2 do 16) : "))
    boxSize = size

    #ustalanie nowych, dobrych wymiarów zdjęcia do pixelizacji
    width, height = newImage.size
    width = width // boxSize * boxSize
    height = height // boxSize * boxSize
    newImage1 = newImage.crop((0, 0, width, height))
    pixels_map = newImage1.load()


    print("Konwertuje...")
    for i in range(0, height, boxSize):
        for j in range(0, width, boxSize):

            temp = PixelBox(boxSize) 
            temp.setAvgColor(pixels_map, j, i) 
            temp.paintColor(pixels_map, j, i)
            del temp 
    print("Koniec konwertowania :)")

    name = str(random.randint(0,10000))
    newImage1.save('./modified_pictures/'+name+'.png')
    os.system("cls")
    print("zapisano jako %s.png" % (name))
    print("")
    dec = input("Kontynuować ? <T/N> : ")
    if dec != 'T':
        cont = False


