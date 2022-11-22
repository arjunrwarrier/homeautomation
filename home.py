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
        temperature = input("Enther the temperature: ")
        humidity = input("Enter the humidity: ")
        moisture = input("Enter the moisture: ")
        #date = input("Enter the date: ")

        sql = "INSERT INTO `sensorvalues`(`temperature`, `humidity`, `moisture`, `date`) VALUES (%s,%s,%s,now())"
        data = (temperature,humidity,moisture)
        mycursor.execute(sql,data)
        mydb.commit()

    elif(choice ==2):
        print("View all values")
        sql = "SELECT `temperature`, `humidity`, `moisture`, `date` FROM `sensorvalues` "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)


    elif(choice == 3):
        print("Search a value")
        date = input("Enter the date: ")
        sql = "SELECT `temperature`, `humidity`, `moisture` FROM `sensorvalues` WHERE `date`= '"+date+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        break