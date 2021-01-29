#Christopher Seven
#DU ID - 873571051
#This program takes in a file, or multiple files, as well as the flags -c, -z, and -l to then count the frequency of each letter appearing in said file(s).

import sys
import string

def add_frequencies(d, file, remove_case):
    #This function is accessed through the main() function, and simply serves to count the frequency of each letter in a text file. It takes in 3 arguments, a dictionary, file name, and a boolean.
    f = open(file, "r")
    a = {}
    #An empty dictionary which then counts the frequency of letters.

    if remove_case is False:
    #Essentially, if False, then we create a key for each letter, irregardless of case.
        for line in f:
            for letter in line:
                if letter.isupper() or letter.islower():
                    if letter in a:
                        a[letter] += 1
                    else:
                        a[letter] = 1
        for key in d:
        #This code then updates a with the dictionary that was inputted as d.
            if key in a:
                a[key] += d[key]
            else:
                a[key] = d[key]
    elif remove_case is True:
    #Here, we only wish to count letters, not create separate keys for upper and lowercase.
        for line in f:
            for letter in line:
                if letter.islower():
                    if letter in a:
                        a[letter] += 1
                    else:
                        a[letter] = 1
                elif letter.isupper():
                    if letter.lower() in a:
                        a[letter.lower()] += 1
                    else:
                        a[letter.lower()] = 1
        for key in d:
            keylower = key.lower()
            if keylower in a:
                a[keylower] += d[key]
            else:
                a[keylower] = d[keylower]
    return(a)

def main():
    d = {}
    remove_case = True
    #The base outcome is then that we only have 1 key for each letter, which is modified by the -c flag.

    vals = []
    #This is how the flags and file names are put into a list.
    for val in sys.argv:
        vals.append(val)

    valscopy = vals.copy()
    #To restrict the list of flags to only include the file names, a copy is first made. The flags are then individually removed from the list, until only the file names remain.
    valscopy.pop(0)
    if "-c" in valscopy:
        cindex = valscopy.index("-c")
        valscopy.pop(cindex)
    if "-l" in valscopy:
        lindex = valscopy.index('-l')
        valscopy.pop(lindex + 1)
        valscopy.pop(lindex)
    if "-z" in valscopy:
        zindex = valscopy.index('-z')
        valscopy.pop(zindex)


    if "-c" in vals:
    #If the -c flag is present, then we know that we want to create a separate key for each letter, upper and lower case, thus changing the boolean to False.
        remove_case = False

    for file in valscopy:
    #This is how multiple files are read in to the function, and where the counting occurrs.
        d.update(add_frequencies(d, file, remove_case))

    if "-z" in vals:
    #This flag then creates a key for each letter of the alphabet that is not present in the dictionary and assigns it a value of 0.
        for letter in string.ascii_lowercase:
            if letter not in d:
                d[letter] = 0

    if "-l" in vals:
    #This flag will restrict our dictionary keys to only include the characters immediately after the -l flag.
        lindex = vals.index("-l")
        charindex = lindex + 1
        alphabet = string.ascii_lowercase
        for letter in alphabet:
            if letter not in vals[charindex]:
                if letter in d.keys():
                    d.pop(letter)

    for k, v in d.items():
        print(f'{k},', v)

main()


