series= (21,22,23,24,25,26,27,28,29,30,31,33,35)
odd_count=0
even_count=0
for i in series:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print("odd number count:  ",odd_count)
print("even number count:  ",even_count)