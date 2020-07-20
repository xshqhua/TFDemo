a = "ggsssaaaaww"
b_dict = {}
for i in range(len(a)):
    b_dict[a[i]] = b_dict.get(a[i], 0) + 1

    # if a[i] in b_dict.keys():
    #     b_dict[a[i]] = b_dict[a[i]] + 1
    # else:
    #     b_dict[a[i]] = 1
    #
print(b_dict)

from operator import itemgetter

# sorted(b_dict.items(), key=itemgetter(0, 1))
# c = sorted(b_dict.items(), key=lambda x: (x[1]), reverse=True)
c = sorted(b_dict.items(), key=itemgetter(0, 1))
print(c)
for j in c:
    print(j[0], end="")
