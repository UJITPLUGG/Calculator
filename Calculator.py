import tkinter as tk
from functools import partial


root = tk.Tk()
buttons = []
size = 4
buttons_text = ["0","C","DEL","/",
		"7","8","9","*",
		"4","5","6","-",
		"1","2","3","+",
		"(",")",".","="]


def calculate(button_pressed,Label):
	try:
		if button_pressed == "DEL":
			Label["text"] = Label["text"][:-1]
		elif button_pressed == "C":
			Label["text"] = ""
		elif button_pressed == "=":
			exec(f'Label["text"] = str(round({Label["text"]},8))')
		else:
			Label["text"] += button_pressed
		if not any(Label["text"][0] == str(x) for x in range(1,10)):
			Label["text"] = ""
	except:
		Label["text"] = ""

def main():
	Label = tk.Label(root,font=("TimesNewRoman", 20),height=1,padx=10,pady=10,relief="flat",text="")
	Label.grid(column=0,row=0,columnspan=4)
		
	for x in range(size+1):
		for y in range(size):
			buttons.append(tk.Button(root,text=f"{buttons_text[size*x+y]}",font=("TimesNewRoman", 20),background="#00ffdd",relief="groove",height=2,width=4,command=partial(calculate,buttons_text[size*x+y],Label)))
			buttons[size*x+y].grid(column=y,row=x+1)
	root.resizable(False, False)
	root.mainloop()


if __name__ == "__main__":
	main()
