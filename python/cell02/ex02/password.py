#!/usr/bin/env python3

password = "Python is awesome"

entered_password = input("Please enter the password: ").strip()

if entered_password == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")