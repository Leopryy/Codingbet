def front3(str):
  new = list(str)
  fthree = []
  fthree.append(new[0])
  fthree.append(new[1])
  fthree.append(new[2])
  end = ''.join(fthree)
  end1 = end+end+end
  return end1

print(front3('Java'))