from tkinter import *
import tkinter.messagebox as messagebox

# Initialize main window
window = Tk()
window.geometry("800x700")
window.configure(bg="#ADD8E6")

# Define languages
languages = {
    "English": {
        "samosa": "Samosa",
        "vada_pav": "Vada Pav",
        "fried_rice": "Fried Rice",
        "chole_bhature": "Chole Bhature",
        "pav_bhaji": "Pav Bhaji",
        "biryani": "Biryani",
        "idli": "Idli",
        "medu_vada": "Medu Vada",
        "frankie": "Frankie",
        "pay": "Total Amount:",
        "payment": "Payment Method:",
        "discount": "Discount Code:",
        "bill": "Generate Bill",
        "clear": "Clear",
        "exit": "Exit",
        "language": "Select Language:",
        "success": "Bill Generated Successfully!",
        "invalid_code": "Invalid discount code!",
        "invalid_quantity": "Please enter valid quantities for all items.",
    },
    "Hindi": {
        "samosa": "समोसा",
        "vada_pav": "वड़ा पाव",
        "fried_rice": "फ्राइड राइस",
        "chole_bhature": "चोले भटूरा",
        "pav_bhaji": "पाव भाजी",
        "biryani": "बिरयानी",
        "idli": "इडली",
        "medu_vada": "मेदु वड़ा",
        "frankie": "फ्रैंकी",
        "pay": "कुल राशि:",
        "payment": "भुगतान विधि:",
        "discount": "छूट कोड:",
        "bill": "बिल उत्पन्न करें",
        "clear": "साफ करें",
        "exit": "बाहर निकलें",
        "language": "भाषा चुनें:",
        "success": "बिल सफलतापूर्वक उत्पन्न हुआ!",
        "invalid_code": "अमान्य छूट कोड!",
        "invalid_quantity": "कृपया सभी आइटम के लिए मान्य मात्राएँ दर्ज करें।",
    }
}

current_language = "English"

# Function to update labels based on the current language
def update_labels():
    for i, (item, price) in enumerate(menu_items):
        label = Label(window, text=f"{languages[current_language][item]}        Rs {price}", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
        label.place(x=450, y=120 + i * 30)

    label7.config(text=languages[current_language]["payment"])
    label_discount_code.config(text=languages[current_language]["discount"])
    b2.config(text=languages[current_language]["bill"])
    b3.config(text=languages[current_language]["clear"])
    exit_button.config(text=languages[current_language]["exit"])
    language_label.config(text=languages[current_language]["language"])

# Function to switch language
def switch_language(language):
    global current_language
    current_language = language
    update_labels()

# Function to validate quantity entries
def validate_entries():
    quantities = []
    for entry in [e1, e2, e3, e4, e5, e6, e7, e8, e9]:
        value = entry.get().strip()
        if value:  # Check if value is not empty
            if not value.isdigit():  # Check if value is a valid digit
                messagebox.showerror("Error", languages[current_language]["invalid_quantity"])
                return None
            quantities.append(int(value))
        else:
            quantities.append(0)  # If field is empty, assume quantity is 0
    return quantities

# Function to calculate the total and generate the bill
def calculate():
    quantities = validate_entries()
    if quantities is None:
        messagebox.showerror("Error", languages[current_language]["invalid_quantity"])
        return

    total = sum([
        quantities[0] * 15,
        quantities[1] * 18,
        quantities[2] * 50,
        quantities[3] * 60,
        quantities[4] * 70,
        quantities[5] * 120,
        quantities[6] * 30,
        quantities[7] * 35,
        quantities[8] * 80,
    ])
    
    # Apply discount if code is valid
    discount_code = discount_code_entry.get().strip()
    if discount_code == "VES1234":
        discount = total * 0.10  # 10% discount
        total -= discount
        messagebox.showinfo("Discount Applied", f"10% discount applied! You saved Rs {discount:.2f}.")
    elif discount_code != "":
        messagebox.showwarning("Warning", languages[current_language]["invalid_code"])

    # Display total amount
    label12.config(text=f"{languages[current_language]['pay']} Rs {total:.2f}")

    # Payment details
    payment_method = payment_method_var.get()
    payment_details_label.config(text=f"{languages[current_language]['payment']} {payment_method}")

    # Show success message
    messagebox.showinfo("Success", languages[current_language]["success"])

# Function to clear entries
def clear_entries():
    for entry in [e1, e2, e3, e4, e5, e6, e7, e8, e9, discount_code_entry]:
        entry.delete(0, END)
    label12.config(text="")
    payment_details_label.config(text="")

# Exit function
def exit_program():
    window.quit()

# Header
label6 = Label(window, text="VES CANTEEN", font=("Comic Sans MS", 30, "bold"), bg="#ADD8E6", fg="#00698F")
label6.place(x=400, y=20, anchor="center")

# Menu items
menu_items = [
    ("samosa", 15),
    ("vada_pav", 18),
    ("fried_rice", 50),
    ("chole_bhature", 60),
    ("pav_bhaji", 70),
    ("biryani", 120),
    ("idli", 30),
    ("medu_vada", 35),
    ("frankie", 80),
]

# Create label for each menu item
for i, (item, price) in enumerate(menu_items):
    label = Label(window, text=f"{languages[current_language][item]}        Rs {price}", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
    label.place(x=450, y=120 + i * 30)

# Order section
label7 = Label(window, text="", font=("Comic Sans MS", 20, "bold"), bg="#ADD8E6", fg="#00698F")
label7.place(x=70, y=70)

# Create entry fields for each menu item
e1 = Entry(window, font=("Comic Sans MS", 18), width=5)
e1.place(x=20, y=150)

e2 = Entry(window, font=("Comic Sans MS", 18), width=5)
e2.place(x=20, y=180)

e3 = Entry(window, font=("Comic Sans MS", 18), width=5)
e3.place(x=20, y=210)

e4 = Entry(window, font=("Comic Sans MS", 18), width=5)
e4.place(x=20, y=240)

e5 = Entry(window, font=("Comic Sans MS", 18), width=5)
e5.place(x=20, y=270)

e6 = Entry(window, font=("Comic Sans MS", 18), width=5)
e6.place(x=20, y=300)

e7 = Entry(window, font=("Comic Sans MS", 18), width=5)
e7.place(x=20, y=330)

e8 = Entry(window, font=("Comic Sans MS", 18), width=5)
e8.place(x=20, y=360)

e9 = Entry(window, font=("Comic Sans MS", 18), width=5)
e9.place(x=20, y=390)

# Discount code entry
label_discount_code = Label(window, text="", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
label_discount_code.place(x=20, y=420)

discount_code_entry = Entry(window, font=("Comic Sans MS", 18), width=15)
discount_code_entry.place(x=20, y=450)

# Payment method
label_payment = Label(window, text="", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
label_payment.place(x=20, y=490)

payment_method_var = StringVar(value="Cash")
payment_options = [
    ("Cash", "Cash"),
    ("Card", "Card"),
    ("Digital", "Digital Payment"),
]

for i, (text, value) in enumerate(payment_options):
    rb = Radiobutton(window, text=text, variable=payment_method_var, value=value, font=("Comic Sans MS", 16), bg="#ADD8E6", fg="#00698F")
    rb.place(x=20 + (i * 100), y=520)

# Bill button
b2 = Button(window, text="", width=15, command=calculate, font=("Comic Sans MS", 18), bg="#00698F", fg="#FFFFFF")
b2.place(x=100, y=580)

# Clear button
b3 = Button(window, text="", width=15, command=clear_entries, font=("Comic Sans MS", 18), bg="#00698F", fg="#FFFFFF")
b3.place(x=300, y=580)

# Exit button
exit_button = Button(window, text="", width=15, command=exit_program, font=("Comic Sans MS", 18), bg="#00698F", fg="#FFFFFF")
exit_button.place(x=500, y=580)

# Total label
label12 = Label(window, text="", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
label12.place(x=100, y=640)

# Payment details label
payment_details_label = Label(window, text="", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
payment_details_label.place(x=450, y=640)

# Language selection dropdown
language_label = Label(window, text="", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00698F")
language_label.place(x=20, y=20)

language_var = StringVar(value="English")
language_menu = OptionMenu(window, language_var, "English", "Hindi", command=switch_language)
language_menu.place(x=20, y=50)

# Initial label updates
update_labels()

# Run the main loop
window.mainloop()
