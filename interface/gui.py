import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("dark-blue") 

def deploy_images():
    path = tk.filedialog.askopenfilename()
    return path


app = ctk.CTk()

app.title("Face Recognition System")
app.geometry("800x600")

button = ctk.CTkButton(app, text="Deploy Image", command=deploy_images)
button.place(relx=0.5, rely=0.5, anchor="center")




app.mainloop()