import tkinter as tk
def mouse_click(event):
    print(event.x,event.y)

root = tk.Tk()
canvas = tk.Canvas(root,width=300, height=300)
canvas.bind("<Button-1>",mouse_click)

#button = tk.Button(root, text="Click me!")
#button.pack()
#button = tk.Button(root, text="Click me!")
#button.pack()

root.mainloop()