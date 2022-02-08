# Importieren des OS - Modules
import os

# Die Liste aller Dateien des Pfades aufrufen
path = "/Users/student/music"

#Variable mit dem Befehl der Ausgabe definieren
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# Alle Dateien ausgeben
print(dir_list)

#selection = input("Bitte wählen Sie den Song aus:")
songlist = dir_list
songs=len(dir_list)
print(songs)




for i in range(len(dir_list)):
    print("{} - {}".format(i,songlist[i]))

def songselection():
    selection = int(input("Bitte wählen Sie einen Song aus"))

    if selection <= songs-1:
        print(dir_list[selection])

        if dir_list[selection].endswith(".mp3"):
            filetoplay = path + "/" + (dir_list[selection])
            print(filetoplay)
            os.system("afplay " + path + "/{}".format(dir_list[selection]))
        else:
            print("Dieses Format wird nicht unterstützt")

    else:
        print("Titel konnte nicht gefunden werden")
        songselection()


selection = songselection()