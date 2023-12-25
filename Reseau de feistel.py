#!/usr/bin/python3

#auteur marien manima-----



def ou(text1,text2):
    result=""
    for i in range(len(text1)):
        if (text1[i]=="0" and text2[i]=="0"):
            result += "0"
        else:
            result += "1"
    return result


#------------------------------------------

def xor(text1,text2):
    result=""
    for i in range (len(text1)):
        if(text1[i]!=text2[i]):
            result+="1"
        else:
            result+="0"
    return result

#------------------------------------------------------
def et(text1,text2):
    result=""
    for i in range (len(text1)):
        if(text1[i]=="1" and text2[i]=="1"):
            result+="1"
        else:
            result+="0"
    return result
    
#------------------------------------------------------------
def decalage(valeur, orientation,ordre):
    resultat=[]
    if(orientation=="l"):
        resultat=valeur[ordre:]+valeur[:ordre]
    else:
        resultat=valeur[len(valeur)-ordre:]+valeur[:len(valeur)-ordre]
    return resultat
            
    #-----------------------------------------------------------
def split(chaine):
    p1=""
    p2=""
    for x in range(len(chaine)):
        if(x<=(len(chaine)/2)-1):
            p1=p1+chaine[x]
        else:
            p2=p2+chaine[x]
    return [p2,p1]
    
#--------------------------------------------------------
def permutationInverse(bits,model):
    resultat=[]
    for i in range(len(model)):
        resultat.append(model.index(str(i)))
    return "".join(permutation(bits,resultat))

 #----------------------------------------------
def permutation (bits,model):
    valeurpermuter=[]
    for i in range(len(bits)):
        valeurpermuter.append(bits[int(model[i])])
    return valeurpermuter


#----------------------------------------

def veriBinaire(chaine):
    test=0
    for i in chaine:
        if((i!="0" and i!="1")or(len(chaine)!=8)):
           test=1

    if(test==1):
        raise ValueError()




try:

    # commencement de l'algorithme de génération de clé
    fonction_permuGe = "65274130"
    fonction_permu = "46027315"
    fonction_permu2 = "2013"

    print("nombre des bits autorisés 8 pas plus pas moins")
    k = input("Entrer la clé en binaire \n")
    veriBinaire(k)


    n1=int(input("le decalage à gauche de la prémiere paire de clé sera d'ordre combien?\n"))
    n2=int(input("le decalage à droite de la deuxième paire de clé sera d'ordre combien?\n"))

    k=permutation (k,fonction_permuGe)

    k1p,k2p=split (k)[1], split (k)[0]

    k1,k2=xor(k1p,k2p),et(k1p,k2p)

    k1,k2=decalage(k1,"l",n1),decalage(k2,"r",n2)

    print("Les clés sont:(",k1,",",k2,")")




    #algo de chiffrement----------------

    N=input("entrer le message en binaire")
    N=permutation(N,fonction_permu)
    veriBinaire(N)

    #decoupage
    G0,D0=split(N)[1],split(N)[0]

    #calcule de round1
    D1,G1=xor(permutation(G0,fonction_permu2),k1),xor(D0,ou(G0,k1))

    #calcule de round 2
    D2,G2=xor(permutation(G1,fonction_permu2),k2),xor(D1,ou(G1,k2))

    #combinage
    c=G2+D2
    print(c,"combine")

    #mesage crypté
    c=permutationInverse(c,fonction_permu)
    print("message crypté :",c)

#---------------------------------------------------------------------------------------------------------

    #algo de dechiffrement--------------------------

    #message crypté déjà connue

    #la permutation

    c=permutation(c,fonction_permu)
    #decoupage
    G2,D2=split(c)[1],split(c)[0]

    #round 1
    G1,D1=permutationInverse(xor(D2,k2),"2013"),xor(G2,ou(G1,k2))

    #round 2
    G0,D0=permutationInverse(xor(D1,k1),"2013"),xor(G1,ou(G0,k1))

    N=G0+D0
    N=permutationInverse(N,fonction_permu)

    print("message decrypter:",N)
except:
    print("il y a une erreur lors de la saisie des données veillez recommencer et suivez les consignes svp!!!")




    