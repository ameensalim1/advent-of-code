
def get_lists(filename):
    with open(filename) as f:
            total_list = []
            for line in f:
                # Split on whitespace and convert to integer
                total_list.append(list(map(int, line.strip().split())))
    return total_list

def check_safety(levels):

    if len(levels) < 2:
        # A report with fewer than 2 levels cannot be unsafe by the rules.
        return True
    is_increasing = levels[1] > levels[0]
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
    
        if not (1 <= abs(diff) <= 3):
             return False
        
        if ((diff > 0) != is_increasing):
             return False
        
    return True
    

def check_lists(reports_list):
    safe = 0
    for level in reports_list:
         if check_safety(level):
            safe += 1
    return safe


reports_list = get_lists("aocday2.txt")
# print(f"reports list {reports_list}")
safe = check_lists(reports_list)
print(safe)




            
                
                

                