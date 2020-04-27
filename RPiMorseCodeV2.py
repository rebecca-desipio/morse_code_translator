#Maria Buzzoni Wiimote Morse Decoder Ver. 1.2

#Adapted from https://www.raspberrypi-spy.co.uk/2013/02/nintendo-wii-remote-python-and-the-raspberry-pi/

import cwiid
import time

button_delay = 0.5

print '\nPlease press 1 and 2 together to begin.'
print 'This may take a moment. Thank you for your patience.\n'
time.sleep(1)

#Here the program establishes a connection with the remote; if there is no connection, program ends

try:
    wii=cwiid.Wiimote()
except RuntimeError:
    print "No connection established, please try pressing 1 and 2 together again.\n"
    quit()
 
print '---------------------------------------------------------------------'
print 'Connection established. You may now begin inputting data.\n'
print 'The controls are as follows:\n'
print 'Press A to input a dot.'
print 'Press B to input a dash.'
print 'Press UP to submit a letter.'
print 'Press DOWN to submit a word.'
print 'Press HOME to receive your translated sentence.'
print 'Press PLUS and MINUS together to disconnect and quit at any time.\n'
print 'The controls to correct errors are as follows:\n'
print 'Press RIGHT to restart the input of a letter.'
print 'Press LEFT to restart the input of a word.'
print '---------------------------------------------------------------------\n'

###

#define Morse dictionary

morse_dictionary = {	'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G',
                        '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N',
                        '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', 
			'...-':'V', '.--':'W', '-..-':'X', '-.--':'Y','--..':'Z'}
 
#creates empty string to put dots and dashes in

morse_input = ''

#creates empty string to put decoded letters in

morse_output = ''

#creates empty string to put completed sentence in

morse_final = ''
 
wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']
 

    #the user made an error - to start a letter over 
    
    if (buttons & cwiid.BTN_RIGHT):
        morse_input = ''
        time.sleep(button_delay)
 
     #the user made an error - to start a word over 
 
    if (buttons & cwiid.BTN_LEFT):
        morse_output = ''
        time.sleep(button_delay)
 
    #the user inputs a dot

    if (buttons & cwiid.BTN_A):
        morse_input = morse_input + '.'
        print 'You added a dot to ' + morse_input
        time.sleep(button_delay)

    #the user inputs a dash

    if (buttons & cwiid.BTN_B):
        morse_input = morse_input + '-'
        print 'You added a dash to ' + morse_input
        time.sleep(button_delay)

    #the user completes and submits a letter 

    if (buttons & cwiid.BTN_UP):
        if morse_input in morse_dictionary:
	    morse_output = morse_output + morse_dictionary[morse_input]
	    print 'You submitted the letter ' + morse_dictionary[morse_input] + '\n' 
	else: 
	    print 'I cannot find a letter with the code' + morse_input
	    print 'Please try again'
	morse_input = ''
	time.sleep(button_delay)

    #the user completes and submits a word

    if (buttons & cwiid.BTN_DOWN):
        morse_final = morse_final + ' ' + morse_output
        print 'You submitted the word ' + morse_output + '\n' 
	morse_output = ''
        time.sleep(button_delay)	

    #the user completes a sentence and promts translated result to be displayed

    if (buttons & cwiid.BTN_HOME):
        print '------------------------------------------------------'
        print '\nYour completed sentence translated from Morse code is:\n'
	print(morse_final)
	print '------------------------------------------------------'
	#morse_input = ''
	#morse_output = ''
	#morse_final = ''
        time.sleep(button_delay)

    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print '\nThank you for using this program. Closing connection.\n'
	wii.rumble = 1
	time.sleep(1)
	wii.rumble = 0
	exit(wii)
	break
	
