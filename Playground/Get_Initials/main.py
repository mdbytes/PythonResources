def main():
    name = get_name()
    initials = convert_name(name)
    display(name,initials)

def get_name():
    return input("What is the name we will be converting?")

def convert_name(name):
    initials = ""
    name_list = name.split(" ")
    for s in name_list:
        initials += s[0] + "."
    return  initials

def display(name,initials):
    print("Name: ",name)
    print("Initials: ",initials)

main()