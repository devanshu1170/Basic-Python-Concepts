"""
amount=p(1+R/100)**T
ci=amount-p
"""
p=float(input("enter initial principal balance:"))
r=float(input("enter initial interest rate:"))
t=float(input("enter time (in years): "))
amount=p*(1+r/100)**t
ci=amount-p
print("compound interest is: ", ci)

