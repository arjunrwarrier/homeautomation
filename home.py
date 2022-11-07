import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password='',database = 'homeautomationdb')

mycursor = mydb.cursor()

while True:
    print("\nSelect an option")
    print("1. Add values")
    print("2. View all values")
    print("3. Search values using date")
    print("4. Exit")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("Enter the values")
    elif(choice ==2):
        print("View all values")
    elif(choice == 3):
        print("Search a value")
    elif(choice==4):
        break