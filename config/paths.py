from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DISC_STANDARDS = BASE_DIR / "disclosure_standards"
DISC_STANDARDS_RAW = DISC_STANDARDS / "raw"
DISC_STANDARDS_PROCESSED = DISC_STANDARDS / "processed"