import tkinter as tk

# Window
root = tk.Tk()
root.title("Love Lyrics Effect")
root.geometry("800x400")
root.configure(bg="pink")

# Top LOVE text
love_label = tk.Label(
    root,
    text="LOVE ❤️",
    font=("Comic Sans MS", 28, "bold"),
    bg="pink",
    fg="red"
)
love_label.pack(pady=10)

# Center lyric label
label = tk.Label(
    root,
    text="",
    font=("Comic Sans MS", 22, "bold"),
    bg="pink",
    fg="blue",
    wraplength=700,
    justify="center"
)
label.place(relx=0.5, rely=0.55, anchor="center")

# Lyrics (example – short rakho demo ke liye)
lyrics = """Tum mile, toh mil gaya yeh jahaan
Tum mile, toh har pal hai naya
Tum mile, toh jaadu chaa gaya
Tum mile, toh jeena aa gaya"""

lines = lyrics.split("\n")

line_index = 0
char_index = 0

def animate():
    global line_index, char_index

    current_line = lines[line_index]

    # Typing effect (no deleting)
    if char_index <= len(current_line):
        label.config(text=current_line[:char_index])
        char_index += 1
        root.after(120, animate)
    else:
        # Line complete → pause → next line
        root.after(1100, next_line)

def next_line():
    global line_index, char_index

    char_index = 0
    line_index = (line_index + 1) % len(lines)
    label.config(text="")   # old line instantly clear
    animate()

animate()
root.mainloop()
