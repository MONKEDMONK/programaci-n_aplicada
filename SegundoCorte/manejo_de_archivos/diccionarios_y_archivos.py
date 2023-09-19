#my_dictionary ={'song': "estrandged","artist":"Guns N roses"}
#print(my_dictionary["song"]) 
#my_dictionary["song"]= "paradaise City"
#print(my_dictionary)   

#without default
#print({"name":"victor"}.get("name"))
#returns "victor"

#without default
#print({"name":"victor"}.get("nickname"))
#returns "none"
#dictionary ={
#1:"hello","two":True,"3":[1,2,3],"four":{"fun":"addition"},5.0:5.5
#}
#print (dictionary)
dict1 ={"color":"blue","Shape":"circle"}
dict2 ={"color":"red", "number":42}

dict1.update(dict2)
#ditc is now ({"color":"bluer","Shape":"circle","number":42}

print(dict1)
