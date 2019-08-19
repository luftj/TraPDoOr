import csv

result = []
headerline = ""
with open('data/baugenehmigungen.csv','r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in spamreader:
        if(len(row) < 8):
            continue
        
        fssplit = row[7].split("|")

        fssplit = [i.lstrip('0') for i in fssplit] # strip leading zeroes
        fssplit = list(set(fssplit)) # remove duplicates

        for fs in fssplit: # flurstuecke
            newrow = row.copy()
            newrow[7] = fs[:]

            gmsplitl = row[8].split("|")
            gmsplit = list(set(gmsplitl))   # remove duplicates
            for gm in gmsplit: # gemarkungen
                newnewrow = newrow.copy()
                newnewrow[8] = gm[:]

                result.append(newnewrow)

with open('data/baugenehmigungen_split.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_ALL)

    for row in result:
        spamwriter.writerow(row)