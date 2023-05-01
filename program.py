import json
from datetime import datetime

dzimsanas_dienas = {}


class DzDienas():

  def addBD():

    with open('dzimsanas_dienas.json', 'r') as f:
        dzimsanas_dienas = json.load(f)
        
    name = input("Ievadiet vārdu: ")
    date_str = input("Ievadiet dzimšanas dienu (DD/MM/YYYY): ")
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        dzimsanas_dienas[name] = date.strftime("%d/%m/%Y")
        with open('dzimsanas_dienas.json', 'w') as f:
            json.dump(dzimsanas_dienas, f, indent=4)
            print("Updated birthdays:", dzimsanas_dienas)
    except ValueError:
        print("Nepareizs datuma formāts")
    

    DzDienas.chooseAction()



  def deleteBD():
    with open('dzimsanas_dienas.json', 'r') as f:
        dzimsanas_dienas = json.load(f)

    name = input("Ievadiet vārdu, kura dzimšanas dienu vēlaties dzēst: ")
    if name in dzimsanas_dienas:
        del dzimsanas_dienas[name]
        with open('dzimsanas_dienas.json', 'w') as f:
            json.dump(dzimsanas_dienas, f, indent=4)
            print(f"Dzimšanas diena veiksmīgi dzēsta: {name}")
    else:
        print(f"Nav saglabātas dzimšanas dienas priekš {name}")

 
    DzDienas.chooseAction()



  def editBD():
    with open('dzimsanas_dienas.json', 'r') as f:
        dzimsanas_dienas = json.load(f)

    name = input("Ievadiet vārdu, kura dzimšanas dienu vēlaties labot: ")
    if name in dzimsanas_dienas:
        date_str = input("Ievadiet jauno dzimšanas dienu (DD/MM/YYYY): ")
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y").date()
            dzimsanas_dienas[name] = date.strftime("%d/%m/%Y")
            with open('dzimsanas_dienas.json', 'w') as f:
                json.dump(dzimsanas_dienas, f, indent=4)
                print(f"Dzimšanas diena veiksmīgi labota: {name}: {date.strftime('%d.%m.%Y')}")
        except ValueError:
            print("Nepareizs datuma formāts")
    else:
        print(f"Nav saglabātas dzimšanas dienas priekš {name}")
   

    DzDienas.chooseAction()



  def showBD():
    with open('dzimsanas_dienas.json', 'r') as f:
        dzimsanas_dienas = json.load(f)
        
    if not dzimsanas_dienas:
        print("Nav saglabātu dzimšanas dienu")
    else:
        print("Saglabātās dzimšanas dienas:")
        for name, date_str in dzimsanas_dienas.items():
            date = datetime.strptime(date_str, "%d/%m/%Y").date()
            print(f"{name}: {date.strftime('%d.%m.%Y')}")

    
    DzDienas.chooseAction()




  def chooseAction():
    choice = input(
      "Izvēlaties funkciju: \n1. Ievadīt Dzimšanas dienu \n2. Dzēst Dzimšanas dienu \n3. Rediģēt dzimšanas dienas \n4. Parādīt dzimšanas dienas\n"
    )
    #pāraude
    if choice.isdigit() == False:
      print("Ievadiet ciparu\n")
      DzDienas.chooseAction()

    elif int(choice) > 4:
      print("Nav tāda funkcija. \n")
      DzDienas.chooseAction()
    #pārbaudes beigas

    if int(choice) == 1:
        DzDienas.addBD()

    elif int(choice) == 2:
        DzDienas.deleteBD()

    elif int(choice) == 3:
        DzDienas.editBD()

    elif int(choice) == 4:
        DzDienas.showBD()


DzDienas.chooseAction()
