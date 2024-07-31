



from tkinter import *
from tkinter import messagebox
from random import choice as ch 
from PIL import Image, ImageTk
import imageio

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("780x580")

frame1 = Frame(root, bg='#E3FEF7')  
frame2 = Frame(root, bg='#E3FEF7')  

frame1.grid(row=0, column=0, sticky='nsew')
frame2.grid(row=0, column=0, sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame1.grid_rowconfigure(0, weight=1)
frame1.grid_rowconfigure(1, weight=1)
frame1.grid_rowconfigure(2, weight=1)
frame1.grid_rowconfigure(3, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(2, weight=1)

frame2.grid_rowconfigure(0, weight=1)
frame2.grid_rowconfigure(1, weight=1)
frame2.grid_rowconfigure(2, weight=1)
frame2.grid_rowconfigure(3, weight=1)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
frame2.grid_columnconfigure(2, weight=1)

rps = ["rock", "paper", "scissor"]
user_choice = None

def show_frame(frame):
    frame.tkraise()

def set_user_choice(choice):
    global user_choice
    user_choice = choice
    messagebox.showinfo("Your Choice", f"You chose {choice.capitalize()}!")
    show_frame(frame2)

def shoot():
    global user_choice
    if user_choice is None:
        messagebox.showwarning("No Choice", "Please select Rock, Paper, or Scissors before shooting.")
        show_frame(frame2)
        return
    
    random_choice = ch(rps)
    if random_choice == user_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and random_choice == "scissor") or \
         (user_choice == "paper" and random_choice == "rock") or \
         (user_choice == "scissor" and random_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    messagebox.showinfo("Result", f"Computer chose {random_choice.capitalize()}. {result}")
    user_choice = None  
    show_frame(frame2)

first_label = Label(frame1, text='Welcome! To Rock Paper Scissor game', fg='black', bg='#E3FEF7', font=("sans 16 bold", 18))
first_label.grid(row=0, column=0, columnspan=3, pady=20)

rock_image = PhotoImage(file="rock.png")
rock_label = Label(frame1, image=rock_image, bg='#E3FEF7')  
rock_label.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

paper_image = PhotoImage(file="paper.png")
paper_label = Label(frame1, image=paper_image, bg='#E3FEF7')  
paper_label.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

scissor_image = PhotoImage(file="scissor.png")
scissor_label = Label(frame1, image=scissor_image, bg='#E3FEF7')  
scissor_label.grid(row=1, column=2, padx=20, pady=20, sticky='nsew')

button_go_to_frame2 = Button(frame1, text="Go to Shoot Page", command=lambda: show_frame(frame2), width=30, fg='#FFFFFF', bg='#87CEEB', relief='groove', activebackground='#B0E0E6', font=12)  
button_go_to_frame2.grid(row=2, column=0, columnspan=3, pady=20)

button_rock = Button(frame2, text="Rock", command=lambda: set_user_choice("rock"), width=30, fg='#FFFFFF', bg='#87CEEB', relief='groove', activebackground='#B0E0E6', font=("sans 16 bold", 10))  
button_rock.grid(row=0, column=0, pady=10)

button_paper = Button(frame2, text="Paper", command=lambda: set_user_choice("paper"), width=30, fg='#FFFFFF', bg='#87CEEB', relief='groove', activebackground='#B0E0E6', font=("sans 16 bold", 10))  
button_paper.grid(row=0, column=1, pady=10)

button_scissor = Button(frame2, text="Scissor", command=lambda: set_user_choice("scissor"), width=30, fg='#FFFFFF', bg='#87CEEB', relief='groove', activebackground='#B0E0E6', font=("sans 16 bold", 10)) 
button_scissor.grid(row=0, column=2, pady=10)

button_shoot = Button(frame2, text="Shoot", command=shoot, width=30, fg='#FFFFFF', bg='#87CEEB', relief='groove', activebackground='#B0E0E6', font=("sans 16 bold", 10))  
button_shoot.grid(row=4, column=0, columnspan=3, pady=20)

button_go_to_frame1 = Button(frame2, text="Go back to Main Page", command=lambda: show_frame(frame1), width=30, fg='#FFFFFF', bg='#87CEEB', relief='groove', activebackground='#B0E0E6', font=("sans 16 bold", 10))  
button_go_to_frame1.grid(row=8, column=0, columnspan=3, pady=20)

gif_label = Label(frame2, bg='#E3FEF7')
gif_label.grid(row=3, column=0, columnspan=3, pady=20)

def update_frame(frame_number):
    frame_image = frames[frame_number]
    gif_label.configure(image=frame_image)
    root.after(100, update_frame, (frame_number + 1) % len(frames))

frames = []
gif_path = "anima-rps.mp4"
gif = imageio.get_reader(gif_path)
for frame in gif:
    frame_image = Image.fromarray(frame).resize((780, 350))
    frame_image = ImageTk.PhotoImage(frame_image)
    frames.append(frame_image)

update_frame(0)

show_frame(frame1)

root.mainloop()