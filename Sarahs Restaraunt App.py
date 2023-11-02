import tkinter as tk
import tkinter.messagebox as messagebox

class RestaurantManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Sarah's Restaurant")
        self.orders = []

        # Define an extended menu with separate categories for drinks, food, and dessert
        self.menu = {
            "Food": [
                {"name": "Burger", "price": 5.99},
                {"name": "Pizza", "price": 7.99},
                {"name": "Pasta", "price": 9.99},
                {"name": "Salad", "price": 3.99},
                {"name": "Steak", "price": 14.99},
                {"name": "Chicken Alfredo", "price": 11.99},
                {"name": "Fish and Chips", "price": 8.99},
                {"name": "Lasagna", "price": 10.99},
                {"name": "Sushi Roll", "price": 12.99},
                {"name": "Pho", "price": 9.99},
                {"name": "Sushi Nigiri", "price": 14.99},
                {"name": "BBQ Ribs", "price": 13.99},
            ],
            "Drinks": [
                {"name": "Soda", "price": 1.99},
                {"name": "Tiramisu", "price": 4.99},
                {"name": "Margarita", "price": 6.49},
                {"name": "Lemonade", "price": 2.49},
                {"name": "Smoothie", "price": 3.99},
                {"name": "Cappuccino", "price": 2.99},
            ],
            "Dessert": [
                {"name": "Chocolate Cake", "price": 5.99},
                {"name": "Cheesecake", "price": 4.99},
                {"name": "Apple Pie", "price": 4.49},
                {"name": "Fruit Parfait", "price": 3.99},
                {"name": "Brownie Sundae", "price": 6.49},
                {"name": "Tart", "price": 5.49},
                {"name": "Creme Brulee", "price": 6.99},
                {"name": "Panna Cotta", "price": 5.99},
                {"name": "Molten Lava Cake", "price": 6.49},
                {"name": "Key Lime Pie", "price": 4.99},
            ]
        }

        self.show_welcome_message()
        self.create_menu()
        self.create_order()
        self.create_feedback_button()
        self.create_total_button()
        self.create_call_server_button()
        self.create_exit_button()

    def show_welcome_message(self):
        messagebox.showinfo("Welcome", "Welcome to Sarah's Restaurant")

    def create_menu(self):
        menu_frame = tk.LabelFrame(self.root, text="Menu", bg="red", fg="white")
        menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

        for category, items in self.menu.items():
            category_label = tk.Label(menu_frame, text=category, bg="red", fg="white")
            category_label.pack()
            for item in items:
                item_button = tk.Button(menu_frame, text=f"{item['name']} - ${item['price']:.2f}", command=lambda i=item: self.add_to_order(i),
                                        bg="black", fg="white")
                item_button.pack(fill=tk.X)

    def create_order(self):
        order_frame = tk.LabelFrame(self.root, text="Order", bg="red", fg="white")
        order_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.order_listbox = tk.Listbox(order_frame, selectmode=tk.SINGLE)
        self.order_listbox.pack(fill=tk.BOTH)

        delete_button = tk.Button(order_frame, text="Delete", command=self.delete_item, bg="black", fg="white")
        delete_button.pack(pady=10)

    def delete_item(self):
        selected_index = self.order_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.order_listbox.delete(index)
            del self.orders[index]

    def create_feedback_button(self):
        feedback_button = tk.Button(self.root, text="Give Feedback", command=self.take_feedback, bg="black", fg="white")
        feedback_button.pack(pady=10)

    def create_total_button(self):
        total_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total, bg="red", fg="white")
        total_button.pack(pady=10)

    def create_call_server_button(self):
        call_server_button = tk.Button(self.root, text="Call Server", command=self.call_server, bg="black", fg="white")
        call_server_button.pack(pady=10)

    def create_exit_button(self):
        exit_button = tk.Button(self.root, text="Exit Application", command=self.exit_app, bg="red", fg="white")
        exit_button.pack(pady=10)

    def add_to_order(self, item):
        self.orders.append(item)
        self.order_listbox.insert(tk.END, f"{item['name']} - ${item['price']:.2f}")

    def calculate_total(self):
        subtotal = sum(item['price'] for item in self.orders)
        tax = 2.0
        total = subtotal + tax
        total_message = f"Subtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}"
        messagebox.showinfo("Order Total", total_message)

    def take_feedback(self):
        feedback_window = tk.Toplevel(self.root)
        feedback_window.title("Feedback")
        feedback_label = tk.Label(feedback_window, text="Please provide your feedback (optional):")
        feedback_label.pack()
        feedback_text = tk.Text(feedback_window, height=5, width=30)
        feedback_text.pack()
        feedback_button = tk.Button(feedback_window, text="Submit Feedback", command=feedback_window.destroy, bg="black", fg="white")
        feedback_button.pack()

    def call_server(self):
        messagebox.showinfo("Call Server", "A server will be with you shortly.")

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManager(root)
    root.mainloop()
