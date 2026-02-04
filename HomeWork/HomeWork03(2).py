frst1 = []

if len(frst1) == 0:
    result = 0

else:
    sum_frst1 = sum(frst1[0::2])
    result = sum_frst1 * frst1[-1]

print(result)