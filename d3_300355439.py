#nom: Samuel Prevost
#numero d'etudiant: 300355439

#Q1 (list) -> int
'''nombre de chiffres superieur de 100'''
def compte100(x):
    num = 0
    for pos in range(0, len(x), 1):
        if (x[pos] > 100):
            num += 1
    print(num)
    return num

compte100([1,102,-3.5, 104]) #2
compte100([1,99,-3.5,-7]) #0
compte100([]) #0


#Q2 (list) -> int
'''somme des elements pairs d'une liste'''
def sommeListeDiv2(x):
    somme = 0
    for pos in range(0, len(x), 1):
        if (x[pos] % 2 == 0):
            somme += x[pos]
    print(somme)
    return somme

sommeListeDiv2([1,4,3,8,5]) #12
sommeListeDiv2([]) #0 
sommeListeDiv2([4,-10,7]) #-6

#Q3 (str) -> bool
'''true si 3 char. consecutifs, false si non'''
def triples(x):
    for pos in range(0, len(x)-2, 1):
        check1 = x[pos] 
        check2 = x[pos+1]  
        check3 = x[pos+2]
        if (check1 == check2) and (check2 == check3):
            print(True)
            return True
    print(False)    
    return False

triples("abc") #False
triples("abbbcdeeggggg") #True
triples("abc2eee") #True
triples("a23xxxxx") #True
triples("abaacd") #False

#Q4 (str) -> str
"prend un string et dit combien de fois une lettre ce repete (ex: 'bbcggggeeeeebb' -> 'b2c1g4e5b2')"
def momo(x):
    nouv = ""
    i = 0
    while (i<len(x)):
        j=0
        for k in range(i, len(x), 1):
            if x[i] == x[k]:
                k += 1
                j +=1
            else:
                break
        nouv = nouv + x[k-1] + str(j)
        i = k
        k += 1   
    print(nouv)
    return

momo("a") #'a1'
momo("aabbbccccx") #'a2b3c4x1'
momo("aaa1111") #'a314'
momo("aaabcaax") #'a3b1c1a2x1'


#Q5 (str) -> str
"enleve les char. qui sont dupliquer"
def noDup(x):
    nouv = ""
    i = 0
    while (i<len(x)):
        for k in range(i, len(x), 1):
            if x[i] == x[k]:
                k += 1
            else:
                break
        nouv = nouv + x[k-1] 
        i = k
        k += 1   
    print(nouv)
    return

noDup("a") #'a'
noDup("aabbbccccx") #'abcx'
noDup("aaa1111") #'a1'
noDup("aaabcaax") #'abcax'