f = open('C:\\Guna\\Training\\Data Science\\Python\\VS Code\\Data\\input.txt', 'r')
print (f)
for line in f:
    print (line.rstrip())
f.close()