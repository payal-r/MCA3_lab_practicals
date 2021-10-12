test_str = 'myself Mansi Tyagi is from dehradun'
print("The original string is : " + str(test_str))
  
lookp_dict = {"myself" : "I", "dehradun" : "clement town"}
  
temp = test_str.split()
res = []
for wrd in temp:
      
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)
print("Replaced Strings : " + str(res)) 