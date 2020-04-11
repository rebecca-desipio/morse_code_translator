#Maria Buzzoni Wiimote Morse Decoder Ver. 1.1

#Currently only outputs single words

#Adapted from #https://www.raspberrypi-spy.co.uk/2013/02/nintendo-wii-remote-python-and-the-raspberry-pi/

#defined inputs
    #A is dot
    #B is dash
    #A+B appends letter to word
    #home initiates output of word

#define Morse dictionary

morse_dictionary = {	'.-':'A', 
                        '-...':'B', 
                        '-.-.':'C', 
                        '-..':'D', 
                        '.':'E', 
                        '..-.':'F', 
                        '--.':'G', 
                        '....':'H', 
                        '..':'I', 
                        '.---':'J', 
                        '-.-':'K', 
                        '.-..':'L', 
                        '--':'M', 
                        '-.':'N', 
                        '---':'O', 
			'.--.':'P', 
			'--.-':'Q', 
                    	'.-.':'R', 
			'...':'S', 
			'-':'T', 
                        '..-':'U', 
                        '...-':'V', 
                        '.--':'W', 
                        '-..-':'X', 
                        '-.--':'Y',
                        '--..':'Z'}

import cwiid
import time

button_delay = 0.1

print 'Press 1+2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.

try:
wii=cwiid.Wiimote()
except RuntimeError:
print "Error opening wiimote connection"
quit()
 
print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'
 
wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']

    #creates empty string to put dots and dashes in
    morse_input = ''

    #creates empty string to put decoded letters in
    morse_output = ''
 
    if (buttons & cwiid.BTN_A):
        morse_input = morse_input + '.'
        time.sleep(button_delay)

    elif (buttons & cwiid.BTN_B):
        morse_input = morse_input + '-'
        time.sleep(button_delay)

    elif (buttons - cwiid.BTN_A - cwiid.BTN_B == 0):
	if morse_input in morse_dictionary:
	    morse_output = '' + morse_dictionary[morse_input]
	    morse_input = ''
	else: 
	    time.sleep(button_delay)	

    #print translated word 
    elif (buttons & cwiid.BTN_HOME):
    	print(morse_output)
    	morse_input = ''
    	morse_output = ''
    	time.sleep(button_delay)

