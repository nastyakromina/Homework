a = float(input ('Введите a:'))
b = float(input ('Введите b:'))
c = float(input ('Введите c:'))
U1 = U4 = False
if a * b == c:
    U1 = True
    print ('Выполняется условие 1')
if a * c + b == 0:
    U4 = True
    print ('Выполняется условие 4')
if U1 and U4:
    print ('Выполняются условия 1 и 4')
else:
    if U1 == False and U4 == False:
        {
            print ('НЕ выполняется ни одно из условий 1 или 4')
        }
print ('Для завешения нажмите ENTER')
ENTER = input('')        
 


    
