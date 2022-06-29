from pyfiglet import Figlet
import qrcode

def load():
  print("LOADING...")
  myfile=open("datas.txt","r")
  data=myfile.read().split("\n")  

  for i in range(len(data)):
      products_info = data[i].split(",")
      PRODUCTS.append({'id':int(products_info[0]) , 
                       "name" : products_info[1] ,
                       "price" :float(products_info[2]),
                       "count" :int(products_info[3])})  
  print(" welcome ")

PRODUCTS=[]

def Add_new_product():
  id=int(input("please type id new product : "))
  name=(input("please type name new product : "))
  price=float(input("please type price new product : "))
  count=int(input("please type count new product : "))
  PRODUCTS.append({"id":id,"name":name,"price":price,"count":count})
  print(PRODUCTS)
  print(" new product added successfully")


def Show_all():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i]["id"],"\t",PRODUCTS[i]["name"],"\t",PRODUCTS[i]["price"],"\t",PRODUCTS[i]["count"])  

def show_Edit_product():
    print("1.name")
    print("2.price")
    print("3.count")
    print("4.exit")

def Edit_product():
    id=int(input("please type id product : "))

    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]["id"]== id:
          while True:
            show_Edit_product()
            select = int(input(" please select a number of menu : "))
            if select == 1:
                PRODUCTS[i]["name"]=input("please type rename product : ")
            elif select ==2:
                PRODUCTS[i]["price"]=float(input("please type reprice product : "))
            elif select == 3:
                PRODUCTS[i]["count"]=int(input("please type recount product : "))
            elif select ==4:
                break  
            else:
                print("Your selection is not defined!")

def Delete_product():
    id=int(input("please type  id for delete product : "))

    for i in range(len(PRODUCTS)):
      if PRODUCTS [i] ["id"]==id:
          PRODUCTS.pop(i)
          print("removed product")
          break

def Search_product():
    User_input= input(" please type id or name product for search : ")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]["name"]==User_input or str(PRODUCTS[i]["id"])==User_input:
            print(PRODUCTS[i])
        else:
            print(" not foand !") 

def Show_Qrcode_product():
    idqr=input('Enter id kala for qrcode:')
    for i in range(len(PRODUCTS)):
        if idqr==PRODUCTS[i]['id']:
          myqr=qrcode.make(PRODUCTS[i])
          myqr.save(f'qrcode{i}.png')
          print('QrCode product created')

def Buy_of_store():
    Cart=[]
    while True:
      id = int (input("please type id product : "))
      for i in range(len(PRODUCTS)):
          if PRODUCTS[i]["id"]==id:
              count= int(input("please type the count : "))

              if PRODUCTS[i]["count"]>= count:
                  Cart.append({"name":PRODUCTS[i]["name"],
                              "price":PRODUCTS[i]["price"],
                              "count":count})
                  PRODUCTS[i]["count"] -= count
                  print("the product added cart")
              else:
                  print("not exit!")
      select=input("Do you still want to continue?    ( y/n)")     
      if select=="n" or select=="N":
        break

      print( Cart )               
      Total_price = 0 
      for i in range(len(Cart)):
          Total_price += Cart[i]["price"] * Cart[i]["count"]         
      print("Total_price :", Total_price)
      print("thanks for your shopping :)")

def Exit_of_store():
    f=open("datas.txt","w")
    for i in range(len(PRODUCTS)):
        data=str(PRODUCTS[i]["id"])+","+PRODUCTS[i]["name"]+","+str(PRODUCTS[i]["price"])+","+str(PRODUCTS[i]["count"])+"\n"
        f.write(data)
    f.close()
    exit()

    

def show_menu():
  print("1.Add new product : ") 
  print("2.Edit product :")
  print("3.Delete product : ") 
  print("4.Search product : ") 
  print("5.Show all : ") 
  print("6.Buy of store  : ") 
  print("7.product qrcod")
  print("8.Exit of store : ") 

load()
f=Figlet(font="standard")
print(f.renderText("Shopping  center"))

while True:
  show_menu()
  select=int(input("please select a number : "))
  if select==1:
    Add_new_product()
  elif select==2:
    Edit_product()
  elif select==3:
    Delete_product()
  elif select==4:
    Search_product()
  elif select==5:
    Show_all() 
  elif select==6:
    Buy_of_store()
  elif select==7:
    Show_Qrcode_product()
  elif select==8:
    Exit_of_store()