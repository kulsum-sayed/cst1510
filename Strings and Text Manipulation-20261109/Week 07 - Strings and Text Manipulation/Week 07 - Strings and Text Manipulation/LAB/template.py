"""
RECORD CHECK  -  my version
===========================

Name  : sayed kulsum
Lane  :  AI 
Date  : 12-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """status line into a dictionary."""
    line =raw_line.strip().lower()
    hostname_part,rest =line.split(",", 1)
    hostname =hostname_part.strip()
    fields = {}
    for p in rest.split(","):
        key, value = p.split("=")
        fields[key.strip()] = float(value.strip())
    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}
def status_of(used, total, warning=90):
    """return OVER LIMIT WARNING or OK """
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning:
        return "WARNING"
    else:
        return "OK"


path = r"C:\Users\Farhat\Downloads\mdx\Strings and Text Manipulation-20261109\Week 07 - Strings and Text Manipulation\Week 07 - Strings and Text Manipulation\LAB\messy_lines.txt"

raw_records = []
with open(path) as f:
    for line in f:
        raw_records.append(line)

total =0
flagged =0

for raw_record in raw_records:
    record =parse_line(raw_record)
    current_status = status_of(record["used"],record["total"])
    print(record, current_status)

    total=total + 1
    if current_status != "OK":
        flagged =flagged + 1

print(f"Total records: {total}, Flagged:{flagged}")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] Run it with a value that will not convert to a number - write the
#        error down: ValueError: could not convert string to float: 'unknown'
#    [x] Check every function does one job, with a docstring


