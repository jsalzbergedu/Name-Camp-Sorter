from pathlib import Path

pByStudent = Path('By-Student')
pByCamp = Path('By-Camp')

if not pByStudent.exists() and not pByCamp.exists():
	pByStudent.mkdir()
	pByCamp.mkdir()

## some input file is parsed
## TODO automate file to open
changeString = '-unused-'
studentsNameString = '-unused-'
ageString = '-unused-'
birthdateString = '-unused-'
upcomingGradeString = '-unused-'
streetAdressString = '-unused-'
cityString = '-unused-'
zipString = '-unused-'
lastGradeSchool = '-unused-'
dossier = open('igmeTest1.txt')
'''
for rangee in dossier

dossier.close()
'''
