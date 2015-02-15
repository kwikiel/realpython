import time

current_time = time.strftime("%d.%m.%y %H:%M ", time.localtime())
with open("hello.txt", "a") as myInput:
    userInput = raw_input("What you did today? "+"\n")
    myInput.writelines(current_time + userInput+'\n')
