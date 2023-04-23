# # Part 1
# a =5
# b =0

# try:
#     print("Open")
#     print(a/b)
# except Exception as e:
#     print("Hey, you can not divide a number by zero:", e)
# finally:
#     print("close")
# # Finally block will excute at any condition doesn't matter whether we get
# # an error or not

# Part 2
a =5
b =2

try:
    print("open")
    print(a/b)
    k = int(input("enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("you can not divide a number by zero:", e)
except ValueError:
    print("Invalid input")
except Exception as e:
    print("something is wrong", e)
finally:
    print("close")