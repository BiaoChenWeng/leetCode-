

my_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
    }

class Solution(object):
    def romanToInt(self, s):
        suma=0;
        for x in s:
            if my_dict[x]>my_dict[letra_anterior]:
                suma= suma-(2*my_dict[letra_anterior])+my_dict[x]
            else:
                suma=suma+my_dict[x]
            
            letra_anterior=x
            
        return suma


