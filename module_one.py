# if __name__ == "__main__"

# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ variable a value of "__main__" if its the initial module being run


if __name__ == "__main__":
    print("running this module directly")
else:
    print("running other module indirectly")

def main():
    print("hello!")

if __name__ == "__main__":
    main()