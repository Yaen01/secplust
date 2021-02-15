#Imports json package
import json

#Imports json file called scores.json
with open("scores.json") as f:
    data = json.load(f)



#Function responsible for inserting new results to the database
def write():
    #Grabs the chapter number
    testNum = int(input("Type chapter number for the test: "))
    print("")

    #Checks if the chapter number is within normal range
    if (testNum >= 1 and testNum <= 29):
        testScore = int(input("Type score achieved for the test: "))
        print("")

        if (len(data["test" + str(testNum)])!= 0):
            testLen = str(len(data["test" + str(testNum)]) + 1)

        else:
            testLen = '1'

        #Checks if the test score number is within normal range
        if (testScore >= 1 and testScore <= 100):

            testDate = input("Type the date the test was taken (MM/DD/YYYY): ")

            data['test'+str(testNum)][testLen]={}

            data['test'+str(testNum)][testLen]['score']= testScore

            data['test'+str(testNum)][testLen]['date']= testDate

            print("")
            print("Data Validated: Chapter: " + str(testNum) + " Score: " + str(testScore))
            print("")

            #export data to json
            with open('scores.json', 'w') as outFile:
                json.dump(data, outFile, indent=2)
            outFile.close()

        #If the parameters above where not met the function is restarted
        else:
            print("Error: Invalid Input Restarting Program")
            write() 

    #If the parameters above where not met the function is restarted
    else:
        print("Error: Invalid Input Restarting Program")
        write()



#Function responsible for displaying results from the database
def read():
    #Determines whether all results will be pulled or just one test
    readAll = input("Type (Y) if you want to see all results or (N) if not: ")
    print("")

    #Logical proccess to get all results pulled
    if (readAll == "y" or readAll == "Y"):

        #For loop that goes through all the test chapters
        for x in range(1, len(data)):

            if (len(data["test" + str(x)]) > 0):
                print("     Chapter " + str(x) + " Test Results")
                print("     ----------------------")
                print("")

                #For loop that goes through every individual result per chapter
                for y in range(1, len(data["test" + str(x)])+1):
                    print("     Score: " + str(data["test" + str(x)][str(y)]["score"]))
                    print("     Date: " + str(data["test" + str(x)][str(y)]["date"]))
                    print("")
                    print("")

    #Proccess to grab all results for one individual test
    elif (readAll == "n" or readAll == "N"):
        #Grabs the chapter that will be pulled
        readNum = int(input("Type the number of the chapter you want results for: "))
        print("")
        print("     Chapter " + str(readNum) + " Test Results")
        print("     ----------------------")
        print("")

        #For loop that goes through every individual result for the chapter
        for x in range(1, len(data["test" + str(readNum)])):
            print(" Score: " + str(data["test" + str(readNum)][str(x)]["score"]))
            print(" Date: " + str(data["test" + str(readNum)][str(x)]["date"]))
            print("")
            print("")

    #If the parameters above where not met the function is restarted
    else:
        print("Error: Invalid Input Restarting")
        read()


#Function responsible for starting the program
def main():
    print("")
    print("     Security+ Test Results Database Initiated")
    print("     -----------------------------------------")
    print("")
    #Determines whether results will be inputed or outputed
    testActivity = input("Type (W) to Write Test Results or (R) to Read Test Results: ")
    print("")

    #Calls the write function if w or W is entered
    if (testActivity == "w" or testActivity == "W"):
        write()

    #Calls the read function if r or R is entered
    elif (testActivity == "r" or testActivity == "R"):
        read()

    #Terminates the program if exit or EXIT are entered
    elif (testActivity == "exit" or testActivity == "EXIT"):
        return()

    #If the parameters above where not met the function is restarted
    else:
        print("Error: Invalid Input Restarting Program")
        main() 

main()