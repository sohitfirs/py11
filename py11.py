def pl(m, i = 0):
    
    print(m[i])    
    i += 1
    
    if i > len(m)-1:
        print('END LIST')
        return
    
    x = pl(m, i)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

pl(my_list)

input()
