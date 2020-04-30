x = [0, 1, 2, 1, 0, 0, 2, 2, 0, 1]

A = [0, 1]
D = [1, 0, 0]
word_space = [3]
temp = []
y = [];
sentence = ''

print(len(x))
for ii in range(0,len(x)):
    print('index: ',ii)
    print('x value: ',x[ii])
    print('y: ',y)
    
    if (x[ii] == 0) | (x[ii] == 1):
        print("!")
        temp.append(x[ii])
        print('temp var: ',temp)

    if ii != (len(x)-1):
        if (x[ii] == 2) & (x[ii+1] == 2):
            y.append(temp)
            temp = []
            y.append([3])
            
        elif (x[ii] == 2) & (x[ii+1] != 2):
            if (x[ii-1] == 2):
                print('skip')
            else:
                y.append(temp)
                temp = []
                y.append([2])
    
    if ii == (len(x)-1):
        y.append(temp)
                
for jj in range(0,len(y)):
    if y[jj] == A:
        sentence = sentence + 'A'
    if y[jj] == D:
        sentence = sentence + 'D'
    if y[jj] == word_space:
        sentence = sentence + ' '
    print(sentence)
    
        
        