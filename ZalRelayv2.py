#import
#  needed libraries
import RPi.GPIO as GPIO
import time
import tkinter as tk
import threading as th
from datetime import datetime

root = tk.Tk()
root.title('Zaleski Relay Control')

GPIO.setmode(GPIO.BCM)

# init list with pin numbers 
# pin 2 is Relay 1
# pin 3 is Relay 2
# pin 4 is Relay 3
# pin 17 is Relay 4
# pin 27 is Relay 5
# pin 22 is Relay 6
# pin 10 is Relay 7
# pin 9 is Relay 8
pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

#define initialized counter variables
counter1 = 0
running1 = False
counter2 = 0
running2 = False
counter3 = 0
running3 = False
counter4 = 0
running4 = False
counter5 = 0
running5 = False
counter6 = 0
running6 = False
counter7 = 0
running7 = False
counter8 = 0
running8 = False

#set wait time events
time1 = th.Event()
time2 = th.Event()
time3 = th.Event()
time4 = th.Event()
time5 = th.Event()
time6 = th.Event()
time7 = th.Event()
time8 = th.Event()

#sets autolog files if no input recieved
filename1 = 'Relay 1 logfile'
addtolog1 = 'Enter info you want added to logfile'
filename2 = 'Relay 2 logfile'
addtolog2 = 'Enter info you want added to logfile'
filename3 = 'Relay 3 logfile'
addtolog3 = 'Enter info you want added to logfile'
filename4 = 'Relay 4 logfile'
addtolog4 = 'Enter info you want added to logfile'
filename5 = 'Relay 5 logfile'
addtolog5 = 'Enter info you want added to logfile'
filename6 = 'Relay 6 logfile'
addtolog6 = 'Enter info you want added to logfile'
filename7 = 'Relay 7 logfile'
addtolog7 = 'Enter info you want added to logfile'
filename8 = 'Relay 8 logfile'
addtolog8 = 'Enter info you want added to logfile'

#define button functions
#Relay 1 functions
def power_input1(elapsed1):
    global t1
    global running1 
    power1_button['state']='disabled'
    stop1_button['state']='normal'
    running1=True
    t1 = e_t1.get()
    GPIO.output(2, GPIO.LOW)
    start1 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename1),'a+') as log1:
        log1.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start1, addtolog1))
    time1.clear()
    counter1_label(elapsed1)
    time1.wait(float(t1))
    GPIO.output(2, GPIO.HIGH)
    end1 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename1),'a+') as log1:
        log1.writelines('End time: {} \n\n'.format(end1))

def stop_input1(elapsed1):
    global running1 
    global counter1
    running1=False
    counter1=0
    GPIO.output(2, GPIO.HIGH)
    stopreset1 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename1),'a+') as log1:
        log1.writelines('Stop/reset time: {} \n\n'.format(stopreset1))
    time1.set()
    elapsed1['text']='waiting..'
    power1_button['state']='normal'
    stop1_button['state']='disabled'

#Relay 2 functions
def power_input2(elapsed2):
    global t2
    global running2
    power2_button['state']='disabled'
    stop2_button['state']='normal' 
    running2=True
    t2 = e_t2.get()
    GPIO.output(3, GPIO.LOW)
    start2 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename2),'a+') as log2:
        log2.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start2, addtolog2))
    time2.clear()
    counter2_label(elapsed2)
    time2.wait(float(t2))
    GPIO.output(3, GPIO.HIGH)
    end2 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename2),'a+') as log2:
        log2.writelines('End time: {} \n\n'.format(end2))

def stop_input2(elapsed2):
    global running2 
    global counter2
    running2=False
    counter2=0
    GPIO.output(3, GPIO.HIGH)
    stopreset2 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename2),'a+') as log2:
        log2.writelines('Stop/reset time: {} \n\n'.format(stopreset2))
    time2.set()
    elapsed2['text']='waiting..'
    power2_button['state']='normal'
    stop2_button['state']='disabled'

#Relay 3 functions
def power_input3(elapsed3):
    global t3
    global running3
    power3_button['state']='disabled'
    stop3_button['state']='normal' 
    running3=True
    t3 = e_t3.get()
    GPIO.output(4, GPIO.LOW)
    start3 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename3),'a+') as log3:
        log3.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start3, addtolog3))
    counter3_label(elapsed3)
    time3.clear()
    time3.wait(float(t3))
    GPIO.output(4, GPIO.HIGH)
    end3 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename3),'a+') as log3:
        log3.writelines('End time: {} \n\n'.format(end3))

def stop_input3(elapsed3):
    global running3 
    global counter3
    running3=False
    counter3=0
    GPIO.output(4, GPIO.HIGH)
    stopreset3 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename3),'a+') as log3:
        log3.writelines('Stop/reset time: {} \n\n'.format(stopreset3))
    time3.set()
    elapsed3['text']='waiting..'
    power3_button['state']='normal'
    stop3_button['state']='disabled'

#Relay 4 functions
def power_input4(elapsed4):
    global t4
    global running4 
    power4_button['state']='disabled'
    stop4_button['state']='normal'
    running4=True
    t4 = e_t4.get()
    GPIO.output(17, GPIO.LOW)
    start4 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename4),'a+') as log4:
        log4.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start4, addtolog4))
    counter4_label(elapsed4)
    time4.clear()
    time4.wait(float(t4))
    GPIO.output(17, GPIO.HIGH)
    end4 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename4),'a+') as log4:
        log4.writelines('End time: {} \n\n'.format(end4))

def stop_input4(elapsed4):
    global running4 
    global counter4
    running4=False
    counter4=0
    GPIO.output(17, GPIO.HIGH)
    stopreset4 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename4),'a+') as log4:
        log4.writelines('Stop/reset time: {} \n\n'.format(stopreset4))
    time4.set()
    elapsed4['text']='waiting..'
    power4_button['state']='normal'
    stop4_button['state']='disabled'

#Relay 5 functions
def power_input5(elapsed5):
    global t5
    global running5 
    power5_button['state']='disabled'
    stop5_button['state']='normal'
    running5=True
    t5 = e_t5.get()
    GPIO.output(27, GPIO.LOW)
    start5 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename5),'a+') as log5:
        log5.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start5, addtolog5))
    counter5_label(elapsed5)
    time5.clear()
    time5.wait(float(t5))
    GPIO.output(27, GPIO.HIGH)
    end5 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename5),'a+') as log5:
        log5.writelines('End time: {} \n\n'.format(end5))

def stop_input5(elapsed5):
    global running5 
    global counter5
    running5=False
    counter5=0
    GPIO.output(27, GPIO.HIGH)
    stopreset5 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename5),'a+') as log5:
        log5.writelines('Stop/reset time: {} \n\n'.format(stopreset5))
    time5.set()
    elapsed5['text']='waiting..'
    power5_button['state']='normal'
    stop5_button['state']='disabled'

#Relay 6 functions
def power_input6(elapsed6):
    global t6
    global running6
    power6_button['state']='disabled'
    stop6_button['state']='normal' 
    running6=True
    t6 = e_t6.get()
    GPIO.output(22, GPIO.LOW)
    start6 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename6),'a+') as log6:
        log6.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start6, addtolog6))
    counter6_label(elapsed6)
    time6.clear()
    time6.wait(float(t6))
    GPIO.output(22, GPIO.HIGH)
    end6 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename6),'a+') as log6:
        log6.writelines('End time: {} \n\n'.format(end6))

def stop_input6(elapsed6):
    global running6 
    global counter6
    running6=False
    counter6=0
    GPIO.output(22, GPIO.HIGH)
    stopreset6 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename6),'a+') as log6:
        log6.writelines('Stop/reset time: {} \n\n'.format(stopreset6))
    time6.set()
    elapsed6['text']='waiting..'
    power6_button['state']='normal'
    stop6_button['state']='disabled'

#Relay 7 functions
def power_input7(elapsed7):
    global t7
    global running7 
    power7_button['state']='disabled'
    stop7_button['state']='normal'
    running7=True
    t7 = e_t7.get()
    GPIO.output(10, GPIO.LOW)
    start7 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename7),'a+') as log7:
        log7.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start7, addtolog7))
    counter7_label(elapsed7)
    time7.clear()
    time7.wait(float(t7))
    GPIO.output(10, GPIO.HIGH)
    end7 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename7),'a+') as log7:
        log7.writelines('End time: {} \n\n'.format(end7))

def stop_input7(elapsed7):
    global running7 
    global counter7
    running7=False
    counter7=0
    GPIO.output(10, GPIO.HIGH)
    stopreset7 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename7),'a+') as log7:
        log7.writelines('Stop/reset time: {} \n\n'.format(stopreset7))
    time7.set()
    elapsed7['text']='waiting..'
    power7_button['state']='normal'
    stop7_button['state']='disabled'

#Relay 8 functions
def power_input8(elapsed8):
    global t8
    global running8 
    power8_button['state']='disabled'
    stop8_button['state']='normal'
    running8=True
    t8 = e_t8.get()
    GPIO.output(9, GPIO.LOW)
    start8 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename8),'a+') as log8:
        log8.writelines('-' * 50 +'\nStart time: {} \n\n{} \n\n'.format(start8, addtolog8))
    counter8_label(elapsed8)
    time8.clear()
    time8.wait(float(t8))
    GPIO.output(9, GPIO.HIGH)
    end8 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename8),'a+') as log8:
        log8.writelines('End time: {} \n\n'.format(end8))

def stop_input8(elapsed8):
    global running8 
    global counter8
    running8=False
    counter8=0
    GPIO.output(9, GPIO.HIGH)
    stopreset8 = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('%s.txt' % (filename8),'a+') as log8:
        log8.writelines('Stop/reset time: {} \n\n'.format(stopreset8))
    time8.set()
    elapsed8['text']='waiting..'
    power8_button['state']='normal'
    stop8_button['state']='disabled'

#defines counter functions
def counter1_label(elapsed1): 
    def count():
        t1 = e_t1.get()
        if running1: 
            global counter1 
   
            if counter1 <= float(t1):
                remain1 = int(t1) - int(counter1)             
                display=str(remain1)
            else: 
                display="done!" 
  
            elapsed1['text']=display    
            elapsed1.after(1000, count)  
            counter1 += 1
    count()  

def counter2_label(elapsed2): 
    def count():
        t2 = e_t2.get()
        if running2: 
            global counter2 
   
            if counter2 <= float(t2):             
                remain2 = int(t2) - int(counter2)             
                display=str(remain2)
            else: 
                display="done!" 
  
            elapsed2['text']=display    
            elapsed2.after(1000, count)  
            counter2 += 1
    count() 
def counter3_label(elapsed3): 
    def count():
        t3 = e_t3.get()
        if running3: 
            global counter3 
   
            if counter3 <= float(t3):             
                remain3 = int(t3) - int(counter3)             
                display=str(remain3)
            else: 
                display="done!" 
  
            elapsed3['text']=display    
            elapsed3.after(1000, count)  
            counter3 += 1
    count() 
def counter4_label(elapsed4): 
    def count():
        t4 = e_t4.get()
        if running4: 
            global counter4 
   
            if counter4 <= float(t4):             
                remain4 = int(t4) - int(counter4)             
                display=str(remain4)
            else: 
                display="done!" 
  
            elapsed4['text']=display    
            elapsed4.after(1000, count)  
            counter4 += 1
    count() 
def counter5_label(elapsed5): 
    def count():
        t5 = e_t5.get()
        if running5: 
            global counter5 

            if counter5 <= float(t5):
                remain5 = int(t5) - int(counter5)             
                display=str(remain5)
            else: 
                display="done!" 

            elapsed5['text']=display
            elapsed5.after(1000, count)  
            counter5 += 1
    count() 
def counter6_label(elapsed6): 
    def count():
        t6 = e_t6.get()
        if running6: 
            global counter6 
   
            if counter6 <= float(t6):             
                remain6 = int(t6) - int(counter6)             
                display=str(remain6)
            else: 
                display="done!" 
  
            elapsed6['text']=display    
            elapsed6.after(1000, count)  
            counter6 += 1
    count() 
def counter7_label(elapsed7): 
    def count():
        t7 = e_t7.get()
        if running7: 
            global counter7 
   
            if counter7 <= float(t7):             
                remain7 = int(t7) - int(counter7)             
                display=str(remain7)
            else: 
                display="done!" 
  
            elapsed7['text']=display    
            elapsed7.after(1000, count)  
            counter7 += 1
    count() 
def counter8_label(elapsed8): 
    def count():
        t8 = e_t8.get()
        if running8: 
            global counter8 
   
            if counter8 <= float(t8):
                remain8 = int(t8) - int(counter8)
                display=str(remain8)
            else: 
                display="done!" 
  
            elapsed8['text']=display    
            elapsed8.after(1000, count)  
            counter8 += 1
    count() 

#define terminate button function
def terminate_input():
    time1.set()
    time2.set()
    time3.set()
    time4.set()
    time5.set()
    time6.set()
    time7.set()
    time8.set()
    GPIO.cleanup()
    root.quit()

#thread power inputs
def threadpower_input1():
    th.Thread(target=lambda: power_input1(elapsed1)).start()
def threadstop_input1():
    th.Thread(target=lambda: stop_input1(elapsed1)).start()

def threadpower_input2():
    th.Thread(target=lambda: power_input2(elapsed2)).start()
def threadstop_input2():
    th.Thread(target=lambda: stop_input2(elapsed2)).start()

def threadpower_input3():
    th.Thread(target=lambda: power_input3(elapsed3)).start()
def threadstop_input3():
    th.Thread(target=lambda: stop_input3(elapsed3)).start()

def threadpower_input4():
    th.Thread(target=lambda: power_input4(elapsed4)).start()
def threadstop_input4():
    th.Thread(target=lambda: stop_input4(elapsed4)).start()

def threadpower_input5():
    th.Thread(target=lambda: power_input5(elapsed5)).start()
def threadstop_input5():
    th.Thread(target=lambda: stop_input5(elapsed5)).start()

def threadpower_input6():
    th.Thread(target=lambda: power_input6(elapsed6)).start()
def threadstop_input6():
    th.Thread(target=lambda: stop_input6(elapsed6)).start()

def threadpower_input7():
    th.Thread(target=lambda: power_input7(elapsed7)).start()
def threadstop_input7():
    th.Thread(target=lambda: stop_input7(elapsed7)).start()

def threadpower_input8():
    th.Thread(target=lambda: power_input8(elapsed8)).start()
def threadstop_input8():
    th.Thread(target=lambda: stop_input8(elapsed8)).start()

#defines the help box popup and text that appears up pressing Help button
def helppopup():
    popup = tk.Tk()
    popup.wm_title("Help")
    helptext = tk.Label(popup, text = """
    This software is designed by Mackenzie Fahey to run an 8 channel relay.
    I have literally no knowledge on how to code in any near correct manner so this is 
    likely a very messy program but bare with me.

    Each relay channel has three buttons, an entry box and a time remaining label.

    The first thing a user should do is click the Edit Log button to open up the log entry
    for the given relay. The first entry box is for entering the title of the log file and 
    the second box is for entry of the text contents. Upon starting the relay, the program will
    create the file of given name if it does not exist or add to the file if it already exists, 
    it will automatically add the start time and the contents of the second entry box. Once the time 
    has been reached, the file will again be edited with the time it stopped and when the stop/reset
    button is pressed that time is logged as well. The logs are all in the desktop folder.

    The second thing a user should do is enter the time for the experiment (in seconds) into
    the entry box. In the initial design, this would be how long you want the LED to 
    irradiate the sample.

    Once the time is designated, the Start button can be pressed and the relay will complete 
    the circuit. You will notice that the time remaining in seconds will begin counting down. 
    Once 0 is reached the relay will open the circuit.

    If there is nothing or a non-numerical entry in the time entry box and the Start
    button is pressed, the relay will turn on indefintely. Internally, there will be an 
    error due to the conversion of input text from string to float but everything will 
    function as it is designed until the Stop/Reset button is pressed. There will be no
    programmatic way to know how long it has been running due to the design, so you must
    keep track of time yourself if you are going use a relay indefinitely.

    The Stop/Reset button turns off the relay and opens the circuit, this button is designed 
    to be used if there is an experimental issue and the circuit on the given relay needs to 
    be stopped. It also must be used after completion of a run to reset timers. If the relay
    is running indefinitely it will stop it.

    The Terminate button should be used if any of the relays were turned on after opening
    the program, this will reset the relays and close the program. If no relays were open
    they do not need to be reset and the program can be closed normally. 
    """)
    helptext.pack()
    popup.mainloop()

#defines the log file edit pop up and the text boxes
def logfilepopup1():

    def savenquit1():
        global filename1
        global addtolog1
        filename1 = e_filename1.get()
        addtolog1 = e_addtolog1.get('1.0', 'end')
        popup1.destroy()

    popup1 = tk.Tk()
    popup1.wm_title("Relay 1 log")
    e_filename1 = tk.Entry(popup1, width=50, borderwidth=5)
    e_filename1.insert(0, '{}'.format(filename1))
    e_addtolog1 = tk.Text(popup1, width=50, height=20, borderwidth=5)
    e_addtolog1.insert('1.0', '{}'.format(addtolog1))
    savenquitb1 = tk.Button(popup1, text = 'Save and Close', command = savenquit1)
    e_filename1.pack()
    e_addtolog1.pack()
    savenquitb1.pack()
    popup1.mainloop()

def logfilepopup2():

    def savenquit2():
        global filename2
        global addtolog2
        filename2 = e_filename2.get()
        addtolog2 = e_addtolog2.get('1.0', 'end')
        popup2.destroy()

    popup2 = tk.Tk()
    popup2.wm_title("Relay 2 log")
    e_filename2 = tk.Entry(popup2, width=50, borderwidth=5)
    e_filename2.insert(0, '{}'.format(filename2))
    e_addtolog2 = tk.Text(popup2, width=50, height=20, borderwidth=5)
    e_addtolog2.insert('1.0', '{}'.format(addtolog2))
    savenquitb2 = tk.Button(popup2, text = 'Save and Close', command = savenquit2)
    e_filename2.pack()
    e_addtolog2.pack()
    savenquitb2.pack()
    popup2.mainloop()
    
def logfilepopup3():

    def savenquit3():
        global filename3
        global addtolog3
        filename3 = e_filename3.get()
        addtolog3 = e_addtolog3.get('1.0', 'end')
        popup3.destroy()

    popup3 = tk.Tk()
    popup3.wm_title("Relay 3 log")
    e_filename3 = tk.Entry(popup3, width=50, borderwidth=5)
    e_filename3.insert(0, '{}'.format(filename3))
    e_addtolog3 = tk.Text(popup3, width=50, height=20, borderwidth=5)
    e_addtolog3.insert('1.0', '{}'.format(addtolog3))
    savenquitb3 = tk.Button(popup3, text = 'Save and Close', command = savenquit3)
    e_filename3.pack()
    e_addtolog3.pack()
    savenquitb3.pack()
    popup3.mainloop()

def logfilepopup4():

    def savenquit4():
        global filename4
        global addtolog4
        filename4 = e_filename4.get()
        addtolog4 = e_addtolog4.get('1.0', 'end')
        popup4.destroy()

    popup4 = tk.Tk()
    popup4.wm_title("Relay 4 log")
    e_filename4 = tk.Entry(popup4, width=50, borderwidth=5)
    e_filename4.insert(0, '{}'.format(filename4))
    e_addtolog4 = tk.Text(popup4, width=50, height=20, borderwidth=5)
    e_addtolog4.insert('1.0', '{}'.format(addtolog4))
    savenquitb4 = tk.Button(popup4, text = 'Save and Close', command = savenquit4)
    e_filename4.pack()
    e_addtolog4.pack()
    savenquitb4.pack()
    popup4.mainloop()

def logfilepopup5():

    def savenquit5():
        global filename5
        global addtolog5
        filename5 = e_filename5.get()
        addtolog5 = e_addtolog5.get('1.0', 'end')
        popup5.destroy()

    popup5 = tk.Tk()
    popup5.wm_title("Relay 5 log")
    e_filename5 = tk.Entry(popup5, width=50, borderwidth=5)
    e_filename5.insert(0, '{}'.format(filename5))
    e_addtolog5 = tk.Text(popup5, width=50, height=20, borderwidth=5)
    e_addtolog5.insert('1.0', '{}'.format(addtolog5))
    savenquitb5 = tk.Button(popup5, text = 'Save and Close', command = savenquit5)
    e_filename5.pack()
    e_addtolog5.pack()
    savenquitb5.pack()
    popup5.mainloop()

def logfilepopup6():

    def savenquit6():
        global filename6
        global addtolog6
        filename6 = e_filename6.get()
        addtolog6 = e_addtolog6.get('1.0', 'end')
        popup6.destroy()

    popup6 = tk.Tk()
    popup6.wm_title("Relay 6 log")
    e_filename6 = tk.Entry(popup6, width=50, borderwidth=5)
    e_filename6.insert(0, '{}'.format(filename6))
    e_addtolog6 = tk.Text(popup6, width=50, height=20, borderwidth=5)
    e_addtolog6.insert('1.0', '{}'.format(addtolog6))
    savenquitb6 = tk.Button(popup6, text = 'Save and Close', command = savenquit6)
    e_filename6.pack()
    e_addtolog6.pack()
    savenquitb6.pack()
    popup6.mainloop()

def logfilepopup7():

    def savenquit7():
        global filename7
        global addtolog7
        filename7 = e_filename7.get()
        addtolog7 = e_addtolog7.get('1.0', 'end')
        popup7.destroy()

    popup7 = tk.Tk()
    popup7.wm_title("Relay 7 log")
    e_filename7 = tk.Entry(popup7, width=50, borderwidth=5)
    e_filename7.insert(0, '{}'.format(filename7))
    e_addtolog7 = tk.Text(popup7, width=50, height=20, borderwidth=5)
    e_addtolog7.insert('1.0', '{}'.format(addtolog7))
    savenquitb7 = tk.Button(popup7, text = 'Save and Close', command = savenquit7)
    e_filename7.pack()
    e_addtolog7.pack()
    savenquitb7.pack()
    popup7.mainloop()

def logfilepopup8():

    def savenquit8():
        global filename8
        global addtolog8
        filename8 = e_filename8.get()
        addtolog8 = e_addtolog8.get('1.0', 'end')
        popup8.destroy()

    popup8 = tk.Tk()
    popup8.wm_title("Relay 8 log")
    e_filename8 = tk.Entry(popup8, width=50, borderwidth=5)
    e_filename8.insert(0, '{}'.format(filename8))
    e_addtolog8 = tk.Text(popup8, width=50, height=20, borderwidth=5)
    e_addtolog8.insert('1.0', '{}'.format(addtolog8))
    savenquitb8 = tk.Button(popup8, text = 'Save and Close', command = savenquit8)
    e_filename8.pack()
    e_addtolog8.pack()
    savenquitb8.pack()
    popup8.mainloop()

#defines headers or labels
header_index = tk.Label(root, text='Index')
header_power = tk.Label(root, text='Relay Execution')
header_t = tk.Label(root, text='Run time / s')
header_elapsed = tk.Label(root, text='Time remaining / s')
header_terminate = tk.Label(root, text='To reset GPIO and relays, must close program through button below!')

#define Relays index labels
index1 = tk.Label(root, text='Relay 1')
index2 = tk.Label(root, text='Relay 2')
index3 = tk.Label(root, text='Relay 3')
index4 = tk.Label(root, text='Relay 4')
index5 = tk.Label(root, text='Relay 5')
index6 = tk.Label(root, text='Relay 6')
index7 = tk.Label(root, text='Relay 7')
index8 = tk.Label(root, text='Relay 8')

#defines GUI for log file edit to pop up the entry boxes
openlogfile1 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup1)
openlogfile2 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup2)
openlogfile3 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup3)
openlogfile4 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup4)
openlogfile5 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup5)
openlogfile6 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup6)
openlogfile7 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup7)
openlogfile8 = tk.Button(root, text="Edit Log", padx=40, pady=20, command=logfilepopup8)

#defines GUI for relay opening buttons
power1_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input1)
power2_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input2)
power3_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input3)
power4_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input4)
power5_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input5)
power6_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input6)
power7_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input7)
power8_button = tk.Button(root, text="Start", padx=40, pady=20, fg='green', command=threadpower_input8)

#defines GUI for relay stop buttons
stop1_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input1)
stop2_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input2)
stop3_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input3)
stop4_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input4)
stop5_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input5)
stop6_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input6)
stop7_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input7)
stop8_button = tk.Button(root, text="Stop/Reset", padx=40, pady=20, fg='red', command=threadstop_input8)

#defines initial button states
power1_button['state']='normal'
stop1_button['state']='disabled'
power2_button['state']='normal'
stop2_button['state']='disabled'
power3_button['state']='normal'
stop3_button['state']='disabled'
power4_button['state']='normal'
stop4_button['state']='disabled'
power5_button['state']='normal'
stop5_button['state']='disabled'
power6_button['state']='normal'
stop6_button['state']='disabled'
power7_button['state']='normal'
stop7_button['state']='disabled'
power8_button['state']='normal'
stop8_button['state']='disabled'

#define GUI input boxes for runtime for each relay in seconds 
e_t1 = tk.Entry(root, width=10, borderwidth=5)
e_t2 = tk.Entry(root, width=10, borderwidth=5)
e_t3 = tk.Entry(root, width=10, borderwidth=5)
e_t4 = tk.Entry(root, width=10, borderwidth=5)
e_t5 = tk.Entry(root, width=10, borderwidth=5)
e_t6 = tk.Entry(root, width=10, borderwidth=5)
e_t7 = tk.Entry(root, width=10, borderwidth=5)
e_t8 = tk.Entry(root, width=10, borderwidth=5)

#defines time elapsed labels for each relay presented in seconds
elapsed1 = tk.Label(root, text='waiting..')
elapsed2 = tk.Label(root, text='waiting..')
elapsed3 = tk.Label(root, text='waiting..')
elapsed4 = tk.Label(root, text='waiting..')
elapsed5 = tk.Label(root, text='waiting..')
elapsed6 = tk.Label(root, text='waiting..')
elapsed7 = tk.Label(root, text='waiting..')
elapsed8 = tk.Label(root, text='waiting..')

#defines button for termination and GPIO cleanup
terminate_button = tk.Button(root, text="Terminate Program", padx=80, pady=20, borderwidth=5, fg='red', command=terminate_input)

#defines help pop up GUI
help_button= tk.Button(root, text="HELP", command=helppopup)

#creates GUI
header_index.grid(row=0, column=0)
header_power.grid(row=0, column =1, columnspan=3)
header_t.grid(row=0,column=4)
header_elapsed.grid(row=0,column=5)

index1.grid(row=1, column=0)
openlogfile1.grid(row=1,column=1)
power1_button.grid(row=1, column=2)
stop1_button.grid(row=1, column=3)
e_t1.grid(row=1, column=4)
elapsed1.grid(row=1, column=5)

index2.grid(row=2, column=0)
openlogfile2.grid(row=2,column=1)
power2_button.grid(row=2, column=2)
stop2_button.grid(row=2, column=3)
e_t2.grid(row=2, column=4)
elapsed2.grid(row=2, column=5)

index3.grid(row=3, column=0)
openlogfile3.grid(row=3,column=1)
power3_button.grid(row=3, column=2)
stop3_button.grid(row=3, column=3)
e_t3.grid(row=3, column=4)
elapsed3.grid(row=3, column=5)

index4.grid(row=4, column=0)
openlogfile4.grid(row=4,column=1)
power4_button.grid(row=4, column=2)
stop4_button.grid(row=4, column=3)
e_t4.grid(row=4, column=4)
elapsed4.grid(row=4, column=5)

index5.grid(row=5, column=0)
openlogfile5.grid(row=5,column=1)
power5_button.grid(row=5, column=2)
stop5_button.grid(row=5, column=3)
e_t5.grid(row=5, column=4)
elapsed5.grid(row=5, column=5)

index6.grid(row=6, column=0)
openlogfile6.grid(row=6,column=1)
power6_button.grid(row=6, column=2)
stop6_button.grid(row=6, column=3)
e_t6.grid(row=6, column=4)
elapsed6.grid(row=6, column=5)

index7.grid(row=7, column=0)
openlogfile7.grid(row=7,column=1)
power7_button.grid(row=7, column=2)
stop7_button.grid(row=7, column=3)
e_t7.grid(row=7, column=4)
elapsed7.grid(row=7, column=5)

index8.grid(row=8, column=0)
openlogfile8.grid(row=8,column=1)
power8_button.grid(row=8, column=2)
stop8_button.grid(row=8, column=3)
e_t8.grid(row=8, column=4)
elapsed8.grid(row=8, column=5)

header_terminate.grid(row=9,column=0,columnspan=6)

terminate_button.grid(row=10, column=0, columnspan=6)

help_button.grid(row=11, column =0, columnspan=6)


root.mainloop()
