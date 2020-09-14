import time
import random

#define variable------------
option="yes"
dict={}
list1=[]
list2=[]
clock1=time.strftime("%d/%m/%Y",time.localtime(time.time()))
clock2=time.strftime("%r",time.localtime(time.time()))
clock3=time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))

print('      \||/','     ..........  .......   .      .  .  ..........')
print('      \||/','     |           |      \  |      |  |       |')
print('    .<><><>.','   .......     ......./  |      |  |       |')
print('   .<><><><>.','  |           |   \     |      |  |       |')
print('   .<><><><>.','  |           |    \    |      |  |       |')
print('    .<><><>.','   |           |     \   \....../  |       |')
print('  ')
print('                                              ******************Billing System*************')
print('  ')
print('                  \VM/','       ........  |       |     ......     ..........')
print('                 .o0000o.','   /          |       |    /      \    |         \ ')
print('                0000000000','  \........  |.......|   |        |   ........../')
print('                 .o0000o.','            \ |       |   \        /   |')
print('                  .o00o.','     ......../ |       |     ......     |')

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(clock1+"\t\t\t"+"Welcome to fruit Biling System"+"\t\t"+clock2)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(' ')

#Bill creation
def bill():
  generate_bill='yes'
  while generate_bill in ("yes","y","Y","Yes"):
    print(' ')
    print("Bill No.",random.randint(0,200),"\t\t\t",clock3)
    print('****************************************************')
    print(' ')
    selectitem=input("Do you want to create a bill for all items?")
    print(' ')
    if selectitem in ("yes","y","Y","Yes"):
            i=0
            sumtotal=0
            for i in range(len(list1)):
                    item=list1[i]
                    Rate=list2[i]
                    print('item:',item)
                    Qty = int(input("Enter quantity: "))
                    print(' ')
                    Amount= (Rate * Qty)
                    print(' ')
                    print("item",'\t\t',"Rate",'\t\t',"Qty",'\t\t',"Amount")
                    print(item,'\t\t',Rate,'\t\t',Qty,'\t\t',Amount)
                    print('\t\t\t\t','------------------------------')
                    print('\t\t\t\t',"Total Amount: ",Amount,"Rs.")
                    sumtotal=Amount+sumtotal
            i=i+1
            print('\t\t\t\t','----------------------------')
            print('\t\t\t\t','Total Price of all Items: ',sumtotal,'Rs.')
            print(' ')
    elif selectitem in ("no","n" ,"N","No"):
            item=input("Enter item for bill :")
            Rate=dict.get(item, "No data found")
            Qty = int(input("Enter Quantity: "))
            print(' ')
            Amount= (Rate *Qty)
            print(' ')
            print("item",'\t\t',"Rate",'\t\t',"Qty",'\t\t',"Amount")
            print(item,'\t\t',Rate,'\t\t',Qty,'\t\t',Amount)
            print('\t\t\t\t','----------------------------')
            print('\t\t\t\t',"Total Amount: ",Amount,"Rs.")
            print(" ")
    else:
            print("Sorry, Your answer is not valid.Please create a bill by more bills option.")
    Bill_again=input("Do you want to create more bills?")
    if Bill_again in ("yes","y" ,"Y","Yes"):
            generate_bill="yes"
    elif Bill_again in ("no","n" ,"N","No"):
           break  
    else:
        print("Sorry, Your answer is not valid but we drop you at bill creation page")
       

#Item adding options:
while option in ("yes","y" ,"Y","Yes"):
    print("Selection options:")
    print("1.Show Item")
    print("2.Add item")
    print("3.Exit")
    choice=input("choose a valid option : ") #which is 1,2
    print(' ')
    if choice =='1':
        if len(dict.keys()) == 0:
            print("Nothing to show...choose a valid option")
            print(' ')
            continue
            options = 'yes'
        else:
            print(' ')
            print("item",'\t\t',"Rate")
            print('----------------------')
            i=0
            for i in range(len(list1)):
                    item=list1[i]
                    Rate=list2[i]
                    print(item,'\t\t',Rate)
            print(' ')
            generate_bill= input("Do you want to generate bill?")
            print(' ')
            if generate_bill in ("yes","y" ,"Y","Yes"):
                bill()
            elif generate_bill in ("no","n" ,"N","no"):
                options='yes'
            else:
                print("Sorry, Your answer is not valid. please create a bill by choosing a valid option.")


    elif choice =='2':
         item = input("Enter item name (max 14 character): ").strip()
         Rate = int(input("Enter Rate: "))
         dict[item]=item
         list1.append(item)
         list2.append(Rate)
         print("Item Added")
         print(' ')
         generate_bill= input("Do you want to generate bill?")
         print(' ')
         if generate_bill in ("yes","y" ,"Y","Yes"):
             bill()
         elif generate_bill in ("no","n" ,"N","No"):
                 options='yes'
         else:
             print(" Sorry, Your answer is not valid. Please create a bill by choosing a valid option.")



    elif choice == '3':
          print("thank you for using this app.")
          options='yes'
          

                          
                    
                
      
