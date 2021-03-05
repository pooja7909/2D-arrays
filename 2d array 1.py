laptops = [[15,34,23,12],[12,43,45,23],[13,33,43,23],[45,23,32,44],[34,32,12,23],[32,33,12,23],[22,23,33,23],[12,23,12,23],[12,34,35,23],[18,23,40,33],[20,30,42,35]]
t=[]
#numrows = len(laptops)
#numcolms = len(laptops[0])
#print(numrows)
#print(numcolms) 
def sum2(laptops):
    for row in range (0,len(laptops)):
        sum1 = 0
        for col in range(len(laptops[0])):
            sum1 = sum1 + laptops[row][col]
        t.append(sum1)
    return t

total=sum2(laptops)
print(total)
'''
def row_sums(square):

    # list to store sums
    output = []

    # go through each row in square
    for row in square:

        # variable to store row total
        total = 0

        # go through each item in row and add to total
        for item in row:
            total += item

        # append the row's total to the output list
        output.append(total)
    return output

  

square = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
   [13, 14, 15, 16]
]

row_totals = row_sums(square)
print(row_totals)'''
