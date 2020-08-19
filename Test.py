from tkinter import *

tkWindow = Tk()
tkWindow.geometry('500x200')
tkWindow.title('Cazare')

Nume_Client = input("Numele dumneavoastra: ")
def sayhi(Client):
    print("Bine ati venit " + Nume_Client + "!")

sayhi(Nume_Client)

clientLabel = Label (tkWindow, text = 'Client') .grid(row=0, column=0)
client = StringVar()
clientEntry = Entry(tkWindow, textvariable= client) .grid(row=0, column=1)

Client = 1
camere = True
capacitate = 50
camere_duble = 2
camere_triple = 3
raspuns_negativ = 'nu'
raspuns_pozitiv = 'da'

def AlegereCamera:
 while camere == True:
    Client = input("Cate persoane sunteti? ")
    if int(Client) >= 1 and int(Client) <= 50:
        camere_duble = (input("Doriti camera dubla? "))
        if camere_duble == raspuns_negativ:
            if int(Client) >= 3:
                print('Avem si camere triple.')
            else:
                print('Ne cerem scuze dar nu avem camere single!')
            if int(Client) >= 3:
                camere_triple = (input('Cate camere triple doriti? '))
                if int(camere_triple) <= 10:
                    print('Desigur! Poftiti, va rog!')
                else:
                    print('Nu dispunem de acest numar.')
        else:
            print('Poftiti,va rog!')


        camere = int(Client)
    else:
        print('Avem doar 20 de camere.')


