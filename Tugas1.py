import tkinter as tk
from tkinter import ttk

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Enkripsi & Dekripsi - Caesar Cipher")
        self.root.geometry("600x400")
        self.root.configure(bg="#ffe6f2")  # Light pink background

        # Apply a ttk theme and style configurations
        style = ttk.Style()
        style.theme_use("clam")  # Use "clam" or "alt" for a modern look
        style.configure("TFrame", background="#ffe6f2")
        style.configure("TLabel", background="#ffe6f2", font=("Arial", 10))
        style.configure("TButton", background="#ff66b2", foreground="white", font=("Arial", 10, "bold"))
        style.map("TButton", background=[("active", "#ff3385")])
        style.configure("TNotebook", background="#ffccf2", tabposition="n")
        style.configure("TNotebook.Tab", padding=[10, 5], font=("Arial", 10, "bold"), background="#ff99cc")
        style.map("TNotebook.Tab", background=[("selected", "#ff66b2")])
        style.configure("TText", wrap="word", font=("Arial", 10), padding=[5, 5])

        # Shift value
        self.shift_value = tk.IntVar(value=3)
        
        # Create tabs
        self.tab_control = ttk.Notebook(root)
        
        self.tab1 = ttk.Frame(self.tab_control, padding=(10, 10))
        self.tab2 = ttk.Frame(self.tab_control, padding=(10, 10))
        
        self.tab_control.add(self.tab1, text='Enkripsi')
        self.tab_control.add(self.tab2, text='Dekripsi')
        self.tab_control.pack(expand=1, fill="both", padx=10, pady=10)
        
        # Enkripsi tab
        self.setup_enkripsi_tab()
        
        # Dekripsi tab
        self.setup_dekripsi_tab()
    
    def setup_enkripsi_tab(self):
        shift_frame = ttk.Frame(self.tab1)
        shift_frame.pack(pady=10)
        
        ttk.Label(shift_frame, text="Jumlah Pergeseran:").pack(side=tk.LEFT)
        shift_spinbox = ttk.Spinbox(
            shift_frame, 
            from_=1, 
            to=25, 
            width=5,
            textvariable=self.shift_value,
            font=("Arial", 10)
        )
        shift_spinbox.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(self.tab1, text="Masukkan Plainteks:").pack(pady=5)
        self.plaintext_input = tk.Text(self.tab1, height=5, width=50, wrap="word", font=("Arial", 10), bg="#ffccf2", fg="#660033")
        self.plaintext_input.pack(pady=5)
        
        encrypt_button = ttk.Button(self.tab1, text="Enkripsi", command=self.encrypt)
        encrypt_button.pack(pady=10)
        
        ttk.Label(self.tab1, text="Hasil Enkripsi (Cipherteks):").pack(pady=5)
        self.cipher_output = tk.Text(self.tab1, height=5, width=50, wrap="word", font=("Arial", 10), bg="#ffccf2", fg="#660033")
        self.cipher_output.pack(pady=5)
    
    def setup_dekripsi_tab(self):
        shift_frame = ttk.Frame(self.tab2)
        shift_frame.pack(pady=10)
        
        ttk.Label(shift_frame, text="Jumlah Pergeseran:").pack(side=tk.LEFT)
        shift_spinbox = ttk.Spinbox(
            shift_frame, 
            from_=1, 
            to=25, 
            width=5,
            textvariable=self.shift_value,
            font=("Arial", 10)
        )
        shift_spinbox.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(self.tab2, text="Masukkan Cipherteks:").pack(pady=2)
        self.cipher_input = tk.Text(self.tab2, height=5, width=50, wrap="word", font=("Arial", 10), bg="#ffccf2", fg="#660033")
        self.cipher_input.pack(pady=5)
        
        decrypt_button = ttk.Button(self.tab2, text="Dekripsi", command=self.decrypt)
        decrypt_button.pack(pady=10)
        
        ttk.Label(self.tab2, text="Hasil Dekripsi (Plainteks):").pack(pady=2)
        self.plain_output = tk.Text(self.tab2, height=5, width=50, wrap="word", font=("Arial", 10), bg="#ffccf2", fg="#660033")
        self.plain_output.pack(pady=5)
    
    def shift_character(self, char, shift, encrypt=True):
        if not char.isalpha():
            return char
        ascii_base = 97 if char.islower() else 65
        if not encrypt:
            shift = -shift
        shifted = (ord(char) - ascii_base + shift) % 26
        return chr(shifted + ascii_base)
    
    def process_text(self, text, encrypt=True):
        shift = self.shift_value.get()
        result = ''.join(self.shift_character(char, shift, encrypt) for char in text)
        return result
    
    def encrypt(self):
        plaintext = self.plaintext_input.get("1.0", tk.END).strip()
        ciphertext = self.process_text(plaintext, encrypt=True)
        self.cipher_output.delete("1.0", tk.END)
        self.cipher_output.insert("1.0", ciphertext)
    
    def decrypt(self):
        ciphertext = self.cipher_input.get("1.0", tk.END).strip()
        plaintext = self.process_text(ciphertext, encrypt=False)
        self.plain_output.delete("1.0", tk.END)
        self.plain_output.insert("1.0", plaintext)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
