"""
RECORD CHECK  -  my version
===========================

Name  : kulsum sayed
Lane  :  AI 
Date  : 18-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit, warning_at=90):
    """calculates difference percent and status for one record"""
    difference = value-limit 
    percent = (value/limit) * 100 
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= warning_at:
        status = "WARNING" 
    else:
        status = "OK" 
    return difference, percent, status 

def print_report(label, value, limit, difference, percent, status):
    """prints the report inside border"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}") #prints header with label
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}") #for right aligning
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}") #+ for showing sign
    print(f"  Of limit    : {percent:>9.1f} %")#right align with one decimal point 
    print(f"  Status      : {status:>10}") #righ within 10 spaces
    print("=" * 34)
    print()


def load_records(path):
    records_list = [] #empty list to store the records later on in code
    try:
        with open(path, "r") as f: #open the path and read the file
            for line in f: #for loop to read lines in the file
                label, val, lim = line.strip().split(",") #splitfor spliting the data with , and strip to remove space
                records_list.append({ #adding it to the empty records made above
                    "label":label,
                    "value":float(val), #getting it in float no string
                    "limit":float(lim)
                })
    except FileNotFoundError: #if file not found error is there the below msg would be printed
        print(f"data file'{path}'not found")
    return records_list #returning it to code


def save_results(path, results):
    with open(path, "w") as f: #opens file with write 
        for r in results: #loop for each result
            f.write(f"{r['label']},{r['status']}\n") #\n for ending line


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = load_records("records_sample.txt") #loading records fromf ile using load records function


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
overlimit=0 #counter for over limit records
results=[] #empty list for storing results
total= 0    

for record in records: #looping over each record dict in list
    total += 1 #when ever it loop scount would increase from 0 to 1 and on to get total
    difference,percent,status = check_record(record["value"],record["limit"]) #pulls out value and limit sends it into check record and calculates evrythin into percentaage status and difference
    print_report(record["label"],record["value"],record["limit"],
                 difference,percent,status) #takes calculated value with label etc and gives them to print report funtion

    results.append({"label":record["label"],"status":status}) #adding label and status

    if status == "OVER LIMIT":
        overlimit+= 1 #increase if overlimitfrom 0 to 1 and so onnnn

print(f"Checked {total} records \n {overlimit} were over limit") #\n to mak eit neat
save_results("results.txt",results) #saving result



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
