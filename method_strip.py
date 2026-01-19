from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path
from time import perf_counter

SUPPORTED_LANGUAGES: tuple = (".java", ".js")
stack = []


def get_words(path: Path):
    with open(path, "r") as original:
        for line in original:
            for word in line.split():
                yield word


def strip_with_copy(original_path: Path, new_path: Path):
    with open(new_path, "x") as new:
        match original_path.suffix:
            case ".java":
                for word in get_words(original_path):
                    ...
            case ".js":
                for word in get_words(original_path):
                    if word == "function":
                        ...




def strip_in_place(original_path: Path, new_path: Path):
    ...

def strip_methods(original_path: Path, save_choice : IntVar):
    start = perf_counter()
    match save_choice:
        case 0:
            new_path: Path = original_path.parent/f"{original_path.stem}_stripped{original_path.suffix}"
            i = 2 # Number the file name if it already exists
            while new_path.exists():
                new_path = original_path.parent/f"{original_path.stem}_stripped{i}{original_path.suffix}"
                i += 1
            strip_with_copy(original_path, new_path)
        case 1:
            new_path: Path = original_path
            strip_in_place(original_path, new_path)


    end = perf_counter()

    elapsed = end - start

def validate_file(save_choice: IntVar):
    path_str = filedialog.askopenfilename()
    if not path_str:
        return
    path: Path = Path(path_str)
    extension: str = path.suffix
    if extension in SUPPORTED_LANGUAGES:
        strip_methods(path, save_choice)
    else:
        messagebox.showerror(title="Unsupported file",
                             message="The file you uploaded wasn't a Java or JS file.\nPlease try uploading again!")
        return

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

    upload_button = Button(
        text="Upload a file...",
        command=lambda: validate_file(save_choice),
        font=("Courier New", 15))
    upload_button.place(x=210, y=300)

    note = Label(window,
                 text="MethodStrip operations are reversible as long as this window is kept open.\nAlways be careful when overwriting files.",
                 font=("Courier New", 10),
                 bg= "white",
                 fg="black")
    note.place(x=210, y= 340)


    window.mainloop()

if __name__ == "__main__":
    main()
