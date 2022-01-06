import csv
from hashlib import sha256
d = dict()
list = []
for i in range(0 , 9999):
    m =sha256(b'%i' % i).hexdigest()
    #print(m)
    d[m] = i
    #print(d)
    list.append([i , m])
#print(list)
with open('file address' , 'w' , newline = '') as outfile:
        writer = csv.writer(outfile)
        for item in list:
            writer.writerow(item)
with open('file address' , 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[0]
        hash = row[1]
        for key in d:
            if key == hash:
                print(name , d[key])