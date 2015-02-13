with open("hello.txt", "a") as myInput:
    userInput = raw_input("What you did today? "+"\n")
    myInput.writelines(userInput+'\n')
