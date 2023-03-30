pr = float(input())
q = int(input())
total = pr * q
desc = (q/100) 
print(f'{total:.2f}')
print(f'{(total-total*0.10)-(total*(q/100)):.2f}')
