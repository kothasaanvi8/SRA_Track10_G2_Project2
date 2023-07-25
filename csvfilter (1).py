import csv

with open("data.csv", newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';')
    with open("Edited ODIR Dataset.csv", 'w', newline = '') as newcsvfile:
        writer = csv.writer(newcsvfile, delimiter = ';')
        for r in reader:
            row = r[0].split(",")
            print(row)
            for i in range(0, len(row)-2):
                if(row[i][-3:] == "jpg" and row[i-1][-3:] == "jpg"):
                    leftdiseaselist = [row[i-1]]
                    rowleft = row[i + 1].split("，")
                    for disease in rowleft:
                        if(disease.find("non proliferative") != -1):
                            disease = disease.replace("non proliferative", "nonproliferative")
                        if(((disease.find("retinopathy") != -1) and (disease.find("hypertensive") != -1 or disease.find("proliferative") != -1 or disease.find("nonproliferative") != -1)) or disease.find("normal fundus") != -1):
                            leftdiseaselist.append(disease)
                            print(leftdiseaselist)
                    if len(leftdiseaselist) > 1:
                        writer.writerow([leftdiseaselist])
                    rightdiseaselist = [row[i]]
                    rowright = row[i + 2].split("，")
                    for disease in rowright:
                        if(disease.find("non proliferative") != -1):
                            disease = disease.replace("non proliferative", "nonproliferative")
                        if(((disease.find("retinopathy") != -1) and (disease.find("hypertensive") != -1 or disease.find("proliferative") != -1 or disease.find("nonproliferative") != -1)) or disease.find("normal fundus") != -1):
                            rightdiseaselist.append(disease)
                            print(rightdiseaselist)
                    if len(rightdiseaselist) > 1:
                        writer.writerow([rightdiseaselist])
                #print(row[i+1]+","+row[i+2]);
            
        
                #if(row[i].substr(row[i].length()-3, ))
    
