from utils import inputInt
from utils import inputYN

n = inputInt("n을 입력하시오: ")
flag = inputYN("대상을 지정하시겠습니까? (y/n) ")
array = list()
if(flag == "y") :
  a = 0
  while(a > -1) :
    a = inputInt("대상 후보를 입력하시오(끝내려면 -1을 입력하시오): ")
    if(a != -1) :
      array.append(a)
else :
  a = 1
  while( a < 10):
    array.append(a)
    a = a + 1
sumValue = inputInt("합계를 입력하시오: ")

result = list()

def getCombination(parent, count, target):
  temp = target.copy()
  while len(temp) :
    t = temp.pop()
    if count > 1 :
      tempParent = parent.copy()
      tempParent.append(t)
      getCombination(tempParent, count - 1, temp)
    else :
      tempParent = parent.copy()
      tempParent.append(t)
      if(sum(tempParent) == sumValue) :
        result.append(tempParent)

getCombination(list(), n, array)

print("*****result*****")
print(result)