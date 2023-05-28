from tkinter import *

root = Tk()
root.title("Pizzaold's fond calculator")
root.maxsize(1000, 1000)
root.config(bg='light grey')
root.resizable(width=False, height=False)

input_frame = Frame(root, width=500, height=400, bg='grey')
input_frame.grid(row=0, column=0, padx=10, pady=5)

output_frame = Frame(root, width=500, height=400, bg='grey')
output_frame.grid(row=1, column=0, padx=10, pady=5)

def calculation():
    for i in range(1, 6):
        try:
            mid_of_growth = 0
            for j in range(2, 5):
                mid_of_growth += float(inputs.grid_slaves(row=j, column=i)[0].get()) / 3
            for j in range(5, 7):
                mid_of_growth -= float(inputs.grid_slaves(row=j, column=i)[0].get())
            result = round(float(inputs.grid_slaves(row=1, column=i)[0].get()) * (mid_of_growth / 100), 3)
            Label(output_frame, text=result, bg="grey").grid(row=1, column=i, padx=5, pady=5, sticky='wens')
        except ValueError:
            Label(output_frame, text="Invalid input", bg="grey").grid(row=1, column=i, padx=5, pady=5, sticky='wens')

Label(input_frame, text="Input", bg="grey").grid(row=0, column=0, padx=5, pady=5)

inputs = Frame(input_frame, width=180, height=185, bg='grey')
inputs.grid(row=2, column=0, padx=5, pady=5)

for i in range(1, 6):
    Label(inputs, text="Fond " + str(i), bg="grey").grid(row=0, column=i, padx=5, pady=5, sticky='wens')

for i in range(1, 6):
    Label(output_frame, text="Fond " + str(i), bg="grey").grid(row=0, column=i, padx=5, pady=5, sticky='wens')

for i in range(1, 6):
    for j in range(1, 7):
        Entry(inputs).grid(row=j, column=i, padx=5, pady=5, sticky='wens')

Label(inputs, text="Sum in fond (€)", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky='wens')
Label(inputs, text="Current month growth (%)", bg="grey").grid(row=2, column=0, padx=5, pady=5, sticky='wens')
Label(inputs, text="Last month growth (%)", bg="grey").grid(row=3, column=0, padx=5, pady=5, sticky='wens')
Label(inputs, text="Last last month growth (%)", bg="grey").grid(row=4, column=0, padx=5, pady=5, sticky='wens')
Label(inputs, text="maintenance fee (%)", bg="grey").grid(row=5, column=0, padx=5, pady=5, sticky='wens')
Label(inputs, text="administration fee (%)", bg="grey").grid(row=6, column=0, padx=5, pady=5, sticky='wens')

Button(inputs, text="Calculate", relief="raise", command=calculation).grid(row=7, column=5, padx=5, pady=5, sticky='wens')

Label(output_frame, text="Overall growth/loss", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky='wens')

root.mainloop()
