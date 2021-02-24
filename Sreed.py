#!/usr/bin/env python
# coding: utf-8

# 24th February,2021

# This will be the prototype application named "Sreed". This will be a training application for speed reading. We will need a pdf book of anykind.

# In[1]:


#First we need to import all the libraries
from tkinter import *
from tkinter import messagebox
from PyPDF2 import PdfFileReader
import time

#Initialize the window 
window = Tk()
window.minsize(500, 500)
window.title('Sreed (Read in a pace to learn faster)')
window.iconbitmap('icon.bmp')

stop_called = False

#All the Functions will be below
def break_words(text):
    '''This will be the splitter of words of a single page and give a list of word'''
    text_to_string = str(text)
    text_to_string = text_to_string.replace('\n', ' ')
    word_list = text_to_string.split(' ')
    return word_list

#time.sleep(time_for_one_word)

def time_per_word(words_per_minute, num_of_words):
    '''This is the calculating function of the time required for single word which will determine the sleep time in sec'''
    time_for_a_word = 60 * num_of_words / words_per_minute
    return time_for_a_word

def start_process():
    global stop_called
    stop_called = False
    '''Thiw is the main function for wiring up of gui and back end functions'''
    #print('start_process being called')
    stop_button.config(state=ACTIVE)
    start_button.config(state=DISABLED)
    #Here we will wire up all the widgets
    try:
        if file_path_text.get() == '' or page_number_text.get() == '' or wpm_text.get() == '':
            messagebox.showerror('Requires fields','You have not filled all the required entries. Please give all the input properly')
            return
        pdf = PdfFileReader(file_path_text.get()) #wiring up the pdf to open
        page_num = int(page_number_text.get()) #wiring up the page number to load
        wpm = int(wpm_text.get()) #wiring up the word per minute to calculate
        num_of_words = int(nwt_integer.get()) #wiring up the number of words at a time to show
        if num_of_words != 1 and num_of_words != 2 and num_of_words != 3:
            num_of_words = 1
        pageObj = pdf.getPage(page_num-1) #wiring up the page and load it
        txt = pageObj.extractText() #converting the page elements into texts
        words_list = break_words(txt) #Now let's break the text
        time_for_aword = time_per_word(wpm, num_of_words)
        print(words_list)
        if len(words_list) == 1:
            messagebox.showerror('File error','Either your file is not readable or you did not put the correct path with file name')
            return
        
        i=0
        while i < len(words_list):
            if stop_called == False:
                word = ''
                for j in range(num_of_words):
                    word += words_list[i+j] + ' '
                i += num_of_words
                read_word_label.config(text=word)
                read_word_label.update()
                time.sleep(time_for_aword)
                
            else:
                break

    except IndexError:
        pass
    stop_button.config(state=DISABLED)
    start_button.config(state=ACTIVE)    

def stop_process():
    print('stop_process being called')
    global stop_called 
    stop_called = True
    read_word_label.config(text="Read Here")
    read_word_label.update()
    stop_button.config(state=DISABLED)
    start_button.config(state=ACTIVE)
    
#File Path
file_path_text = StringVar()
file_path_label = Label(window, text='Please give the pdf file path: ', font=('bold', 10), pady=10)
file_path_label.grid(row=0, column=0, sticky=W)
file_path_entry = Entry(window, textvariable=file_path_text, width=100)
file_path_entry.grid(row=0, column=1)

#Page Number
page_number_text = StringVar()
page_number_label = Label(window, text='Please give the page number, you want to read: ', font=('bold', 10), pady=10)
page_number_label.grid(row=1, column=0, sticky=W)
page_number_entry = Entry(window, textvariable=page_number_text, width=10)
page_number_entry.grid(row=1, column=1)

#Words Per Minute
wpm_text = StringVar()
wpm_label = Label(window, text='Please give desired word per minute in integer: ', font=('bold', 10), pady=10)
wpm_label.grid(row=1, column=2, sticky=W)
wpm_entry = Entry(window, textvariable=wpm_text, width=10)
wpm_entry.grid(row=1, column=3)

#Number of Words at a Time
nwt_integer = IntVar()
one_word_radiob = Radiobutton(window, text="One word at a time(Default)", state=ACTIVE, variable=nwt_integer, value=1)
one_word_radiob.grid(row=2, column=0)
two_word_radiob = Radiobutton(window, text="Two words at a time", state=NORMAL, variable=nwt_integer, value=2)
two_word_radiob.grid(row=2, column=1)
three_word_radiob = Radiobutton(window, text="Three words at a time", state=NORMAL, variable=nwt_integer, value=3)
three_word_radiob.grid(row=2, column=2)

#Start and Stop Button
start_button = Button(window, text="Start", state=ACTIVE, command=start_process)
start_button.grid(row=3, column=1)
stop_button = Button(window, text="Stop", state=DISABLED, command=stop_process)
stop_button.grid(row=3, column=2)

#Word Showing Label
read_word_label = Label(window, text="Read Here", font=('bold', 20), width=30 , pady=100, bg='#ffffff')
read_word_label.grid(row=4, column=1)

window.mainloop()

#To Install use either these two lines
#pyinstaller Sreed.ipynb --oneflie --windowed
#pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' Sreed.ipynb


# In[ ]:




