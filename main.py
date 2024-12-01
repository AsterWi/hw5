#created 1st of december 2024

import requests
import colorama

#this library makes the terminal output things in different colors.
clr = colorama

#there this method i think it fixes console
clr.just_fix_windows_console
#this also bring ANSI to windows
clr.AnsiToWin32

#its __name__ is colorama
print(colorama.__name__)
print(clr.__name__)

#there a lot of methods in it
for method in dir(colorama):
    print(method)

#this use printing variables to change text colors
#these variable Back to change background color, Style to change thickness of text and Fore changes text color
print(clr.Back.BLUE, clr.Style.DIM, clr.Fore.RED, "oguh")
#when i do this, the rest of the text in terminal keeps the changes
#So i use this to reset everything to normal.
print(clr.Style.RESET_ALL,"fodsj")
#it has many colors
print(clr.Fore.BLACK, "hello")
print(clr.Fore.RED, "hello")
print(clr.Fore.GREEN, "hello")
print(clr.Fore.BLUE, "hello")
print(clr.Fore.MAGENTA, "hello")
print(clr.Fore.CYAN, "hello")
print(clr.Fore.YELLOW, "hello")
print(clr.Fore.WHITE, "hello")

#green is an attribute. all the colors are attribute
print(hasattr(clr.Fore, "GREEN"))

#this looks very useful for inside terminal programs. it will really make it look cool. 
#It will also be useful for bug checking, make the error have clr.Fore.RED and its easy to find





