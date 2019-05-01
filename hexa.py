hexa.py
hexnu = []
octnu = []
nos = []
nu = raw_input 'number: '

if 1 < nu < 99:
 for  i in range(1,nu+1):
   hex_num = hex(i)
   hexnu.append(hex_num)
   oct_num = oct(i)
   octnu.append(oct_num)
   nos.extend[(hexnu,octnu)]
else:
 print 'sorry dude enter number between 1 to 99 only'

for i in nos:
 print ' '.join(i)
