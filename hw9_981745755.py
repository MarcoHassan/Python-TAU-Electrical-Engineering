import os

''' Exercise #5. Python for Engineers.'''
''' Name:    Marco Hassan	      '''
''' ID:      981745755 	              '''

# Set working directory
path = "/home/mhassan/Scrivania/TAU - Python/Homeworks/HW_9"
os.chdir(path)


#########################################
# Question 1 - do not delete this comment
#########################################
def sum_nums(file):
    with open(file, "r") as in_file:
        aiuto = in_file.read()
        if aiuto.endswith("\n"):
            aiuto = aiuto[:-1]
        aiuto = aiuto.split(' ')
        summing = 0
        for i in aiuto:
            summing += int(i)
    return summing

#########################################
# Question 2 - do not delete this comment
#########################################


def get_x_freqs(infile, outfile, x):
    in_file = open(infile, "r")
    dic = {}
    length = 0
    for line in in_file:
        if line.endswith("\n"):
            line = line[:-1]
        line2 = line.replace(" ", "")
        length += len(line2)
        for word in line.split():
            dic[word] = dic.get(word, 0) + 1
    if length == 0:
        raise ValueError(f'Invalid name')
    in_file.close()
    out_file = open(outfile, "w")
    for w in sorted(dic.keys(), key=dic.get, reverse=True)[:x]:
        out_file.write(w + " " + str(dic[w]) + "\n")
    out_file.close()

#########################################
# Question 3 - do not delete this comment
#########################################


def decode(in_file, out_file):
    try:
        infile = open(in_file, "r")
        a = ""
        for line in infile:
            for word in line:
                if ord(word.lower()) in range(98, 123):
                    ascII = ord(word)
                    new_letter = chr(ascII - 1)
                elif ord(word.lower()) == 97:
                    ascII = ord(word)
                    new_letter = chr(ascII + 25)
                else:
                    new_letter = word
                a += new_letter
        outfile = open(out_file, "w")
        outfile.write(a)
        infile.close()
        outfile.close()

    except IOError:
        if 'a' in locals():
            print("Can't decipher", out_file, "due to IOError")
            infile.close()
        else:
            print("Can't decipher", in_file, "due to IOError")


#########################################
# Question 4 - do not delete this comment
#########################################


def process_contacts(contacts_file):
    try:
        dizio = {}
        infile = open(contacts_file, "r")
        for line in infile:
            if line.strip().startswith('#'):
                continue
            elif line.count(',,') > 0 or len(line.split(',')) != 4:
                raise ValueError(f'Invalid input file')
            else:
                if line.endswith('\n'):
                    line = line[:-1]
                aiuto = line.split(',')
                if aiuto[3] not in dizio:
                    dizio[aiuto[3]] = ''
                if aiuto[1] not in dizio[aiuto[3]]:
                    if dizio[aiuto[3]] == '':
                        dizio[aiuto[3]] = aiuto[1]
                    else:
                        dizio[aiuto[3]] += ", " + aiuto[1]

        for i in dizio.items():
            dizio[i[0]] = list(i[1].split(','))

        infile.close()

    except IOError:
        print('Cannot decipher the input file due to an IOError')
        # I do not close the file as due to the error
        # it was never opened at first. Is that wrong?

    finally:
        return dizio
