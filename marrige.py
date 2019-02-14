import sys

class Marrige:

    def __init__(self,dulhan_name,dulha_name,marrige_bajet,marrige_of_address,sound_system):
        self.dulhan_name = dulhan_name
        self.dulha_name = dulha_name
        self.marrige_bajet = marrige_bajet
        self.marrige_of_address = marrige_of_address
        self.sound_system = sound_system



        s = open("marriage.txt","a+")

        s.write("\nDulhan name: {0}\n Dulha name: {1}\n Marrige_bajet : {2}\n"
                " Address : {3}\n Sound_System : {4}".
                format(self.dulhan_name,self.dulha_name,self.marrige_bajet,self.marrige_of_address,self.sound_system))
        s.close()

def Display():

    f = open("marriage.txt", "r")
    print(f.read())
    f.close()


while True:

    print("1.Add_record\n2.Search_record\n3.Display_Record")
    choice = int(input("ENTER YOUR CHOICE : "))

    if choice == 1:
        Dulhan_name = input("Enter your Dulhan`s name : ")
        Dulha_name = input("Enter your Dulha`s name : ")
        Budget = int(input("Enter budget : "))
        Address = input("Enter address : ")
        sound_system = input("Enter name of sound system : ")
        mrg1 = Marrige(Dulhan_name, Dulha_name, Budget, Address, sound_system)


    if  choice == 2:


        SE = input("please enter to search : ")

        search_file = open("marriage.txt","r")
        check_file = search_file.readlines()
        search_file.close()

        for line in check_file:
            if line.split()[2] == SE:
                print("found !!!")
                break

    if choice == 3:
        Display()









