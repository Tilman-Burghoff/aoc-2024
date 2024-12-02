with open("input.txt") as f:
    data = f.readlines()

def is_allowed(report):
    is_increasing = int(report[1]) > int(report[0])
    last_el = int(report[0])
    for el in report[1:]:
        el = int(el)    
        if not (el > last_el) == is_increasing:
            return False
        if abs(el-last_el) not in [1,2,3]:
            return False
        last_el = el
    return True


# tried to be efficient instead of brute-forcing, 
# missed edge cases so I brute forced it (didnt use this function)
def is_allowed_dampened(report):
    is_increasing = int(report[1]) > int(report[0])
    if not (int(report[2]) > int(report[1])) == is_increasing:
        is_increasing = int(report[3]) > int(report[2]) # majority voting
    last_el = int(report[0])
    i = 1
    dampener = False
    while i < len(report):
        el = int(report[i])    
        if (not (el > last_el) == is_increasing) or (abs(el-last_el) not in [1,2,3]):
            if dampener:
                return False
            dampener = True
            i += 2
        else:
            last_el = el
            i += 1
    return True



data = list(map(lambda x: x.split(), data))

print("Part 1:", sum(map(is_allowed, data)))

print("Part 2:", sum(map(lambda report: any(map(is_allowed, [report[:i]+ report[i+1:] for i in range(len(report))])), data)))