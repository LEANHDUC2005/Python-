def average(grades_list):
    sum = 0
    for i in grades_list:
        sum += i
    avg = sum / len(grades_list)
    print(avg)
def highest(grades_list):
    grades_list.sort( reverse = True )
    print(grades_list[0])
def lowest(grades_list):
    grades_list.sort()
    print(grades_list[0])
    
