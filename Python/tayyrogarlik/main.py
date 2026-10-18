# task1
# a = 3
# S=6*a*a
# V=a*a*a
# print("Kubning hajmi:", V)
# print("Kubning sirti yuzi:", S)

# task2
# a = int(input("a = "))
# b = int(input("b = "))

# sum = a + b
# if 30 < sum < 50:
#     print("Ok")
# else:
#     print("Eror")

# task3

# a = int(input("son - a = "))
# n = int(input("daraja - n = "))
# if n > 0:
#     print(a**n)
# else:
#     print("son 0 dan kichik")

# task4
# n = int(input("n = "))
# sum = 0

# while n != 0:
#     sum += n%10
#     n = n//10
    
# print(sum)

# task5
# ball = int(input("Ball: "))

# if 0 <= ball <= 54:
#     print("Baho -", 2)
# elif 55 <= ball <= 70:
#     print("Baho -", 3)
# elif 71 <= ball <= 84:
#     print("Baho -", 4)
# elif 85 <= ball <= 100:
#     print("Baho -", 5)
# else:
#     print("Bunday oraliqda baho mavjid emas")

# task6
# matn = input("Matn: ")
# natija = ""

# for i in matn:
#     if i.isdigit():
#         natija += i
#     else:
#         continue

# print(natija)

# bilet2 task1
# som = int(input("So'm = "))
# dollar = round(som/12800,3)
# print(f"{som} UZS = ${dollar} ")

# task2
# a = int(input("a = "))
# b = int(input("b = "))

# if a>5 and b <=10:
#     print("a 5 dan katta va b 10 dan kichik yoki teng")
# else:
#     print("a 5 dan katta emas yoki b 10 dan kichik yoki teng emas")
    
# task3
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# if a == b == c:
#     print("=")
# else:
#     print(max(a, b, c))  

# task4
# n = int(input("n = "))
# kopaytma = 1

# while n != 0:
#     kopaytma *= n%10
#     n = n//10
    
# print("Ko'paytma:", kopaytma)

# task5
# soz = "kitob va dori"
# a = 'a'
# b = 'b'
# d = 'd'

# soz = soz.replace(b, 'd')
# soz = soz.replace(a, 'b')

# print(soz)

# task6
# sonlar = []
# for i in range(100):
#     if i%10 + i//10 <10:
#         sonlar.append(i)
# print(sonlar)

# 3 - bilet task1
# santimetr = int(input("Santimetr: "))
# metr = round(santimetr/100, 3)
# print("Metr:", metr)

# task2
# yosh = int(input("Yosh: "))
# yosh10 = yosh//10
# yosh1 = yosh%10

# match yosh10:
#     case 1: print("O'n", end=" ")
#     case 2: print("Yigirma", end=" ")
#     case 3: print("O'ttiz", end=" ")
#     case 4: print("Qirq", end=" ")
#     case 5: print("Ellik", end=" ")
#     case 6: print("Oltmish", end=" ")
#     case 7: print("Yetmish", end=" ")
#     case 8: print("Sakson", end=" ")
#     case 9: print("To'qson", end=" ")
    
# match yosh1:
#     case 1: print("bir")
#     case 2: print("ikki")
#     case 3: print("uch")
#     case 4: print("to'rt")
#     case 5: print("besh")
#     case 6: print("olti")
#     case 7: print("yetti")
#     case 8: print("sakkiz")
#     case 9: print("to'qqiz")

# task3
# for i in range(1,100,2):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i, end=", ")

# task4
# n = int(input("n = "))
# juft = 0
# toq = 0

# while n != 0:
#     if (n % 10)%2 == 0:
#         juft += 1
#     else:
#         toq += 1
#     n = n//10
    
# print(f"{juft} ta juft son va {toq} ta toq son ")

# task5
# matn = input("Matn: ")
# digit_sum = 0
# for i in matn:
#     if i.isdigit(): 
#         digit_sum += int(i)
    
# print(digit_sum)
    
# task6
# matn = input("Matn: ")
# digit_sum = 0
# str_sum = 0
# for i in matn:
#     if i.isdigit(): 
#         digit_sum += 1
#     elif isinstance(i, str):
#         str_sum += 1
               
# if digit_sum == str_sum:
#     print("Ok")
# else:
#     print("Error")

# 4 - bilet task1
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# average = round((a + b + c)/3, 3)
# print(average)

# task2
# n = int(input("n = "))

# b = n % 10
# o = n // 10 % 10
# y = n // 100
# num = b*100 + o*10 + y*1
# print("Teskari:",num)

# task3
# n = int(input("Oy raqamini kiriting: "))

# match n:
#     case 1 | 2 | 12: print("Qish")
#     case 3 | 4 | 5: print("Bahor")
#     case 6 | 7 | 8: print("Yoz")
#     case 9 | 10 | 11: print("Kuz")
#     case _: print("Bunday ma'lumot mavjud emas")

# task4
# for i in range(10, 100):
#     if (i//10 + i%10) == 9 or (i//10 + i%10) == 15:
#         print(i, end=",")

# task5
# n = int(input("n = "))
# count = 0
# while n != 0:
#     if (n%10)%2== 1:
#         count += 1
        
#     n = n//10
    
# if count == 0:
#     print("True")
# else:
#     print("False")

# task6
# matn = input("matn: ")
# str4 = ""
# for i in matn :
#     if i.isalpha():
#         str4 += i

# print(str4[:4])
        

        
    




    
    
    


    
    
      

