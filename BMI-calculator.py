import tkinter as tk

def calculate():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    height = height/100 #for convert into meter

    bmi = weight/(height*height)
    bmi_result.config(text="Your BMI: {:.2f}".format(bmi))
    if bmi <=18.4:
        status.config(text="Status : Underweight", fg="#FFD95A")
    elif bmi > 18.5 and bmi < 24.9:
        status.config(text="Status : Normal", fg="#33ffce")
    elif bmi > 25.0 and bmi < 39.9:
        status.config(text="Status : Overweight", fg="#E57C23")
    else:
        status.config(text="Status : Obese", fg="#F45050")

def clear():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

bg_color = "#2A3457"
fg_color = "#F2EAED"

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x400")
window.config(bg=bg_color)
window.resizable(0,0)

#create the labels
label_weight = tk.Label(window, text="Weight (kg) :", font=("Rockwell", 15, "bold"),
                        bg=bg_color, fg=fg_color)
label_weight.pack(pady=10)

entry_weight = tk.Entry(window, font=("Rockwell", 15))
entry_weight.pack()

label_height = tk.Label(window, text="Height (cm) :", font=("Rockwell", 15, "bold"),
                        bg=bg_color, fg=fg_color)
label_height.pack(pady=15)

entry_height = tk.Entry(window, font=("rockwell", 15))
entry_height.pack()

#create a frame for buttons
frame = tk.Frame(window)
frame.config(bg=bg_color)
frame.pack(pady=30)

calculate_button = tk.Button(frame, text="Calculate", font=("Rockwell", 15), activebackground=bg_color,
                             activeforeground=fg_color, command=calculate)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(frame, text="clear", font=("Rockwell", 15), activebackground=bg_color,
                             activeforeground=fg_color, command=clear)
clear_button.grid(row=0, column=1, padx=10)

#create label for the result
bmi_result = tk.Label(window,text="", font=("Rockwell", 18), bg=bg_color,fg=fg_color)
bmi_result.pack()

status = tk.Label(window, text="", font=("Rockwell", 18), bg=bg_color)
status.pack(pady=10)

window.mainloop()
