#import modules
import tkinter as tk
import tkinter.font as font
import random

#def variables
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*" #valid characters to choose from
#i mostly chose these based upon what users would find convenient to type. personally i'm not a fan of using
#parentheses in my passwords. same with periods, semi colons, commas, the work
i = 0 #thing that goes up during the while looping for length
q = 0 #thing that goes up while looping for number
length = 0 #length of the pw, user input
num = 0 #how many pws the user wants to generate

#funct
def passGen():
    errorEntry.delete(0, tk.END) #clearing any old errors for those on a retry
    try: #check to make sure people input a valid integer for length
        length = int(lenText.get())
    except: #generates an error message
        errorEntry.grid(row = 4, column = 0, columnspan=2, pady = 10, padx = 10)
        errorEntry.insert(tk.END,"error: invalid 'length' entry. ")
    try: #check to make sure people input a valid integer for number of...
        num = int(numText.get())
    except: #generates error messages
        errorEntry.grid(row = 4, column = 0, columnspan=2, pady = 10, padx = 10)
        errorEntry.insert(tk.END,"error: invalid 'number of' entry. ")

    password = "" #set to nothing so this program works
    pwText.delete(1.0,tk.END) #clears old passwords
    for q in range(num): #this for loop focuses on making a certain number of passwords
        for i in range(length): #while this for loop focuses on making one password a certain length, as well as randomly generating the contents
            password += random.choice(chars)
        n = str(q + 1) #to print password number
        password = "\n " + n + ". " + password
        pwText.insert(tk.END, password) #prints a password
        password = "" #resets password variable so the i for loop works right on 2nd, 3rd, ..., nth recursions

#GUI define

# window

window = tk.Tk()
window.title("password generator for absolute babies.")
window.geometry("780x700")

#fonts
labelFont = font.Font(
    size = 12,
)

titleFont = font.Font(
    size = 18,
    weight = "bold"
)

buttonFont = font.Font(
    size = 12,
    weight = "bold"
)

#main

main = tk.Frame(
    width = 400,
    bg = "linen",
    master=window
)

mainLabel = tk.Label(
    text = "welcome to august kun's funkalicious password generator",
    master = main,
    bg = "linen",
    fg = "rosybrown3",
    font= titleFont
)
#controls the GUI of the section pertaining to number of generations entry
numDiv = tk.Frame(
    width = 30,
    bg = "linen",
    master=main
)
numLabel = tk.Label(
    text="# of passwords",
    bg = "linen",
    fg = "plum3",
    width = 30,
    font = labelFont,
    master = numDiv
)
numText = tk.Entry(
    width = 10,
    fg = "plum3",
    master = numDiv
)

#controls the GUI of the section pertaining to the length entry
lenDiv = tk.Frame(
    width = 30,
    bg = "linen",
    master=main
)
lenLabel = tk.Label(
    text= "length of password(s)",
    bg = "linen",
    fg = "plum3",
    width = 30,
    font = labelFont,
    master=lenDiv
)
lenText = tk.Entry(
    width = 10,
    fg = "plum3",
    master=lenDiv
)

# other

buttonGenerate = tk.Button(
    text = "generate",
    master = main,
    fg = "plum3",
    bg = "lavender blush",
    activebackground = "misty rose",
    activeforeground = "plum3",
    font = buttonFont,
    command = passGen
)
pwText = tk.Text(
    width = 75,
    fg = "rosybrown3",
    master = main
)
errorEntry = tk.Entry(
    width = 75,
    master = main,
    fg = "plum3",
) #hidden until there's an actual error

#loop and such

#run GUI
main.pack(fill=tk.BOTH, expand=True)
mainLabel.grid(row = 0, column = 0, columnspan=2, pady = 20, padx = 50)
lenDiv.grid(row=1,column=0,sticky="n")
lenLabel.pack(pady=5)
lenText.pack(pady=10)
numDiv.grid(row=1,column=1,sticky="n")
numLabel.pack(pady=5)
numText.pack(pady=10)
pwText.grid(row = 2, column = 0, columnspan=2, padx = 20)
buttonGenerate.grid(row = 3, column = 0, columnspan=2, pady = 10, padx = 10)
window.mainloop()
