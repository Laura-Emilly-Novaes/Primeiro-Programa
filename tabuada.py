#print ("===============\n")
#print ("Programa de Tabuadas\n") #título do programa
#num = int ( input ("Digite quantas tabuadas você quer: ")) #recebe a quantidade, o int transforma de texto pra número inteiro, input guarda na var
#for j in range (1, num+1): #repetidor/contagem_ multiplicando - escolhe a tabuada da vez
#    print ("Tabuada do", j ) #mostrar qual tabuada está sendo feita
#    for i in range (11): #multiplicador=quanti que vai ser repetido ou somado; 1
#        print (j, "x", i, "=", j*i) #mostra tudo na tela
#    print (" ") #linha em branco





print ("===============\n")
print ("Programa de Tabuada \n") #vai aparecer na tela
num = int ( input ("Digite qual tabuada você quer: ")) #recebe o multiplicando
for i in range (11): #ele faz a multiplicação daquela tabuada
        print (num, "x", i, "=", num*i) #organização de aparecer na tela
print (" ")
print ("===============\n")

#(j) é o número da tubuada
#(i) o multiplicador
#(j*i) o resultado
