s = "la méthode split est parfois bien utile"
tab = "la méthode split est parfois bien utile"

tab = s.split(" ")
print(tab)
tab = s.split("e")
print(tab)
#tab = s.split("")
#print(tab)

tab = "".join(tab)
print(tab)
tab = " ".join(tab)
print(tab)
tab = " tralala ".join(tab)
print(tab)
tab = "\n".join(tab)
#print(tab)
#print("".join([1,2]))

nombre = [8,20,6,4]
#print(tab.sort())
print(nombre.sort())
nombre = nombre.sort()
print(nombre)
t = list("tino leon")
t = t.sort()
print(t)
print([8,9])