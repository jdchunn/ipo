inp = input("Enter String") # Obtain User Input

print("Input Entered")
print("=============================================================")
print(inp)
print("^^^^=====================================================^^^^")

######## DO NOT EDIT ABOVE THIS LINE #####################################################

res = len(inp.split())

print("Words:"+ str(res))
print("Characters:", len(inp))

counted=0
for i in inp:
    if i.isdigit():
        counted+=1
print("Numbers:", counted)







######## DO NOT EDIT BELOW THIS LINE #####################################################
