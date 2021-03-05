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


#Question A two dimensional array stores the data of the number of Laptops sold by a company in Dubai. The data shows the sales for the 12 months. The Laptops brands sold by the company are: SONY, HP, DELL and ACER. Download the data from theictclub.com.
	SONY	HP	DELL	ACER
Jan	15	34	23	12
Feb	12	43	45	23
March	13	33	43	23
April	45	23	32	44
May	34	32	12	23
June	32	33	12	23
July	22	23	33	23
August	12	23	12	23
September	10	21	34	24
October	12	34	35	23
November	18	23	40	33
December	20	30	42	35

Your program must produce the output for
1.	Total number of laptops of each brand sold during the entire year.
