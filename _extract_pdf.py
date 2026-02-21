import sys
from pdfminer.high_level import extract_text

for f in sys.argv[1:]:
    print(f"===== {f} =====")
    print(extract_text(f))
    print()
