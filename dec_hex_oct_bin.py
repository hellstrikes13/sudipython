n1  = 63
n = len(bin(n1).lstrip('0b'))
for i in range(1,n1+1):
 print str(i).rjust(n,' '),str(oct(i)).lstrip('0').rjust(n,' '),str(hex(i)).lstrip('0x').upper().rjust(n,' '),str(bin(i)).lstrip('0b').rjust(n,' ')
