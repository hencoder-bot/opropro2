  
marks = int(input('input your marks'))
if marks < 0 or marks > 100:
        print( 'invalid marks')
elif marks >= 90:
        print ('A')
elif marks >= 80:
        print ('B')
elif marks >= 70:
        print ('C')
elif marks >= 60:
        print ('D')
else:
        print('F')
    
