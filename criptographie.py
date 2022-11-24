
x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=''
b=''
y=''
mot3=''
x1=list(x)
cle=input("Veuillez entrer la clé:")
for i in range(26):
    if cle==x1[i]:
        a=x1[i:26]
        b=x1[0:i]
y=a+b
mot= input("Veuillez entrer votre texte:")  
mot=mot.upper()
mot1=list(mot)
for i in range(len(mot)):
    for j in range(26):
        if mot1[i] == x1[j]:
            mot2 = y[j]
            mot3=mot3+mot2            
print(mot3)
        

# x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# a=''
# b=''
# y=''
# mot3=''
# x1=list(x)
# cle=input("Veuillez entrer la clé:")
# cle=cle.upper()

# for i in range(26):
#     if cle==x1[i]:
#         a=x1[i:26]
#         b=x1[0:i]
# y=a+b
# print(y)
# mot= input("Veuillez entrer votre texte:")  
# mot=mot.upper()
# mot1=list(mot)
# for i in range(len(mot)):
#     for j in range(26):
#         if mot1[i] == x1[j]:
#             mot2 = y[j]
#         else :
#             mot2 = mot1[i]  
#         mot3=mot3+mot2
            
# print(mot3)
        


