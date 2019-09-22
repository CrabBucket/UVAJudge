master_list = []
temp = 0
skip = False
exitCount = 0

# So I will just go over the idea of my algorithm.
# First, we see that any super power can be written in the form a**(x*y).
# This can be seen by writing it like this as well (a^x)^y  if you let (a^x) = b and (x**y) =z you see that:
# b^y = a^z where a and b are always different. So a**(x*y) is always a super power.
# The rest is just a matter of iterating over a, x, y in an efficent manner so we don't time out.
# The only real challenge in this is knowing when to move on to the next combination.
# This is done using exitCount and skip where we keep track of how many time reach the inner most if loop when,
# y == 2 as if we got to that point it means that we have a too large a,x combo and need to stop trying a,x,2
# which will always be too large if a,x-1,2 was too large.
# Lastly when we find the largest A,x,y pair we can just exit the entire loop as all further combos will be larger






for a in range(2,(2 ** 16)+1):

    for x in range(2,33):
        #Similar reasoning to above
        for y in range(2,33):

            temp = a ** (x*y)
            if (temp<=(2 ** 64)-1):
                master_list.append(temp)

            else:

                if (y == 2):


                    skip = True


                    exitCount += 1
                else:
                    exitCount = 0
                break

        if skip:

            skip = False
            break
    if(exitCount==2):
        break
print(1)
master_list = sorted(set(master_list))

for x in master_list:
    print(x)
