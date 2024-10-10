from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Samuel\Desktop\GOLDEN_FISH\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("912x1040")
window.configure(bg = "#2A2433")
window.title("Goldfish")


canvas = Canvas(
    window,
    bg = "#2A2433",
    height = 1040,
    width = 912,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

meowth_image = PhotoImage(file=relative_to_assets("meowth.png"))  
heart_scale_image = PhotoImage(file=relative_to_assets("heartscale.png"))
gold_image = PhotoImage(file=relative_to_assets("gold.png"))
github_image = PhotoImage(file=relative_to_assets("github.png"))



canvas.create_rectangle(
    0.0,
    1.0,
    912.0,
    1009.0,
    fill="#8165AA",
    outline="")

canvas.create_image(658, 314, image=meowth_image, anchor="center")


canvas.create_rectangle(
    0.0,
    658.0,
    912.0,
    1009.0,
    fill="#2A2433",
    outline="")

canvas.create_text(
    26.0,
    10.0,
    anchor="nw",
    text="Goldfish",
    fill="#F9D662",
    font=("Jaro Regular", 96 * -1)
)

canvas.create_text(
    26.0,
    679.0,
    anchor="nw",
    text="F i s h i n g . . .",
    fill="#FFFFFF",
    font=("Jaldi Regular", 96 * -1)
)

canvas.create_image(60.5, 244, image=heart_scale_image, anchor="center")


canvas.create_text(
    111.0,
    217.0,
    anchor="nw",
    text="x1",
    fill="#FFFFFF",
    font=("Jaldi Regular", 48 * -1)
)

canvas.create_text(
    111.0,
    416.0,
    anchor="nw",
    text="700.000",
    fill="#FFFFFF",
    font=("Jaldi Regular", 48 * -1)
)

canvas.create_text(
    111.0,
    551.0,
    anchor="nw",
    text="minerchan",
    fill="#FFFFFF",
    font=("Jaldi Regular", 48 * -1)
)

canvas.create_image(55.5, 444, image=gold_image, anchor="center")

canvas.create_text(
    26.0,
    164.0,
    anchor="nw",
    text="I T E M S",
    fill="#FFFEDF",
    font=("Jaldi Regular", 32 * -1)
)

canvas.create_text(
    26.0,
    355.0,
    anchor="nw",
    text="M O N E Y",
    fill="#FFFEDF",
    font=("Jaldi Regular", 32 * -1)
)

canvas.create_image(57.5, 579.5, image=github_image, anchor="center")

window.resizable(False, False)
window.mainloop()
