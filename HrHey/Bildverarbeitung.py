# 32 x 32 Pixel
#Bilder als zwei dimensionale Arrays
#Bilder werden im Arbeitsspeicher häufig als zwei dimensionale Arrays abgelegt.
#Für jeden Bildpunkt (Pixel) benötigen wir bei Farbbildern 8-Bit-Werte (RGB für Red, Green, Blue),
#bei Graubildern 1 Byte für die Graustufen und für Schwarz-Weiß-Bilder(z.B. QR-Codes) ein Bit.

#Übung 1

# Legen Sie sich ein Array für Graubilder mit 32x32 Bildpunkten an und füllen Sie jeden Bildpunkt zufällig.
import random
count = 0
random.seed()
pixelx = [[] * 4] *4
pixely = [[] * 4] *4

while count < len(pixelx):
    pixelx[count].append(random.randint(0,255))
    pixely[count].append(random.randint(0,255))
    count = count+1

bild = [pixelx, pixely]

def spiegeln():
    global pixelx, pixely
    for i in range(0-1,len(pixelx)-1):
        spiegel = pixelx[0].pop()
        pixelx[0].insert(i,spiegel)
        print(pixelx)

spiegeln()

#Wie ändert sich Ihr Quelltext für einen QR-Code mit 128*128 Informationen? Wiviel MiB können Sie in dem QR-Code speichern?

pixelx2 = [] * 128
pixely2 = [] * 128

for i in range(0,128 + 1):
    pixelx2.append(random.randint(0,1))
    pixely2.append(random.randint(0,1))

bild2 = [pixelx2, pixely2]

print(bild2)