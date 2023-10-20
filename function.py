# def add():
#     a=10
#     b=20
#     sum=a+b
#     print(sum)
# # add()

# def add(a,b):
   
#     n=a
#     m=b
#     sub=n*m
#     print(sub)
# add(5,6)

    # add()

# def add(a,b):
   
#     n=a
#     m=b
#     sub=n*m
#     return sub
# n=int(input("enter a number"))Untitled Folder 4
# m=int(input("enter the 2nd number"))
# print(add(n,m))

# def solve(s):
#    words = s.split()
# #    print(type(words))

# #    list= []
#    list=''
#    for i in words:
#     #   list.append(i.capitalize())
#     list+=i.capitalize()
#     list+=" "
#    return (list)

# s =input("enter a name :")
# print(solve(s))

# def string():
#     st=""
#     alphabets=set("abcdefghijklmnopqrstuvwxyz")
#     for i in strg:
#         if i in alphabets:
# # x=fruits2.count("grape")
# # print(x)
# mobile=["apple","android","microsoft"]
# bike=["ktm","bajaj","suzuki"]


# print(mobile)
# mobile.insert(1,"blackberry")
# mobile.sort()
# print(mobile)
#             st=st+i
#     return st
# strg=(input("enter "))
# print(string())


# def square():n=68
# for i in range (65,n):
#     for j in range (i,64,-1):
#         print(chr(j),end=" ")
#     print()


#     list=[]
#     list1=[]
#     for i in range(0,4):
#         a=int(input("enter the number  :"))
#         list.append(a)
#     for i in list:
#         i=i**2
#         list1.append(i)
#     print("the square of the list",list1)
# square()



# def square():
#     l=[]
#     c=0
#     for i in range(0,3):
#      n=int(input("enter the number  :"))
#      l.append(n)
# # print(list)
#      for i in l:
#          b=i**2
#          c=c+b
#     print("the sum of squares ",c)    
# square()


# def square():n=68
# for i in range (65,n):
#     for j in range (i,64,-1):
#         print(chr(j),end=" ")
#     print()


#     list=[]
#     n=0
#     for i in range(0,3):
#      a=int(input("enter the number:"))
#      g=a**2
#      n=n+g
#      list.append(n)
# # print(list)
    
#     print("the sum of squares ",n)    
# square()
# def twolist():
#     list1=[]
#     n1=int(input("enter the number of integers in the list one  : "))
#     for i in range(n1):
#         n=int(input( "enter the first list"))
#         list1.append(n)
#     list2=[]
#     n2=int(input("enter the number of integers in list 2  : "))
#     for i in range(n2):
#         n=int(input( "enter the first list"))
#         list2.append(n)
        
#     common=[]
#     for i in range (len(list1)):
#         for j in range(len(list2)):
#                          if((list1[i]==list2[j])):
#                             if list1[i]  not in common:
#                                 common.append(list1[i])
#     return common
# print("common elements are :",twolist())

# def fact():
#     c=1
#     n=int(input("enter the number :"))
#     for i in range (1,n+1):
#      c=c*i
#     print(c)
# fact()


#     return sub
# def prime():
#     n=int((input("enter limit")))

#     for i in range(0,n+1):

#         if i%2!=0 or i==2:
#             if i%3!=0:
#                   print(i)
# prime()
    
    
# def fib():
#     a=int(input("enter the number"))
#     count = 0
#     first = 0
#     second = 1
#     temp = 0
#     while count <= a:
#         print(first)
#         temp = first + secondUntitled Folder 4
#         first = second
#         second = temp
#         count = count + 1
# fib()


# def fun():
#     for i in range (65,68):
#         for j in range (i,64,-1):
#             print(chr(j),end=" ")
#         print()
# fun()



#     return sub
# def fun():
#     for i in range (65,68):
#         for j in range (i,64,-1):
#             print(chr(i),end=" ")
#         print()
# fun()


# def fun():
#     n=70
#     k=65
#     for i in range (65,n):
#         for j in range (65,i+1,1):
#             print(chr(k),end="  ")
#             k=k+1
#         print()
# fun()


# def fun():
#     n=70
#     k=65
#     for i in range (65,n):
#         for j in range (65,i,1):
#             print(chr(j),end="  ")
#             k=k+1
#         print()
# fun()


# def fun():
#     n=70
#     k=65
#     for i in range (65,n):
#         for j in range (65,i+1,1):
#             print(chr(i),end="  ")
#             i=i-1
            
#         print()
# fun()

# def pattern():
#     k=1
#     for i in range(1,8):
#         if i%2==0:
#             for j in range(1,i+1):
#                 print(j,end=" ")
#                 k=k+1
                
#         else:
            
#                 for j in range(0,i):
#                     print("*", end=" ")
                    
#         print()

# pattern()







# n=6
# for i in range(1, n + 1):

#     for j in range(0,i):
#         print("*", end="")
#     print() 
#     if i % 2 == 0:

#         for j in range(1, i + 1):
#             print (j, end="")
#         print()
#     else:

#         for j in range(i, 0, -1):
#             print(j, end="")
# #         print()
# def fibb():

#     b=0
#     f=1
#     n=int(input("enter the number"))
#     for i in range(0,n):
#         if b<=n:
#             print(b)
#             d=b+f
#             b=f
#             f=d
# fibb()

                
                
                
    

# def sum():
#     l=[3,8,12,7,6,10,21,15]

#     total=18
#     for i in l:
#         for j in l :
#             if i+j==total:
#              print("the numbers that give sum 18",i,j)
# sum()

# def number():
#     l=[2,3,4,5,6]
#     for i in l:
#         for j in l:
#             a=i*j
#             b=i+j
#             if a%2==0:
#                print("the numbers which give priduct even are", i,j) 
#             if b%2!=0:
#                 print("the number ehich give sum odd are",i,j)
# number()             


# def words():

#     l=["apple", "banana", "cherry","date" ]

#     for x in l:

#      for y in l: 
#            print(x,y)                
            
# words()






# def number():
#     l=[2,3,4,5,6]
#     print("the numbers which give product even are") 
#     for i in l:
#                for j in l:
#                    a=i*j
#                    if a%2==0:
#                        print(i,j)
#     print("the number which give sum odd are")
#     for i in l:
#                for j in l:
#                     b=i+j       
#                     if b%2!=0:   
#                         print(i,j)
# number()             
 



# def py():
#     n=str(input("enter the string"))
    
    
# def dot(n):
#   return "."..... 
# n=str( input("Enter a word: "))
# print(dot(n))



# print("1.create list\n2.add elements\n3.Replace element\n4.remove elements\n5.exit")
# choice=int(input("enter your choice:"))
# list=[3,2,5,4]
# def create():
#     l=[]
#     for i in range(0,4):
#         n=int(input("enter number="))
#         l.append(n)
#     print('the created list is ',l)
# def add():
#     a=int(input("enter the elemnt:"))
#     list.append(a)
#     print("the new list is",list)
# def replace():
#     replace=int(input("enter position to be replaced="))
#     v=int(input("enter elemnt to be replaced="))
#     list.remove(replace)
#     list.insert(replace,v)
#     print("the new list after replacement =",list)
      
# def remove():
#     Remove=int(input('entr the elment to be removed='))
#     list.remove(Remove)
#     print("the new list after removal is",list)
# # def exit():
# while True:
#     if choice==1:
#         create()
        
#     elif choice==2:
#         add()
        
#     elif choice==3:
#         replace()
#         break
#     elif choice==4:
#         remove()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  2

#     else:
#         print("enter the correct choice")
        




# def python():
#         l=[]
#         n=str(input('enter string='))
#         for i in n:
#                 l.append(i)
#         l.insert(1,".")
#         l.insert(6,".")
#         l[3:5]=["."]
        
#         print("".join(l))
            
# python()


# import random
# l=[2,3,5,7,54,2,9]
# n=random.choice(l)
# # print(n)

# import random
# l=["s","p","r"]
# n=random.choice(l)
# while True:
#     player=str(input(("enter your option=:")))
#     print("computer choice:",n)
#     if(player==n):
        
#         print("tie")
#     elif(player=="r" and n=="s"):
       
#         print("player won")
#     elif(player=="r" and n=="p"):
#         print("computer won").0
#     elif(player=="s"and n=="p"):
#         print("player won")
#     elif(player=="s" and n=="r"):
#         print("computer won")
#     elif(player=="p" and n=="s"):
#         print("computer won")
#     elif(player=="p" and n=="r"):
#         print("player won")
#     elif(player=="quit"):
#         print("game over")
#         break
#     else:
#         print ("incorrect input")
#         quit()



# class bankaccnt():
#     def __init__(self):
#         self.balance=0
        
#         print("welcome to your bank account")
        
#     def deposit(self):
#         deposit=int(input("enter the amount to deposit"))
#         self.balance+=deposit
#         print("deposited amount is " ,deposit,"final balance is ",self.balance)
#     def withdraw(self):
        
#         withdraw=int(input("enter the amount want to withdraw"))
#         self.balance-=withdraw
#     def show(self):
#         print("the availiable balance is",self.balance)
# obj=bankaccnt()
# obj.deposit()
# obj.withdraw()
# obj.show()

# class Bank:
#     def __init__(self):
#         self.customers = {}

#     def create_account(self, account_number, initial_balance=0):
#         if account_number in self.customers:
#             print("Account number already exists.")
#         else:
#             self.customers[account_number] = initial_balance
#             print("Account created successfully.")

#     def make_deposit(self, account_number, amount):
#         if account_number in self.customers:
#             self.customers[account_number] += amount
#             print("Deposit successful.")
#         else:
#             print("Account number does not exist.")

#     def make_withdrawal(self, account_number, amount):
#         if account_number in self.customers:
#             if self.customers[account_number] >= amount:
#                 self.customers[account_number] -= amount
#                 print("Withdrawal successful.")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Account number does not exist.")

#     def check_balance(self, account_number):
#         if account_number in self.customers:
#             balance = self.customers[account_number]
#             print(f"Account balance: {balance}")
#         else:
#             print("Account number does not exist.")

# obj=Bank()
# obj.create_account()
# obj.make_deposit()
# obj.make_withdrawal()
# obj.check_balance() 


class circle():
     def _init_(self):
         self.radius=3
         self.pie=3.14
     def getarea(self):
         area=self.pie*self.radius*self.radius
         print(area)
     def circumference(self):
         circumference=2*self.radius*self.pie
         print(circumference)
obj=circle()
obj.getarea()
obj.circumference()


# class temperature():
#      def _init_(self,faranheit,celcius):
#          self.faranheit=faranheit
#          self.celcius=celcius
#      def calculation(self):
#          F=self.celcius*9/5*32
#          print("celcius to franhiet=",F,"F")
#          C=(self.faranheit-32)*5/9
#          print("faranheit to celcius",C,"C")

# temp=temperature(5,79)
# temp.calculation()    