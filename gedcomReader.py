"""
Jalen Thompson
Project: GEDCOM Parser
"""
import sys

VALID_TAGS = {
    ("0", "INDI"),
    ("0", "FAM"),
    ("0", "HEAD"),
    ("0", "TRLR"),
    ("0", "NOTE"),
    ("1", "NAME"),
    ("1", "SEX"),
    ("1", "BIRT"),
    ("1", "DEAT"),
    ("1", "FAMC"),
    ("1", "FAMS"),
    ("1", "MARR"),
    ("1", "HUSB"),
    ("1", "WIFE"),
    ("1", "CHIL"),
    ("1", "DIV"),
    ("2", "DATE"),
}

def parse_line(raw_line) -> tuple[str, str, str, str]:
    tokens = raw_line.strip().split()

    if not tokens:
        return ("", "" ,"" ,"")

    level = tokens[0]

    if (level == "0" and len(tokens) >= 3 and tokens[2] in ["INDI", "FAM"]):
        tag = tokens[2]
        arguments = tokens[1]
    else:
        tag = tokens[1] if len(tokens) > 1 else ""
        arguments = " ".join(tokens[2:]) if len(tokens) > 2 else ""
    
    valid = "Y" if (level, tag) in VALID_TAGS else "N"
    return (level, tag, valid, arguments)

def process_gedcom(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return
    
    for line in lines:
        display_line = line.rstrip("\n")
        level, tag, valid, arguments = parse_line(display_line)

        print(f"--> {display_line}")
        print(f"<-- {level}|{tag}|{valid}|{arguments}")

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "thompson_family.ged"

process_gedcom(file)