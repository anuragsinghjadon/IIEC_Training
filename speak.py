import os

print(" 1. run notepad ")
print(" 2. run  Browser ")
print(" 3. run Media Player ")
print(" 4. nothing ")

while(True):
    print("")
    choice = input("what you want to open: ")
    if ((("run" in choice) or ("execute" in choice)) and (("notepad" in choice) or ("editor" in choice))) or (("notepad" in choice) or ("editor" in choice)) :
        print("ruuning notepad........ ")
        os.system("notepad")

    elif ((("run" in choice) or ("execute" in choice)) and (("chrome" in choice) or ("browser" in choice))) or (("chrome" in choice) or ("browser" in choice))  :
        print("runing song.......... ")
        os.system("chrome")
    elif ((("run" in choice) or ("execute" in choice)) and (("media player" in choice) or ("song" in choice)))  or (("media player" in choice) or ("song" in choice)):
        print("ruuning song........ ")
        os.system("start wmplayer")
    else:
        print("thank you for come here....")
        break
        
