import tkinter as tk
import threading
from PIL import Image, ImageTk

NUM_TICKETS = 100

tickets_available1 = NUM_TICKETS
tickets_available2 = NUM_TICKETS
tickets_available3 = NUM_TICKETS
ticket_mutex = threading.Lock()

def customer_thread(movie_name, tickets_to_purchase, text_widget):
    global tickets_available1, tickets_available2, tickets_available3
    with ticket_mutex:
        if movie_name == "Leo":
            if tickets_available1 >= tickets_to_purchase:
                tickets_available1 -= tickets_to_purchase
                text_widget.insert('end', f'Customer successfully purchased {tickets_to_purchase} tickets for Leo. {tickets_available1} tickets remaining.\n')
            else:
                text_widget.insert('end', f'Customer couldn\'t purchase {tickets_to_purchase} tickets for Leo. Only {tickets_available1} tickets remaining.\n')
        elif movie_name == "Vikram":
            if tickets_available2 >= tickets_to_purchase:
                tickets_available2 -= tickets_to_purchase
                text_widget.insert('end', f'Customer successfully purchased {tickets_to_purchase} tickets for Vikram. {tickets_available2} tickets remaining.\n')
            else:
                text_widget.insert('end', f'Customer couldn\'t purchase {tickets_to_purchase} tickets for Vikram. Only {tickets_available2} tickets remaining.\n')
        elif movie_name == "Jailer":
            if tickets_available3 >= tickets_to_purchase:
                tickets_available3 -= tickets_to_purchase
                text_widget.insert('end', f'Customer successfully purchased {tickets_to_purchase} tickets for Jailer. {tickets_available3} tickets remaining.\n')
            else:
                text_widget.insert('end', f'Customer couldn\'t purchase {tickets_to_purchase} tickets for Jailer. Only {tickets_available3} tickets remaining.\n')

def book_tickets(movie_name, tickets_to_purchase, text_widget):
    if tickets_to_purchase > 0:
        customer_thread(movie_name, tickets_to_purchase, text_widget)

def change_movie(movie_var, selected_movie):
    selected_movie.set(movie_var.get())

def main():
    root = tk.Tk()
    root.title("Movie Ticket Booking Counter")
    root.geometry("600x500")
    root.configure(bg="black")

    movie_var = tk.StringVar()
    movie_var.set("Leo")

    selected_movie = tk.StringVar()
    selected_movie.set("Leo")

    movie_label = tk.Label(root, text="Select Movie:", font=("Arial", 14), bg="black", fg="white")
    movie_label.pack(pady=10)

    movie_frame = tk.Frame(root, bg="black")
    movie_frame.pack()

    def create_movie_radio_button(movie_name, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 250))
        img = ImageTk.PhotoImage(img)
        label = tk.Label(movie_frame, image=img, compound="top", font=("Arial", 12), bg="black", fg="white")
        label.image = img
        label.pack(side="left")
        radio_button = tk.Radiobutton(root, text=movie_name, variable=movie_var, value=movie_name, command=lambda: change_movie(movie_var, selected_movie))
        radio_button.pack(side="left")

    create_movie_radio_button("Leo", r"D:\PRJ\c0d347f7961c17b66294ab0ee8e0d668 (1).jpg")
    create_movie_radio_button("Vikram", r"D:\PRJ\download (1).jpeg")
    create_movie_radio_button("Jailer", r"D:\PRJ\download.jpeg")

    tickets_label = tk.Label(root, text="Tickets to Purchase:", font=("Arial", 14), bg="black", fg="white")
    tickets_label.pack(pady=10)

    tickets_entry = tk.Entry(root)
    tickets_entry.pack()

    book_button = tk.Button(root, text="Book Tickets", command=lambda: book_tickets(selected_movie.get(), int(tickets_entry.get()), text_widget), font=("Arial", 12), bg="orange")
    book_button.pack(pady=10)

    text_widget = tk.Text(root, height=20, width=40, bg="black", fg="white")
    text_widget.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

