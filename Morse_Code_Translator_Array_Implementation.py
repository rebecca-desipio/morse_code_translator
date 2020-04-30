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

print '-------------------------------------------------------------------------------------------------------'
print 'Wiimote connection established!\n'
print 'Press PLUS and MINUS together to disconnect and quit.'
print 'Type dots/dashes quickly, pause about 2 seconds inbetween letters, and about 4 seconds in between words.'
print 'Between letter, have one SPACE appear. Between words, two sets of SPACES should appear.'
print 'Press "home" button to start typing morse code'
print 'Input Morse Code using "A" for dots and "B" for dashes.'
print 'Press "2" to submit Morse code for translation'
print 'Press "1" to restart the phrase is you"ve messed up'
print '-------------------------------------------------------------------------------------------------------'

# function to interpret morse code (start)
def morse_code_interpreter():
    # EXAMPLE: ** x = [0, 1, 2, 1, 0, 0, 2, 2, 0, 1] --> AD A **
    # defined alphabet in terms of ones and zeros (zeros = dots, ones = dashes)
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

    # iterates through x and creates a 2D array for each "letter"
    for ii in range(0,len(x)):
        # checks if the element is a dot or dash
        # if yes, puts that element in a temp array which will later be added to y
        # when put in y, a 2D array is created 
        if (x[ii] == 0) | (x[ii] == 1):
            temp.append(x[ii])
        
        if ii != (len(x)-1):
            # if there are two 2's in a row, a 3 will be representative in y as a space between words
            if (x[ii] == 2) & (x[ii+1] == 2):
                y.append(temp)
                temp = []
                y.append([3])
                
            # only one 2 is found, then a 2 will be representative of a letter space
            elif (x[ii] == 2) & (x[ii+1] != 2):
                if (x[ii-1] != 2):
                    y.append(temp)
                    temp = []
                    y.append([2])
                    
        # when the end of the sentence is reached, the last temp variable made is appended to y
        # this completes the iteration of the x array and completes creating the 2D array of y from x
        if ii == (len(x)-1):
            y.append(temp)
            
        # ** y = [[0, 1], [2], [1, 0, 0], [3], [0, 1]] **

    # Iterate through 2D array, y, to match elements of 2D array against the alphabet letters
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
    # ** AD A **
# end of function

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

# this allows the user to press wiimote buttons
while True:
    buttons = wii.state['buttons']
    
    # press home button to be able to type morse code
    if (buttons & cwiid.BTN_HOME):
        print('Start typing sentence')
        time.sleep(button_delay)

        x =[]; # variable defined for morse code input (0 = dot, 1 = dash, 2 = space)
        counter = 0
        counter_delay = .05
        k = 0
        
        # counter starts
        while counter < 500:
            buttons = wii.state['buttons']
            counter = counter + 1
            time.sleep(counter_delay)
            
            # if about 2 seconds passes, a letter space is considered, and a 2 is appended to x
            # This is important later for when the x array is analyzed in the function
            # NOTE: if two, 2's are inputted in a row, then a word space is considered. 
            if counter >= 40:
                k = k+1                     # counts spacers for the user to keep up with the rhythm
                print(k, ': SPACE')         # prints SPACE
                x.append(2)                 # places a 2 in the x array
                counter = 0                 # resets the counter

            # this will enter a dot
            if (buttons & cwiid.BTN_A):     # button A has beed pressed
                x.append(0)                 # places a 0 in the x array
                counter = 0                 # resets the counter
                time.sleep(button_delay)
            
            # this will enter a dash
            if (buttons & cwiid.BTN_B):     # button B has been pressed
                x.append(1)                 # places a 1 in the x array
                counter = 0                 # resets the counter 
                time.sleep(button_delay)
            
            # allows the user to restart the sentence
            if (buttons & cwiid.BTN_1):     # button 1 has been pressed indicating the user has messed up their input.
                x = [];                     # empties the x array for the user to restart immediately after 'RESET ALL' prints
                time.sleep(button_delay+3)
                print('RESET ALL')
            
            # once finished with the sentence, click 2 for it to be analyzed
            if (buttons & cwiid.BTN_2):
                print('TRANSLATING MORSE CODE...')
                morse_code_interpreter() # function defined at the top
                break # this exits the counter while loop and the user can either click 'home' to type a new sentence or 'plus & minus' to exit
                
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):   # disconnects the wiimote and terminates the script. 
        print '\nClosing connection ...'
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)
                


