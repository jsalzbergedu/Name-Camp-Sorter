from pathlib import path

wrkngDrctry = Path()

if not wrkngDrctry('By-Student').exists() and not wrkngDrctry('By-Camp').exists():
	wrkngDrctry.mkdir()
