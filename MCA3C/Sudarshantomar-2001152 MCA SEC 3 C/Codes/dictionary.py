# Sudarshan Tomar MCA 3 - DEHRADUN Campus STD ID-20711156

test_str = 'I  Sudarshan Tomar studying in GEHU'
print("The original string is : " + str(test_str))
  
lookp_dict = {"I" : "Myself", "GEHU" : "GRAPHIC ERA HILL UNIVERSITY"}
  
temp = test_str.split()
res = []
for wrd in temp:
      
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)
print("Replaced Strings : " + str(res)) 