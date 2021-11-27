# # Searching for specific word in the file, with repetition
# print(f.readline())
# fLine = f.readline() #reading the first line
# print(fLine)
f = open("C:/Users/EJ/PycharmProjects/pythonProject1/demo1.txt", "r") #file in read mode
print("The content starts as: ", end="")
print("\"" + f.read(25) + "...\"")

txt = f.read() #reading the whole file content

def askRepeat():
    decide = input("Do you want to search again? (y/n): ")
    if decide == "y":
        repeatIt()
    elif decide == "n":
        stopIt()
    else:
        print("Please input 'y' or 'n' only")
        askRepeat()

def repeatIt():
    global r
    r = 1
    searchContent()

def stopIt():
    print("Thank you for using the program.")

def searchContent():
    r = 1 #r for repeat
    while r == 1:
        findWord = input("Enter your search word (case sensitive): ")
        if findWord in txt:
            print()
            print("We found the word " + "\"" + findWord + "\"" + " in the file.")
            askRepeat()
            break
        else:
            print()
            print("We can\'t find " + "\"" + findWord + "\"" + " in the file.")
            askRepeat()
            break

def askSearch():
    decide = input("Do you want to search the content? (y/n): ")
    if decide == "y":
        searchContent()
    elif decide == "n":
        stopIt()
    else:
        print("Please input 'y' or 'n' only")
        askSearch()

askSearch()


