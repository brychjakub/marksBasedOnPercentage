def counter():
  a = int(input("získaný počet bodů" + "\n"))
  b = int(input("maximální počet bodů" + "\n"))

  result = (a / b) * 100
  print(f"{result} %")

  if result >= 91:
    print("výsledná známka je 1")
  elif 88 < result <= 90:
    print("výsledná známka je 1-")
  elif 75 < result <= 88:
    print("výsledná známka je 2")
  elif 73 < result <= 75:
    print("výsledná známka je 2-")
  elif 50 < result <= 73:
    print("výsledná známka je 3")
  elif 48 < result <= 50:
    print("výsledná známka je 3-")
  elif 25 < result <= 48:
    print("výsledná známka je 4")
  elif 23 < result <= 25:
    print("výsledná známka je 4-")
  else:
    print("výsledná známka je 5")


counter()