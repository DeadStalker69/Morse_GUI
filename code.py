import time                             #import time enables LED blinking functionality
from time import sleep                  #sleep in the functions used for LED blinking
from tkinter import *                   #import tkinter library for GUI interface
import tkinter.font                     
from gpiozero import LED                #using gpiozero module. this helps to its functions which are shorter and easier as compared to rpi.GPIO's functions. 
									    #import LED enables LED functions, like is_lit, off, on etc. 
import RPi.GPIO   

RPi.GPIO.setmode(RPi.GPIO.BOARD)        #using GPIO naming convention

led = LED(14)    

win = Tk()                              #initialising a GUI window 
win.title("Morse Code")                 #setting title of GUI window
Font = tkinter.font.Font(family = 'Calibri' , size = 12, weight = "bold")

def dash():                             #dfining a dash function 
    led.on()
    time.sleep(1.5)
    led.off()
    time.sleep(1)

def dot():                              #defining a dot function
    led.on()
    time.sleep(0.01)
    led.off
    time.sleep(1)

def space():                            #defining a space function
    led.off()
    time.sleep(2)

letters = {                             #a dictionary of all alphabets to morse code.
      'A': '.-', 
      'B': '-...', 
      'C': '-.-.', 
      'D': '-..', 
      'E': '.', 
      'F': '..-.', 
      'G': '--.', 
      'H': '....', 
      'I': '..', 
      'J': '.---', 
      'K': '-.-', 
      'L': '.-..', 
      'M': '--', 
      'N': '-.', 
      'O': '---', 
      'P': '.--.', 
      'Q': '--.-', 
      'R': '.-.', 
      'S': '...', 
      'T': '-', 
      'U': '..-', 
      'V': '...-', 
      'W': '.--', 
      'X': '-..-', 
      'Y': '-.--', 
      'Z': '--..', 
      '1': '.----', 
      '2': '..---', 
      '3': '...--', 
      '4': '....-', 
      '5': '.....', 
      '6': '-....', 
      '7': '--...', 
      '8': '---..', 
      '9': '----.', 
      '0': '-----',
      ' ': ' ',
          }

def morseToString(stringCode):          #definingt a function which translates an alphabet to morse code
    morseString = ""                    #intialising an empty string variable   
    for c in stringCode:                #a for loop for each alphabet in the user input
        morseString += letters[c.upper()]   #comapring each alphabet of input string and finding a match in 'letters' dictionary. then adding the corresponding morse code to the string variable initialsed earlier.
        morseString += " "              #adding an empty chracter to the string variable between morse code of each alphabet
    
    return morseString

def blinker():                          #defining a function which blinks the LED
    blinkText = codeString.get()        #reading the input from user and putting it in a variable
    
    conversion = morseToString(blinkText)   #putting the user input to an earlier defined function to convert it to morse code
    print(conversion)                   #printing the morse code on the terminal
    
    for alphabet in conversion:         #a for loop fo each word 
            for letter in alphabet:     #a for loop for each alphabet in each word
                if letter == "-":       #if else case to blink LED according to the morse code
                    dash()
                elif letter == ".":
                    dot()
                elif letter == " ":
                    space()
                led.off()               #adding a delay after each alphabet
                time.sleep(1)
    led.off()                           #turing the LED off after the morse code is read completly.



def close():                            #definig a function which turns led off on closing the window
    led.off()
    win.destroy()

codeString = Entry(win,font=Font, width=30)     #a user input widget from tkinter libarary
codeString.grid(row=0, column=1)

launch = Button(win,text='SUBMIT', font=Font, command=blinker, bg='blue', height=1, width=13)   #a button that triggers the conversion and LED blinking
launch.grid(row=1, column=1)

exitButton = Button(win, text = 'Exit', font  = Font, command = close, bg = 'blue', width = 24)     #a button to close the window
exitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close) #adding the defined function 'close' on 'close window' button
win.mainloop()

