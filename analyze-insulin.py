insulinText = insulinFile.read()

removeOrigin=insulinText.replace("ORIGIN", "")
removeSlash=removeOrigin.replace("//", "")
removeNewline=removeSlash.replace("\n", "")
noSpace=removeNewline.replace(" ","")
cleanText = ''.join([i for i in noSpace if not i.isdigit()])

with open("preproinsulin-seq-clean.txt", "w") as preproinsulin:
    preproinsulin.write(cleanText)

with open("lsinsulin-seq-clean.txt", "w") as lsinsulin:
    lsinsulin.write(cleanText[0:24])
    
with open("binsulin-seq-clean.txt", "w") as binsulin:
    binsulin.write(cleanTexts[24:54])
    
with open("cinsulin-seq-clean.txt", "w") as cinsulin:
    cinsulin.write(cleanText[54:89])
    
with open("ainsulin-seq-clean.txt", "w") as ainsulin:
    ainsulin.write(cleanText[89:])

insulinFile.close()