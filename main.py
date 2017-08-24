def InputProcessor(rawEmails):
    listEmails = []
    tempEmail = ""
    try:
        for x in rawEmails:
            if x == ',':
                listEmails.append(tempEmail)
                tempEmail = ""
            elif x != " ":
                tempEmail += x
    except:
        print("The input was not correct.")

    # Adding last email or first email
    listEmails.append(tempEmail)

    return listEmails    

rawEmails = input("Enter all the emails, separated by a coma: ")
listEmails = InputProcessor(rawEmails)
print("Total raw emails: " + str(len(listEmails)) + "\n")

processedEmails = list(set(listEmails))
print("Total processed emails: " + str(len(processedEmails)) + "\n")

for i in processedEmails:
    if i == processedEmails[-1]:
        print(i, end='\n')
    else:
        print(i, end=', ')
