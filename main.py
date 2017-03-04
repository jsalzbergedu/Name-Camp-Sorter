from pathlib import Path

pByStudent = Path('By-Student')
pByCamp = Path('By-Camp')

if not pByStudent.exists() and not pByCamp.exists():
	pByStudent.mkdir()
	pByCamp.mkdir()
