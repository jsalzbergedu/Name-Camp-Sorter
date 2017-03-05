from pathlib import Path

pByStudent = Path('By-Student')
pByCamp = Path('By-Camp')

if not pByStudent.exists() and not pByCamp.exists():
    pByStudent.mkdir()
    pByCamp.mkdir()


# Some input file is parsed
# TODO automate file to open
changeString = '-unused-'
studentsNameString = '-unused-'
ageString = '-unused-'
birthdateString = '-unused-'
upcomingGradeString = '-unused-'
streetAdressString = '-unused-'
cityString = '-unused-'
zipString = '-unused-'
lastGradeSchoolString = '-unused-'
parentsNameString = '-unused-'
parentsPhoneString = '-unused-'
parentsEmailString = '-unused-'
programAndDateString = '-unused-'
costString = '-unused-'
programAndDateStringII = '-unused-'
costStringII = '-unused-'
programAndDateStringIII = '-unused-'
costStringIII = '-unused-'
eParentsHomePhoneString = '-unused-'
eMothersWorkPhoneString = '-unused-'
eMothersCellPhoneString = '-unused-'
eFathersWorkPhoneString = '-unused-'
eFathersCellPhoneString = '-unused-'
eContactNameString = '-unused-'
eContactPhoneString = '-unused-'
eContactCellPhoneString = '-unused-'
localHospitalPreferenceString = '-unused'
medAllergiesString = '-unused-'
medAsthmaString = '-unused-'
medEpilepsyString = '-unused-'
medHeartProblemsString = '-unused-'
medDrugAllergiesString = '-unused-'
medRecurringIlnessString = '-unused-'
medOtherString = '-unused-'
medExplainString = '-unused-'
dossier = open('igmeTest1.txt')
'''
for rangee in dossier

dossier.close()
'''
