data={'user':['admin'],
      'acno':[11111],
      'acpass':['admin'],
      'bal':[0],
    'contact':[9898989898]
     }
     #admin#11111#admin#0#9898989898
from getpass import getpass
from random import randint
from os import system

def main():
    try :
        global data
        while True :
            system('cls')
            print()
            print('\t\t    Welcome to Fake Bank of India\n'.center(78))
            x=int(input('\n\n\t\t\t\t\tPress 1 for SignIn\n\n\t\t\t\t\tPress 2 for SignUp\n\n\t\t\t\t\tPress 3 If you are Admin\n\n\t\t\t\t\tPress 4 for exit\n'))
            open_data()
            if   x==1:
                system('cls')
                signin()
                save_data()
            elif x==2 :
                system('cls')
                signUp()
                save_data()
            elif x==3:
                print('\n\n\t\tadmin ji ram ram ')
                print('Your data :=\n',data)
                if input('\n\tPress any key to continue.'):
                    pass
            elif x==4:
                save_data()
                print(' Thankyou for banking with us. '.center(100,'*') )
                return print('\n\n') 
            else:
                print('\n You enter wrong number, Please try again. '.center(100,'*'))
    except Exception as e:
        print('\n You enter wrong number, Please try again later. '.center(100,'*'))

def save_data():
    try:
        global data
        fp = open('bank_program_data.txt','w+')
        data['acno'] = list(map(str,data['acno']))
        data['bal'] = list(map(str,data['bal']))
        data['contact'] = list(map(str,data['contact']))
        x = '+'
        new = []
        for i in data:
            t = x.join(data[i])
            new.append(t)
        x2 = '#'   
        string = x2.join(new)
        fp.write(string)
        fp.close()
    except Exception as e:
        print('\n Something going wrong, Please try again later. '.center(100,'*'))

def open_data():
    try:
        global data
        fp = open('bank_program_data.txt','r')
        c=0
        string = fp.readline()
        l = string.split('#')
        for i in l:
            x = list(data)
            tem = i.split('+')
            data[x[c]]=tem
            c += 1
        data['acno'] = list(map(int,data['acno']))
        data['bal'] = list(map(int,data['bal']))
        data['contact'] = list(map(int,data['contact']))
        fp.close()
    except Exception as e:
        print('\nSomething going wrong, Please try again later.'.center(100,'*'))


def signUp():
    try:
        global data
        print()
        print('\t\tWelcome to Fake Bank of India\n'.center(100))
        while True:
            name=input('\n\n\t\tName     :- ').strip().title()
            c=1
            for i in name:
                if i.isalpha():
                    continue
                elif i.isspace():
                    continue
                else :
                    print("\n\t\t*Invalid Name enter your name again.*")
                    c+=1
                    break
            if c==1:
                break
        while True:
            cont=input('\t\tContact  :- ').strip()
            if (cont.isdigit()) and  (len(cont) == 10):
                break
            else :
                print('\n\t*Invalid contact enter your contact again.*\n')
        cont=int(cont)
        while True:
            pas = getpass("\t\tPassword :-")
            if len(pas)<=6:
                print('\n\t\tPassword incorrect! At least 6 characters are valid')
            else:
                break
        print('\n\t\t* You are successfully registered *')  
        ac=randint(60000,90000)
        bal=0
        print('\n\t\tYour New account number is :- ',ac)
        data['user'].append(name)
        data['acno'].append(ac)
        data['acpass'].append(pas)
        data['bal'].append(bal)
        data['contact'].append(cont)
        print('\n')
        if input('\t\tPress any key to continue.\n'):
            main()
    except Exception as e:
        print('\n\t\tSomething going wrong, Please try again later.')


def signin():
    try:
        global data
                
        print()
        print('\t\tWelcome to Fake Bank of India\n'.center(100))
        print('\n\n\t\tEnter your Account Details.')
        c1=3
        while c1!=0:
            acn=int(input('\n\t\tAccount Number   :- '))
            if acn in data['acno']:
                index=data['acno'].index(acn)
                pas=input('\t\tAccount Password :- ').strip()
                if (data['acno'][index]==acn ) and (data['acpass'][index]==pas ) :
                    main2(index)
                    
                    break    
                else:
                    c1-=1
                    print('\tInvalid account number or password\t\t[ Remaining attempts ',c1,' ]')
            else:
                print('\n\tYou are not Registered.')
                if input('\n\tPress any key to continue.\n'):
                    pass
                break  
    except Exception as e:
        print('\nSomething going wrong, Please try again later.'.center(100,'*'))
    
def main2(index):
    global data
    while True :
        system('cls')
        print()
        print('\t\tWelcome to Fake Bank of India\n'.center(100))
        print('\n\n\t\tAccount Holder Name  :- ',data['user'][index])
        print('\t\tAccount Number       :- ',data['acno'][index])
        print('\t\tAccount Balance      :- ',data['bal'][index])
        print('\t\tContact              :- ',data['contact'][index])
        print('\n\tPress 1 for Deposit\n\tPress 2 for Withdrawal\n\tPress 3 for Balance Enquire\n\tPress 4 for Update account details\n\tPress 5 for Help\n\tPress 6 for SignOut')
        print()
        print('  All Rights Reserved.'.center(100))
        try:
            q=int(input())
            if q==1:
                try:
                    amt=int(input('\tEnter the amount :- '))
                    data['bal'][index]+=amt
                    print('\n\tSuccessfully Added')
                    print('\n\tYour new balance is :-',data['bal'][index])
                    
                except Exception:
                    print('\n\tYou entered Wrong amount. Try again later')
            elif q==2:
                try:
                    amt=int(input('\tEnter the amount :- '))
                    if data['bal'][index]<=amt:
                        print('\n\tYour balance is low .You are not eligible for withdrawal\n')
                    else:
                        data['bal'][index]-=amt
                    print('\n\tYour current balance is :-',data['bal'][index])
                except Exception:
                    print('\n\tYou entered Wrong amount. Try again later')
            elif q==3:
                print('\n\tYour current balance is :-',data['bal'][index])
            elif q==4:
                k=int(input('\n\tPress 1 for change Name\n\tPress 2 for change Password\n\tPress 3 for change Contact\n\tPress 4 for exit\n'))
                if k==1:
                    while True:
                        name=input('\n\n\t\tName     :- ').strip().title()
                        c=1
                        for i in name:
                            if i.isalpha():
                                continue
                            elif i.isspace():
                                continue
                            else :
                                print("\n\t\t*Invalid Name enter your name again.*\n")
                                c+=1
                                break
                        if c==1:
                            break
                    data['user'][index]=name

                elif k==2:
                    password=input('\t\tPassword  :-')
                    data['acpass'][index]=password 

                elif k==3:
                    while True:
                        try:
                            cont=input('\t\tContact  :- ').strip()
                            if (cont.isdigit()) and  (len(cont) == 10):
                                cont=int(cont)
                                break
                            else :
                                print('\n\t*Invalid contact enter your contact again.*\n')
                        except Exception:
                            print('\n\tYou entered Wrong amount. Try again later')
                    
                    data['contact'][index]=cont
                
                elif k==4:
                    
                    pass
                else:
                    print('\t\tyou entered wrong input.')
                print('\n\t\t*Successfully changed.*')

            elif q==5:
                print('\n\tcall on 100 for Help\n')
            elif q==6:
                break
            else :
                print('\n\tYou entered wrong number\n')
            if input('\n\tPress any key to continue.'):
                pass
        except Exception as e:
            print(e)
            print('\n\t\tSomething going wrong .Please try again later.')
    

main()

