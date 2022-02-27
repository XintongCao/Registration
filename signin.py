#define a usernamelist, a pwdlist and a blocklist
usernamelist=list()
pwdlist=list()
blocklist=list()
#create a file
with open('./user1.txt','a+',encoding='utf-8') as fp:
    #move the file's cursor to the front
    fp.seek(0)
    #read all the lines in this file
    res=fp.readlines()
    for i in res:
        r=i.strip() #remove all the \n for each lines
        arr=r.split(':') #divide username and pwd
        #append all the divided usernames and pwds into two different lists
        usernamelist.append(arr[0])
        pwdlist.append(arr[1])
#get all the usernames in the blocklist
with open('./block.txt','a+',encoding='utf-8') as fp:
    fp.seek(0)
    res=fp.readlines()
    for i in res:
        r=i.strip()
        blocklist.append(r)

#define a function
def login():
    #create a loop to check username
    islogin=True
    #define the error times
    errornum=3
    while islogin:
        #enter a username
        username=input('Welcome! To log in, please enter a username: ')
        #check if this entered username has been existed
        if username in usernamelist:
            #check if this entered username is in blocklist
            if username in blocklist:
                print('This entered username has been blocked, please wait for help!')
            else:
            #create a loop to check the pwd
                while True:
                    #enter pwd
                    pwd=input('Please enter your password: ')
                    #get the index of the entered username in the usernamelist
                    inx=usernamelist.index(username)
                    #check if the entered pwd and the pwd associated with the index of the username
                    if pwd==pwdlist[inx]:
                        print('Welcome to log in!')
                        #the loop of islogin can stop here
                        islogin=False
                        #the loop of checking the pwd can stop here
                        break
                    else:
                        #if the two pwd are different,then the error num will be minued 1
                        errornum=errornum-1
                        #check if the current errornum is still bigger than 1
                        if errornum==0:
                            print('Your account has been blocked, please try it later.')
                            #create a blocklist file and write the blocked usernames in this file
                            with open('./block.txt','a+',encoding='utf-8') as fp:
                                fp.write(username+'\n')
                                #the loop of islogin can stop here
                            islogin=False
                            #the loop of checking the pwd here can stop
                            break
                        else:
                            print(f'The entered password is not correct, you still can try {errornum} times, please enter again: ')

        else:
            #the entered username is new, need to finish the register first
            print('The entered username is new, please enter again.')


login()
