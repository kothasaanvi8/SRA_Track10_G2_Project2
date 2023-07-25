from PIL import Image
import csv
import numpy as np

with open("Edited ODIR Dataset.csv", newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';')
    for r in reader:
        row  = r[0].split(",")
        if(".jpg" in row[0]):
            file = row[0]
            try:
                print(row)
                image = Image.open("ODIR-5K/ODIR-5K/Training Images/" + file)
                arrimage = np.array(image)
                width = image.width
                height = image.height
                leftbound = -1
                upbound = -1
                colored = False
                for rows in arrimage:
                    upbound += 1
                    for colors in rows:
                        for color in colors:
                            color = int(color)
                            if color > 0:
                                colored = True
                                break
                        if colored:
                            break
                    if colored:
                        break
                colored = False
                for colnum in range(0, width):
                    edgeloc = int(height/2) - 1
                    leftbound += 1
                    colors = arrimage[edgeloc][colnum]
                    for color in colors:
                        try:
                            color = int(color)
                        except:
                            color = color
                        if color > 1:
                            colored = True
                            print("tru")
                            break
                    if colored:
                        break
                image = image.crop((leftbound, upbound, width - leftbound, height - upbound))
                image = image.resize((512, 512))
                for i in range(1, len(row)):
                    if row[i] != '':
                        image.save("NewTrainingData/" + row[i] + "/" + file)
            except:
                print("Error.")
                image = Image.open("ODIR-5K/ODIR-5K/Testing Images/" + file)
                for i in range(1, len(row)):
                    if row[i] != '':    
                        image.save("NewTestingData/" + row[i] + "/" + file)