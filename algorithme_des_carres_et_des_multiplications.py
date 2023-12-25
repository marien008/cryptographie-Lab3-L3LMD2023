
#auteur marien manima-----

try:

    print("Entrer les entiers svp")

    x=int(input("entrer la valeur de x\n"))
    b=str(format(int(input("entrer la valeur de b\n")),'0b'))
    n=int(input("entrer la valeur de n\n"))
    print("b en binaire:",b)

    etape=[]

    #calcul

    for i in range(len(b)):
        if(i==0):
            etape.append([0,2,0,n,x])
        else:
            if(b[i]=="1"):
                etape.append([etape[i-1][4],2,x,n,((etape[i-1][4]**2)*x)%n])
            else:
                etape.append([etape[i - 1][4], 2, 0, n, (etape[i - 1][4] ** 2) % n])



    #affichage
    for i in range(len(etape)):
        if(i!=0):
            if(etape[i][2]==0):
                print(etape[i][0],"^",2,"mod",n,"=",etape[i][4])
            else:
                print(etape[i][0], "^", 2,"x",x, "mod", n, "=", etape[i][4])
        else:
            print(x)


    print("le résultat est :",etape[len(etape)-1][4])
except:
    print("il y a une erreur lors de la saisie des données veillez recommencer et suivez les consignes svp!!!")
