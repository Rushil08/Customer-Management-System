import pickle
u=open('user','ab')
for i in range(1):    #enter number of users you want to add in the parentheses
    l=[]
    a=input('enter username: ')
    b=input('enter password: ')
    l.extend([a,b])
    pickle.dump(l,u)
    print('User Added')
u.close()
