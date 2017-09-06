phonenumber = input("Please enter the digits of your phone number: ")

# phonenumber = "1234567890"

# area = phonenumber[0:3]
# print(area)
# mid = phonenumber[3:6]
# print(mid)
# end = phonenumber[6:]
# print(end)
# print("{}-{}-{}".format(area,mid,end))

def pretty_phonenumber(phonenumber):
    area = phonenumber[0:3]
    mid = phonenumber[3:6]
    end = phonenumber[6:]
    print("{}-{}-{}".format(area, mid, end))

pretty_phonenumber(phonenumber)