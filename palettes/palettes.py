import os


def choosePalette():
    print("jaką paletę kolorów chcesz wybrać?")
    print('-----------------------------------')
    l = os.listdir(os.getcwd()+'\\palettes\\')
    right_files = []
    for filename in l:
        if filename[-2:] == 'ex':
            right_files.append(filename)
            print(filename)

    print('\n')
    decision = input('')

    try:
        file = open(os.getcwd()+'\\palettes\\'+decision, 'r')
    except IOError:
        print("nie udało się otworzyć pliku, podano złą nazwę")
        exit()


    palette = []
    for line in file.readlines():
        palette.append(tuple(int(line[i:i+2], 16) for i in (0, 2, 4)))

    return palette
