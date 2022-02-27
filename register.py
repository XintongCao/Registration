#define a username-list and a pwdlist
usernamelist=list()
pwdlist=list()
#define a file and read all the lines in this file
with open('./user1.txt','a+',encoding='utf-8') as fp:
    fp.seek(0) #change the position of cursor to the front of this file
    res=fp.readlines()
    for i in res:
        pieces=i.strip() #remove all the \n from the pieces
        r=pieces.split(':') #seperate username and pwd
        usernamelist.append(r[0])
        pwdlist.append(r[1])

#define a function
def register():
    #define a loop for checking the username
    site=True
    while site:
        #input a username
        username=input('Please enter a username: ')
        #check if the username has existed
        if username in usernamelist:
            print('This username has been used, please enter a new one ')
        else:
            #define a loop for checking the pwd
            while True:
                #input a first pwd
                pwd=input('Please enter a password: ')
                #check the length of this pwd
                if len(pwd)>=3:
                    #enter a second pwd
                    repwd=input('Please enter this password again: ')
                    #check if these two pwds are the same
                    if pwd==repwd:
                        #if these two pwds are the same, then store the usernames and pwds into the file defined above
                        with open('./user1.txt','a+',encoding='utf-8') as fp:
                            fp.write(f'{username}:{pwd}\n')
                        #this register has finished
                        print(f'This register has finished! Username:{username}')
                        #the username has been stored, so the username loop can stop here
                        site=False
                        #two pwds are the same, username and pwd has been stored in the file, so this pwd loop can stop here
                        break
                    else:
                        #if two pwds are different, then write pwd again
                        print('The two passwords are different, please enter again.')
                #if the length of this pwd doesnt match
                else:
                    print('The length of this password is not correct, please enter again.')

register()
