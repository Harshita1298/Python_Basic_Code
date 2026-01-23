import tkinter as tk

# Window
root = tk.Tk()
root.title("Typing Effect")
root.geometry("700x400")
root.configure(bg="pink")

# Label (perfect center)
label = tk.Label(
    root,
    text="",
    font=("Arial", 22, "bold"),
    bg="pink",
    fg="blue"
)
label.place(relx=0.5, rely=0.5, anchor="center")  # center both sides

# Text to show (dummy lyrics)
text ="""Tum mile, toh mil gaya yeh jahaan
Tum mile, toh har pal hai naya
Tum mile, toh sabse hai, faasla
Tum mile, toh jaadu chaa gaya
Tum mile, toh jeena aa gaya
Tum mile, toh maine paaya, hai khuda…

Come around, it’s time to baby, come around
Come on now come around
It’s time to baby, come around
Come around, come around…

Palken moondein, chaahat meri so rahi thi
Khushboo hawaaon mein thi maine nahin mehsoos ki
Umm mm, jaane kahaan, bahaaren meri khil rahi thi
Khushboo hawaaon mein thi maine nahin mehsoos ki…

Tum mile, toh mehki baarishen
Tum mile, toh jaagi khwaahishen
Tum mile, toh rangon ka hai, silsila
Tum mile, toh jaadu chaa gaya
Tum mile, toh jeena aa gaya
Tum mile, toh maine paaya, hai khuda…

Ta ra ra, ta ra ra, ta ra ra…

Tune duaaein suni, dil ki sadaaye suni
Tujh se main maangu aur kya
Tujh bin adhura hu main, tere sang poora hu main
Karta hun tera shukriya…

(Kaise kahoon) * 4
Kaise kahoon, lamhe mujhe chu rahe hain
Aisa laga hain in mein tera hi toh ehsaas hain
Oh ho, kaise kahoon, dil mein nayi aahatein hain
Aisa laga hain in mein tera hi toh ehsaas hain…

Tum mile, toh mera dil gaya
Tum mile, toh sab kuch mil gaya
Tum mile, toh logon se kya, vaasta ho oh
Tum mile, toh jaadu chaa gaya
Tum mile, toh jeena aa gaya
Tum mile, toh maine paaya, hai khuda…"""
index = 0
deleting = True

def animate():
    global index, deleting

    if not deleting:
        # Typing
        if index <= len(text):
            label.config(text=text[:index])
            index += 1
            root.after(120, animate)
        else:
            deleting = True
            root.after(800, animate)  # pause before deleting
    else:
        # Deleting
        if index >= 0:
            label.config(text=text[:index])
            index -= 1
            root.after(80, animate)
        else:
            deleting = False
            root.after(500, animate)

animate()
root.mainloop()
