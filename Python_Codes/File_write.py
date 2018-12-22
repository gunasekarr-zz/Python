f = open('C:\\Guna\\Training\\Data Science\\Python\\VS Code\\data\\input.txt', 'r')
output = open('C:\\Guna\\Training\\Data Science\\Python\\VS Code\\data\\output.txt', 'w')
for line in f:
    output.write(line.rstrip() + '\\n')
f.close()