import random

nomeUtente = str(input("Qual è il tuo nome? "))
nomeBot = str(input("Qual è invece il nome del bot avversario? "))
print("")
print("Bene, quindi oggi si sfideranno: ", nomeUtente, "vs", nomeBot, "in una lotta fra campioni!!")
print("")
pedinaUtente = str(input("Quale sarà la tua pedina? X oppure O: "))
while(pedinaUtente != "X" and pedinaUtente != "O"):
    pedinaUtente = str(input("Scegli una figura tra queste due: X oppure O "))
pedinaBot = " "

if(pedinaUtente == "X"):
    pedinaBot = "O"
else:
    pedinaBot = "X"

print("")
print("La pedina scelta da", nomeUtente, " è ", pedinaUtente)
print("")
print("La pedina che di conseguenza ha", nomeBot, " è ", pedinaBot)



caselleUsate = 0
turnoPlayer = True
seeTable = True
botDeveMuovere = True


n1 = "1"
n2 = "2"
n3 = "3"
n4 = "4"
n5 = "5"
n6 = "6"
n7 = "7"
n8 = "8"
n9 = "9"


print("")
print("")
print(" ",n1,"  | ",n2,"  | ",n3,"  ")
print("___________________")
print("")
print(" ",n4,"  | ",n5,"  | ",n6,"  ")
print("___________________")
print("")
print(" ",n7,"  | ",n8,"  | ",n9,"  ")
print("")
print("")

while(caselleUsate < 9):
    #TURNO DEL PLAYER
    turnoPlayer = True
    seeTable = True

    while(turnoPlayer):
        print("")
        print("Il numero che sceglierai sarà la posizione della tua prossima mossa, scegli con cura:")
        rispostaUtente = str(input())

        if(rispostaUtente == "1"):
            if(n1 != pedinaUtente and n1 != pedinaBot):
                n1 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "2"):
            if(n2 != pedinaUtente and n2 != pedinaBot):
                n2 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "3"):
            if(n3 != pedinaUtente and n3 != pedinaBot):
                n3 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "4"):
            if(n4 != pedinaUtente and n4 != pedinaBot):
                n4 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "5"):
            if(n5 != pedinaUtente and n5 != pedinaBot):
                n5 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "6"):
            if(n6 != pedinaUtente and n6 != pedinaBot):
                n6 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "7"):
            if(n7 != pedinaUtente and n7 != pedinaBot):
                n7 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "8"):
            if(n8 != pedinaUtente and n8 != pedinaBot):
                n8 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False

        elif(rispostaUtente == "9"):
            if(n9 != pedinaUtente and n9 != pedinaBot):
                n9 = pedinaUtente
                caselleUsate += 1
                turnoPlayer = False
            else:
                print("Dammi una casella libera")
                seeTable = False
        else:
            print("Dammi una risposta valida! ")
            seeTable = False

        if(seeTable):
            print("")
            print("")
            print(" ",n1,"  | ",n2,"  | ",n3,"  ")
            print("___________________")
            print("")
            print(" ",n4,"  | ",n5,"  | ",n6,"  ")
            print("___________________")
            print("")
            print(" ",n7,"  | ",n8,"  | ",n9,"  ")
            print("")
            print("")


        if((n1 == n2 and n2 == n3) or (n4 == n5 and n5 == n6) or (n7 == n8 and n8 == n9) or (n1 == n4 and n4 == n7) or (n2 == n5 and n5 == n8) or (n3 == n6 and n6 == n9) or (n1 == n5 and n5 == n9) or (n3 == n5 and n5 == n7)):
            caselleUsate += 100
            print("") #questa casella è semplicemente per fare spazio tra il luogo di gioco e la frase della vittoria
            print("ABBIAMO UN VINCITORE: ", str.upper(nomeUtente), "!!")
            print("")
            print("Mi spiace", nomeBot, "ma non puoi competere con ", nomeUtente)

    #se le caselle usate sono minori di 9 il bot fa la sua mossa, sennò il programma finisce
    if(caselleUsate < 9):

        #TURNO DEL BOT


        mossaBot = random.randint(1,9)
        mossaBot = str(mossaBot)

        turnoBot = True
        seeTable = True


        while(turnoBot):
            if(mossaBot == "1"):
                if(n1 != pedinaBot and n1 != pedinaUtente):
                    print("La mossa del bot è ", mossaBot)
                    n1 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;


            elif(mossaBot == "2"):
                if(n2 != pedinaUtente and n2 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n2 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "3"):
                if(n3 != pedinaUtente and n3 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n3 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "4"):
                if(n4 != pedinaUtente and n4 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n4 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "5"):
                if(n5 != pedinaUtente and n5 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n5 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "6"):
                if(n6 != pedinaUtente and n6 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n6 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "7"):
                if(n7 != pedinaUtente and n7 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n7 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "8"):
                if(n8 != pedinaUtente and n8 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n8 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;

            elif(mossaBot == "9"):
                if(n9 != pedinaUtente and n9 != pedinaBot):
                    print("La mossa del bot è ", mossaBot)
                    n9 = pedinaBot
                    caselleUsate += 1
                    turnoBot = False
                else:
                    mossaBot = random.randint(1,9)
                    mossaBot = str(mossaBot)
                    turnoPlayer = False;


            if(seeTable):
                print("")
                print("")
                print(" ",n1,"  | ",n2,"  | ",n3,"  ")
                print("___________________")
                print("")
                print(" ",n4,"  | ",n5,"  | ",n6,"  ")
                print("___________________")
                print("")
                print(" ",n7,"  | ",n8,"  | ",n9,"  ")
                print("")
                print("")

        if((n1 == n2 and n2 == n3) or (n4 == n5 and n5 == n6) or (n7 == n8 and n8 == n9) or (n1 == n4 and n4 == n7) or (n2 == n5 and n5 == n8) or (n3 == n6 and n6 == n9) or (n1 == n5 and n5 == n9) or (n3 == n5 and n5 == n7)):
            caselleUsate += 100
            print("")
            print("ABBIAMO UN VINCITORE: ", str.upper(nomeBot), "!!")
            print("")
            print("Mi spiace", nomeUtente, "ma non puoi competere con ", nomeBot)

#finisce il while(caselleUsate < 9):
