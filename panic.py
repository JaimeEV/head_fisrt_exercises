phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


target = "on tap"
for ch in plist:
    if ch not in target:
        plist.remove(ch)
plist.insert(2," ")
plist.insert(4,"a")
plist.pop(5)
for i in range(3):
    plist.pop()


new_phrase = "".join(plist)
print(plist)
print(new_phrase)