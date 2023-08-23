insulinFile = open("preproinsulin-seq.txt")
insulinText = insulinFile.read()

removeOrigin=insulinText.replace("ORIGIN", "")
removeSlash=removeOrigin.replace("//", "")
removeNewline=removeSlash.replace("\n", "")
noSpace=removeNewline.replace(" ","")
cleanFile = ''.join([i for i in noSpace if not i.isdigit()])

with open("preproinsulin-seq-clean.txt", "w") as preproinsulin:
    preproinsulin.write(cleanFile)

with open("lsinsulin-seq-clean.txt", "w") as lsinsulin:
    lsinsulin.write(cleanFile[0:24])
    
with open("binsulin-seq-clean.txt", "w") as binsulin:
    binsulin.write(cleanFile[24:54])
    
with open("cinsulin-seq-clean.txt", "w") as cinsulin:
    cinsulin.write(cleanFile[54:89])
    
with open("ainsulin-seq-clean.txt", "w") as ainsulin:
    ainsulin.write(cleanFile[89:])

insulinFile.close()