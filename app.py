def get_decimal_from_user():
    while(True):
        try:            
            num = input("Please enter a number: ")
            num = float(num)
            return num
        except ValueError:
            print("I asked for a number.")
        except:
            print("Something went wrong, sorry.")


num_one = get_decimal_from_user()
num_two = get_decimal_from_user()
added_nums = num_one + num_two
print(added_nums)



# try:
#     num = input("Please enter a number: ")
#     num = int(num)
#     test = 2 + num
#     print(test)
#     choice = input("Please enter your name: ")
#     print("Hello: ", choice)
# except TypeError:
#     print("You can't mix and match types like that!")
# except ValueError:
#     print("Hey, I asked for a number. Play nice.")
# except:
#     print("Something has gone wrong, please try again")
# finally:
#     print("I will run no matter what")





