# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:40:46 2018

@author: rushad
"""

from tkinter import *
def res():
    
    num_str = str(e1.get())	
    num_len = len(str(e1.get()))
    var_holder = {}

    res_list = [10, 100, 1000, 10000, 100000, 1000000, 11, 110, 1100, 11000, 110000, 100000, 12, 120, 1200, 12000, 120000, 1200000, 13, 130, 1300, 13000, 130000, 1300000, 15, 150, 1500, 15000, 150000, 1500000, 16, 160, 1600, 16000, 160000, 1600000, 18, 180, 1800, 18000, 180000, 1800000, 20, 200, 2000, 20000, 200000, 2000000, 22, 220, 2200, 22000, 220000, 2200000, 24, 240, 2400, 24000, 240000, 2400000, 27, 270, 2700, 27000, 270000, 2700000, 30, 300, 3000, 30000, 300000, 3000000, 33, 330, 3300, 33000, 330000, 3300000, 36, 360, 3600, 36000, 360000, 3600000, 39, 390, 3900, 39000, 390000, 3900000, 43, 430, 4300, 43000, 430000, 4300000, 47, 470, 4700, 47000, 470000, 4700000, 51, 510, 5100, 51000, 510000, 5000000, 56, 560, 5600, 56000, 560000, 5600000, 62, 620, 6200, 62000, 620000, 6200000, 68, 680, 6800, 68000, 680000, 6800000, 75, 750, 7500, 75000, 750000, 7500000, 82, 820, 8200, 82000, 820000, 8200000, 91, 910, 9100, 91000, 910000, 900000 ]

    if (int(e1.get()) in res_list):
        for i in range(num_len):
            var_holder[i] = num_str[i]
        lat = str(e1.get()[2:]) 

        for i in range(2):
                if (int(var_holder[i]) == 0):
                        print("BLACK ")
                elif (int(var_holder[i]) == 1):
                        print("BROWN ")
                elif (int(var_holder[i]) == 2):
                        print("RED ")
                elif (int(var_holder[i]) == 3):
                        print("ORANGE ")
                elif (int(var_holder[i]) == 4):
                        print("YELLOW ")
                elif (int(var_holder[i]) == 5):
                        print("GREEN ")
                elif (int(var_holder[i]) == 6):
                        print("BLUE ")
                elif (int(var_holder[i]) == 7):
                        print("VIOLET ")
                elif (int(var_holder[i]) == 8):
                        print("GRAY ")
                elif (int(var_holder[i]) == 9):
                        print("WHITE ")


        if (lat == str()):
                print("BLACK ")
        elif (lat == str(0)):
                print("BROWN ")
        elif (lat == str(0) + str(0)):
                print("RED ")
        elif (lat == str(0) + str(0) + str(0)):
                print("ORANGE ")
        elif (lat == str(0) + str(0) + str(0) + str(0)):
                print("YELLOW ")
        elif (lat == str(0) + str(0) + str(0) + str(0) + str(0)):
                print("GREEN ")
        elif (lat == str(0) + str(0) + str(0) + str(0) + str(0) + str(0)):
                print("BLUE ")
        elif (lat == str(0) + str(0) + str(0) + str(0) + str(0) + str(0) + str(0)):
                print("VIOLET ")
        elif (lat == str(0) + str(0) + str(0) + str(0) + str(0) + str(0) + str(0) + str(0)):
                print("GRAY ")
        elif (lat == str(0) + str(0) + str(0) + str(0) + str(0) + str(0) + str(0) + str(0) + str(0)):
                print("WHITE ")

	
    else :
        print("The value you entered is incorrect. Please renter a valid value. ")

    print("\n")

master = Tk()
text = Text(master)
Label(master, text="Resistance value").grid(row=0)

e1 = Entry(master)


e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=res).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )


