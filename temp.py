arr_a = [1,2,3,2,3,4,3,4,5,6]
arr_b = [7,2,10,2,7,4,9,4,9,8]
arr_c = [] 
for x in arr_a:
    if (x in arr_b) and (x not in arr_c):
       #( x in arr_b ) : True <-> giá trị của x xuất hiện ÍT NHẤT 1 LẦN trong arr_b
       #( x not in arr_c ): True <-> giá trị của x không xuất hiện trong arr_c
        arr_c.append(x)
print("arr_c:", arr_c)
#vKết quả: [2, 4]