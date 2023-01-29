import tkinter as tk


class AgendaTelefonica:
    def __init__(self, master):
        self.master = master
        self.master.title("Agenda Telefónica")

        self.contacts = {}

        # Create Entry widgets for name, phone and address
        self.name_entry = tk.Entry(self.master)
        self.phone_entry = tk.Entry(self.master)
        self.address_entry = tk.Entry(self.master)

        # Create buttons for adding and searching contacts
        self.add_button = tk.Button(self.master, text="Añadir", command=self.add_contact)
        self.search_button = tk.Button(self.master, text="Buscar", command=self.search_contact)

        # Create a text widget to display the results
        self.results_text = tk.Text(self.master, height=10, width=30)

        # Place the widgets on the window
        self.name_entry.grid(row=0, column=0)
        self.phone_entry.grid(row=1, column=0)
        self.address_entry.grid(row=2, column=0)
        self.add_button.grid(row=3, column=0)
        self.search_button.grid(row=3, column=1)
        self.results_text.grid(row=4, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        self.contacts[name] = (phone, address)

        self.results_text.insert(tk.END, f"Contacto añadido: {name}\n")

    def search_contact(self):
        name = self.name_entry.get()

        if name in self.contacts:
            phone, address = self.contacts[name]
            self.results_text.insert(tk.END,
                                     f"Contacto encontrado: {name}\n Teléfono: {phone}\n Dirección: {address}\n")
        else:
            self.results_text.insert(tk.END, f"Contacto no encontrado: {name}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaTelefonica(root)
    root.mainloop()
