import re, sys
file = sys.argv[1]
def insert_Line_Breaks():    
    with open(file,"a+") as file_Object:
        for line in file_Object:
            write_Object = open(file,"w")
            write_Object.write("\n".join(re.findall("(?s).{,94}", line))[:-1])
        file_Object.close()
        write_Object.close()
def remove_Line_Breaks():
    no_Breaks = open(file,"a+").read().replace("\n","")
    open(file,"w").write(no_Breaks)
def menu():
    user_Choice = input("Menu:\n1. Add breaks to ACH file.\n2. Remove breaks from ACH file.\n3. Quit.\nChoose an option: ")
    if user_Choice == 1:
        insert_Line_Breaks()
        menu()
    elif user_Choice == 2:
        remove_Line_Breaks()
        menu()
menu()
