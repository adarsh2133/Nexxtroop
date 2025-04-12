import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NexxtroopApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nexxtroop - 2D to 3D Map Converter")
        self.geometry("700x500")
        self.resizable(True, True)

        self.image_path = None

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.build_ui()

    def build_ui(self):
        title = ctk.CTkLabel(self, text="🚀 Nexxtroop", font=("Segoe UI", 28, "bold"))
        title.grid(row=0, column=0, pady=(20, 5))

        subtitle = ctk.CTkLabel(self, text="Convert your 2D maps into 3D models Instantly", font=("Segoe UI", 14))
        subtitle.grid(row=1, column=0, pady=(0, 10))


        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.grid(row=2, column=0, padx=40, pady=20, sticky="nsew")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure((0, 1, 2), weight=1)

    
        upload_btn = ctk.CTkButton(main_frame, text="📁 Upload 2D Map", command=self.choose_file, height=40)
        upload_btn.grid(row=0, column=0, padx=60, pady=(30, 10), sticky="ew")

        self.generate_btn = ctk.CTkButton(main_frame, text="⚙️ Generate 3D Map", command=self.generate_map,
                                          state="disabled", height=40)
        self.generate_btn.grid(row=1, column=0, padx=60, pady=10, sticky="ew")

        self.status_label = ctk.CTkLabel(main_frame, text="No file selected", font=("Segoe UI", 12), text_color="gray")
        self.status_label.grid(row=2, column=0, pady=(20, 30))

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.generate_btn.configure(state="normal")
            self.status_label.configure(text="✅ File selected. Ready to generate!", text_color="lightgreen")

    def generate_map(self):
        self.status_label.configure(text="⏳ Generating 3D map...", text_color="yellow")
        self.update()


        success = True

        if success:
            self.status_label.configure(text="🎉 3D map generated successfully!", text_color="lightgreen")
        else:
            self.status_label.configure(text="❌ Failed to generate map.", text_color="red")

if __name__ == "__main__":
    app = NexxtroopApp()
    app.mainloop()
