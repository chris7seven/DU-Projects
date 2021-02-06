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

def flags(vals):
    #This function takes in the argument vals as its input, where vals is the list that contains all flags. Then, the function flags iterates through each flag and modifies the dictionary, then returns it.
    d = {}
    remove_case = True

    if "-c" in vals:
        remove_case = False

    for file in vals:
        if file.endswith('.txt'):
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
    return d

def main():
    #Main here simply creates the list vals based on the flags input with the code, and then calls flags(vals) to display the  resulting dictionary.
    vals = []
    for val in sys.argv:
        vals.append(val)
    print(flags(vals))

if __name__ == "__main__":
    main()
