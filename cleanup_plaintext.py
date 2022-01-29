with open('old_plaintext.txt', 'r') as infile, \
        open('plaintext.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("'", "")
    data = data.replace('"', "")
    data = data.replace("♪", "")
    data = data.replace(" ", "")
    data = data.replace("\n", "")
    data = data.replace("©", "")
    data = data.replace("Ã", "")
    data = data.replace("¤", "")
    outfile.write(data)


with open('plaintext.txt', 'r') as file:
    data = file.read().replace('\n', '')
