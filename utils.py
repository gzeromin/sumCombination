def inputInt(msg):
  a = input(msg)
  try :
    a = int(a)
  except:
    print("숫자로 다시 입력해주시기 바랍니다.")
    a = inputInt(msg)
  return a

def inputYN(msg):
  a = input(msg)
  if(a != "y" and a != "n"):
    print("y 또는 n을 입력해주시기 바랍니다.")
    a = inputYN(msg)
  else:
    return a
