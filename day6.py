marks = {"Ali": 85, "Sara": 92, "Bilal": 95, "Hina": 60}

print("Marks:", marks);

def calculate_average(marks):
    total = 0
    for name in marks:
        total = total + marks[name]
    average = total / len(marks)
    return average

def find_topper(marks):
    top_name = ""          # champion's name so far
    top_mark = 0           # champion's mark so far
    for name in marks:
        if marks[name] > top_mark:
            top_name = name
            top_mark = marks[name]
    return top_name, top_mark

def find_lowest(marks):
    low_name = ""
    low_mark = 999      # blank 1: what starting value? (think: high, not 0)
    for name in marks:
        if marks[name] < low_mark:    # blank 2: which comparison? (< or >)
            low_name = name
            low_mark = marks[name]
    return low_name, low_mark

print("Lowest:", find_lowest(marks))

print("Average:", calculate_average(marks))
print("Topper:", find_topper(marks))