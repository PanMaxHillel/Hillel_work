import string

inp_user1 = input("Dai bykvi loh: ")

frs_let, sec_let = inp_user1.split("-")

letr =  string.ascii_letters

start_indx = letr.index(frs_let)
end_indx = letr.index(sec_let)

result = string.ascii_letters[start_indx:end_indx+1]

print(result)