P=int(input("Enter Principal: "))
R=float(input("Enter Annual interest Rate: "))
T=int(input("Enter Time in year: "))
N=float(input("Enter number of interest applied in time periode: "))
import math
A=P*math.pow(1+(R/N),N*T)
print(A)