
# simple open and close
st = open("st.txt","w")
st.write("Hi from Python!")
st.close()

# with-statement open, write, and close
with open("st2.txt","w") as f:
    f.write("Hello using a with-statement from Python!")

# reading file contents
with open("st2.txt","r") as f:
    print(f.read())

# save file contents in list to use later
my_list = []
with open("st.txt","r") as f:
    my_list.append(f.read())
print(my_list)


import csv
# writing to csv file
# open in excel after writing

my_first_list = ['one','two','three']
my_second_list = ['four','five','six']

with open("st4.txt","w",newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(my_first_list)
    w.writerow(my_second_list)
    f.close()

new_list = []

with open("st4.txt","r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        new_list.append(",".join(row))
    print(new_list)
    f.close()



