import cwiid, time

button_delay = 0.2

print 'Please press buttons 1 + 2 on your Wiimote now ...'
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!"
  quit()

print 'Wiimote connection established!\n'
print 'Go ahead and press some buttons\n'
print 'Press PLUS and MINUS together to disconnect and quit.'
print 'Type in the sense using "A" for dots and "B" for dashes.'
print 'Type letters quickly, pause about 2 seconds inbetween letters, and about 5 seconds in between words.'
print 'Press "home" button to start typing morse code'

# function to interpret morse code (start)
def morse_code_interpreter():
    A = [0, 1]; B = [1, 0, 0, 0];C = [1,0,1,0]
    D = [1, 0, 0]; E = [0]; F = [0, 0, 1, 0]
    G = [1, 1, 0]; H = [0, 0, 0, 0]; I = [0, 0]
    J = [0, 1, 1, 1]; K = [1, 0, 1]; L = [0, 1, 0, 0]
    M = [1, 1]; N = [1, 0]; O = [1, 1, 1]
    P = [0, 1, 1, 0]; Q = [1, 1, 0, 1]; R = [0, 1, 0]
    S = [0, 0, 0]; T = [1]; U = [0, 0, 1]
    V = [0, 0, 0, 1]; W = [0, 1, 1]; X = [1, 0, 0, 1]
    Y = [1, 0, 1, 1]; Z = [1, 1, 0, 0]

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

    # Iterate through the alphabet to put together the sentence
    for jj in range(0,len(y)):
        if y[jj] == A:
            sentence = sentence + 'A'
        if y[jj] == B:
            sentence = sentence + 'B'
        if y[jj] == C:
            sentence = sentence + 'C'
        if y[jj] == D:
            sentence = sentence + 'D'
        if y[jj] == E:
            sentence = sentence + 'E'
        if y[jj] == F:
            sentence = sentence + 'F'
        if y[jj] == G:
            sentence = sentence + 'G'
        if y[jj] == H:
            sentence = sentence + 'H'
        if y[jj] == I:
            sentence = sentence + 'I'
        if y[jj] == J:
            sentence = sentence + 'J'
        if y[jj] == K:
            sentence = sentence + 'K'
        if y[jj] == L:
            sentence = sentence + 'L'
        if y[jj] == M:
            sentence = sentence + 'M'
        if y[jj] == N:
            sentence = sentence + 'N'
        if y[jj] == O:
            sentence = sentence + 'O'
        if y[jj] == P:
            sentence = sentence + 'P'
        if y[jj] == Q:
            sentence = sentence + 'Q'
        if y[jj] == R:
            sentence = sentence + 'R'
        if y[jj] == S:
            sentence = sentence + 'S'
        if y[jj] == T:
            sentence = sentence + 'T'
        if y[jj] == U:
            sentence = sentence + 'U'
        if y[jj] == V:
            sentence = sentence + 'V'
        if y[jj] == W:
            sentence = sentence + 'W'
        if y[jj] == X:
            sentence = sentence + 'X'
        if y[jj] == Y:
            sentence = sentence + 'Y'
        if y[jj] == Z:
            sentence = sentence + 'Z'
        if y[jj] == word_space:
            sentence = sentence + ' '
        
    print(sentence)
# end of function

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:
    buttons = wii.state['buttons']
    if (buttons & cwiid.BTN_HOME):
        print('Start typing sentence')
        time.sleep(button_delay)

        x =[];
        counter = 0
        counter_delay = .05

        while counter < 500:
            buttons = wii.state['buttons']
            counter = counter + 1
            time.sleep(counter_delay)
            
            if counter >= 40:
                print('SPACE')
                x.append(2)
                print('timer reset')
                print(x)
                counter = 0

            if (buttons & cwiid.BTN_A):
                x.append(0)
                print(x)
                print('timer reset')
                counter = 0
                time.sleep(button_delay)
            
            if (buttons & cwiid.BTN_B):
                x.append(1)
                print(x)
                print('timer reset')
                counter = 0
                time.sleep(button_delay)
                
            if (buttons & cwiid.BTN_1):
                x = [];
                time.sleep(button_delay+3)
                print('reset')
                
            if (buttons & cwiid.BTN_2):
                morse_code_interpreter()
                print('RESET ALL')
                break
                
            if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
                print '\nClosing connection ...'
                # NOTE: This is how you RUMBLE the Wiimote
                wii.rumble = 1
                time.sleep(1)
                wii.rumble = 0
                exit(wii)
                

        print(x)


