test = "ABCBCA"
a = []
    
for x in test:
    if x in a:
        print(x)
        break
    else:
        a.append(x)
