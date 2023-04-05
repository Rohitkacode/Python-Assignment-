
doc_txt = open('doc.txt') 
data = doc_txt.read().split(" ")

for i in data:
    if len(i) % 2 == 0:
        open("doc1.txt", "a").write(i+" ")



    
        

