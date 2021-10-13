
test_str = 'I  Pawan Pandey live in Haldwani'
print("The original string is : " + str(test_str))
  
lookp_dict = {"I" : "Myself", "haldwani" : "dehradun"}
  
temp = test_str.split()
res = []
for wrd in temp:
      
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)
print("Replaced Strings : " + str(res)) 