class Marrige:

    def __init__(self, dulhan_name="", dulha_name="", marrige_budget="", marrige_of_address="", sound_system=""):
        self.dulhan_name = dulhan_name
        self.dulha_name = dulha_name
        self.marrige_budget = marrige_budget
        self.marrige_of_address = marrige_of_address
        self.sound_system = sound_system

        s = open("marriage.txt", "a+")

        s.write( "\nDulhan name: {0}\nDulha name: {1}\nMarrige_bajet : {2}\n"
                "Address : {3}\nSound_System : {4}".
                format(self.dulhan_name, self.dulha_name, self.marrige_budget, self.marrige_of_address,
                       self.sound_system))
        s.close()

def Display():
    f = open("marriage.txt", "r")
    print(f.read())
    f.close()

    k = open("marriage12.txt","r")
    print(k.read())
    k.close()

while True:

    print("1.Add_record\n2.Search_record\n3.Food_Item\n4.Display_Record")
    choice = int(input("ENTER YOUR CHOICE : "))

    if choice == 1:
        Dulhan_name = input("Enter your Dulhan`s name : ")
        Dulha_name = input("Enter your Dulha`s name : ")
        Budget = int(input("Enter budget : "))
        Address = input("Enter address : ")
        sound_system = input("Enter name of sound system : ")
        mrg1 = Marrige(Dulhan_name, Dulha_name, str(Budget) , Address, sound_system)

    if choice == 2:

        SE = input("please enter to search : ")
        search_file = open("marriage.txt", "r")
        check_file = search_file.readlines()
        search_file.close()

        for line in check_file:
            try:
                if line.split()[2] == SE:
                    print(" Found ")
                else:
                    continue
            except IndexError:
                pass

    if choice == 3:
        print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
        CHOICE = int(input("Enter your choice : "))

        if CHOICE == 1:
            GujratiFood = input("Enter gujrati item :")
            A =open("marriage12.txt","a")
            A.write("\nGujrati Food : " + GujratiFood)
            A.close()

        elif CHOICE == 2:
            PanjabiFood = input("Enter panjabi item :")
            B = open("marriage12.txt", "a")
            B.write("\nPanjabi Food : " + PanjabiFood)
            B.close()

        elif CHOICE == 3:
            ChineseFood = input("Enter Chinese item :")
            C = open("marriage12.txt", "a")
            C.write("\nChinese Food : " + ChineseFood)
            C.close()

        elif CHOICE == 4:
            JapaneseFood = input("Enter Japanese item :")
            D = open("marriage12.txt", "a")
            D.write("\nJapanese Food : " + JapaneseFood)
            D.close()

    if choice == 4:
        Display()
