
test_str = 'She is Good Girl'
print("The original string is : " + str(test_str))
  
lookp_dict = {"Good" : "very good", "Girl" : "She is also Beautiful"}
  
temp = test_str.split()
res = []
for wrd in temp:
      
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)
print("Replaced Strings : " + str(res))