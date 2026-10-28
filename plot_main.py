from plot_fxns import *

#import plot_fxns.py
#from plot_fxns.py import *

#data = [4,5,8,3,6,5,6,7,6,9,1,4,5,6,7,6,5,6,6,7]
#word = 'brontosaurus and tyrannosaurus and aptosaurus'

#diction = count_occur(word)

#plot_bar(diction)

#plot_hist(data)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short-1.txt"
    
d = dict()
fh = open(fname)
counta = 0
countb = 0
countc = 0
for line in fh:
    words = line.split()  
    if len(words) == 0:
        continue
    first_word = words[0]  
    if first_word == 'From:':
        d['From:']  = d.get('From:',0) + 1
        counta += 1
    elif first_word == 'From':
        d['From']  = d.get('From',0) + 1
        countb += 1
    else :
        d['other'] = d.get('other',0) + 1
        countc += 1

for key, val in d.items():
    print("There are", val, "counts of ", key, "in the file.")

plot_bar(d,"Frequency of starting word")

