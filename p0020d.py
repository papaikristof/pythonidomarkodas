import random
 
szám = 999 
kísérlet = 0
 
while szám % 2 != 0:
    kísérlet += 1
    szám = random.randint(1, 100)
    print('A(z) ', kísérlet, '. dobás eredménye: ', szám, '.', sep='')
 
print('A(z) ', kísérlet, '. dobás járt eredménnyel.', sep='')
