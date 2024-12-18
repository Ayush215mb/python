
L = [2e-04,"a",False, 87]
T = (6.22,"boy",True, 554)
for i in range(len(L)):
 if L[i]:
   L[i] = L[i] + T[i]
 else:
   T[i] = L[i] + T[i]
   break
L = [2e-04, &#39;a&#39;, False, 87]
T = (6.22, &#39;boy&#39;, True, 554)
for i in range(len(L)):
if L[i]:
L[i] = L[i] + T[i]
else:
T[i] = L[i] +
