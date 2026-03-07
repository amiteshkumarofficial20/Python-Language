info = {
	"name": "apna college",
	"subjects" : ["Python", "C"],
	"topics": ("dictionary", "sets"),
	"subject": {
		"marks" : 94.4,
		"age": 35,
	},
 	"is_adult" : True,
}
print(len(info))
print(info.keys())
print(list(info.keys())) #typecast to list
print(info.values())
print(len(info.values()))
print(info.items())
pairs = list(info.items())
print(pairs)
print(pairs[1])
print(info["name"])
print(info.get("name"))
#print(info["name1"])
print(info.get("name1"))

new_info = {"city": "Delhi"}
info.update(new_info)
print(info)