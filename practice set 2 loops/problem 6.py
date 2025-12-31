password="1234"
Enter_password=int(input("Enter the password:"))

while(Enter_password != password):
    Enter_password=input("Wrogn password! Try again and enter password:")
print("Success!You are logged in")
