my_dictionary ={'song': "estrandged","artist":"Guns N roses"}
print(my_dictionary["song"]) 
my_dictionary["song"]= "paradaise City"
print(my_dictionary)   

#without default
print({"name":"victor"}.get("name"))
#returns "victor"

#without default
print({"name":"victor"}.get("nickname"))
#returns "none"
dictionary ={
1:"hello","two":True,"3":[1,2,3],"four":{"fun":"addition"},5.0:5.5}
print (dictionary)
dict1 ={"color":"blue","Shape":"circle"}
dict2 ={"color":"red", "number":42}

dict1.update(dict2)
#ditc1 is now ({"color":"blue","Shape":"circle","number":42}

print(dict1)

ex_dict ={"a":"anteater","b":"bumblebee","c":"cheetah"}

print (ex_dict.keys())
print(ex_dict.values())
print(ex_dict.items())


with open ('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)


with open ('how_many_lines.txt') as cool_dos_file:
    cool_dos_file.write("air Buddy/n")       

with open ('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()

    print(setup)
    print(punchline)
  
with open ('how_many_lines.txt') as file1:
    setup = file1.readline()
    punchline = file1.readline()
    print(setup)
    print(punchline)
    print(file1.readline())
