import time

# While true:
while True:
    option = input("1 to enter country or 2 to exit\n")
    if option == '1':
        country = input("enter country\n")
        with open("country_input.txt", "w+") as f:
            f.write(country)
            f.close()
        time.sleep(5)
        with open("country_output.txt", "r+") as f:
            capital = f.read()
            f.close()
            print(capital)
        f.close()
    elif option == "2":
        exit()
    else:
        print("unknown option")
