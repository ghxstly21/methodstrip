from tkinter import *
from tkinter import filedialog
from pathlib import Path
from time import perf_counter

SUPPORTED_LANGUAGES: tuple[str,str] = (".java", ".js")

def validate_file():
    path: str = filedialog.askopenfilename()
    extension: str = Path(path).suffix
    if not extension:
        return
    if extension in SUPPORTED_LANGUAGES:
        print(f"Valid! Extension is {extension}")
    else:
        print(f"Invalid! Extension is {extension}")
        # display error label



def main():
    window = Tk()
    bg_color = "#b4d6b9"
    window.geometry("420x420")
    window.title("MethodStrip")

    icon = PhotoImage(file = "images/methodstrip_logo.png")
    window.iconphoto(True, icon)
    window.config(background = bg_color)

    title = Label(window,
                  text="MethodStrip",
                  font=('Courier New', 40, 'bold'),
                  bg=bg_color,
                  fg="black",
                  relief="raised",
                  bd=10)
    title.place(x=210, y=105)
    info_text = Label(window,
                      text="A tool to empty your Java/JS methods.",
                      font=('Courier New', 20),
                      bg=bg_color,
                      fg="black")
    info_text.place(x=210, y= 210)

    save_options: list[str] = ["Save as a copy in same folder as the original", "Overwrite existing file with stripped version"]
    save_choice = IntVar()
    for i in range(len(save_options)):
        radio_button = Radiobutton(window, text=save_options[i], variable=save_choice, value=i)
        radio_button.place(x=210, y=240 + i * 24)
    note = Label(window,
                 text="Note: Your stripped file will be saved as a copy in the same folder as the original",
                 font=("Courier New", 10),
                 bg= "white",
                 fg="black")
    note.place(x=210, y= 240)

    upload_button = Button(
        text="Upload a file...",
        command=validate_file,
        font=("Courier New", 15))
    upload_button.place(x=210, y=300)

    window.mainloop()

if __name__ == "__main__":
    main()
