import customtkinter as ctk
from fpdf import FPDF
import openai

# Set up OpenAI API key
openai.api_key = "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"  # Replace with your OpenAI API key


class CheatSheetGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Integrated Cheat Sheet Generator")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        # Title
        self.title_label = ctk.CTkLabel(root, text="AI Cheat Sheet Generator", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Topic Input
        self.topic_label = ctk.CTkLabel(root, text="Enter Topic for Cheat Sheet:")
        self.topic_label.pack(pady=10)
        self.topic_entry = ctk.CTkEntry(root, width=400)
        self.topic_entry.pack(pady=10)

        # Generate Button
        self.generate_button = ctk.CTkButton(root, text="Generate Cheat Sheet", command=self.generate_cheat_sheet)
        self.generate_button.pack(pady=20)

        # Status Display
        self.status_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        # Output Display (Scrollable Textbox)
        self.output_box = ctk.CTkTextbox(root, height=300, width=600)
        self.output_box.pack(pady=10)

        # Save Button
        self.save_button = ctk.CTkButton(root, text="Save as PDF", command=self.save_to_pdf, state="disabled")
        self.save_button.pack(pady=10)

        # Cheat Sheet Content
        self.cheat_sheet_content = ""

    def generate_cheat_sheet(self):
        topic = self.topic_entry.get().strip()
        if not topic:
            self.status_label.configure(text="Please enter a topic!", text_color="red")
            return

        self.status_label.configure(text="Generating cheat sheet... Please wait.", text_color="blue")
        self.root.update_idletasks()

        try:
            # Call OpenAI API to generate content
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert educator creating cheat sheets."},
                    {"role": "user", "content": f"Create a detailed cheat sheet on the topic: {topic}"}
                ]
            )
            self.cheat_sheet_content = response['choices'][0]['message']['content']
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", self.cheat_sheet_content)
            self.status_label.configure(text="Cheat sheet generated successfully!", text_color="green")
            self.save_button.configure(state="normal")
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}", text_color="red")

    def save_to_pdf(self):
        if not self.cheat_sheet_content:
            self.status_label.configure(text="No content to save!", text_color="red")
            return

        topic = self.topic_entry.get().strip()
        filename = f"{topic.replace(' ', '_')}_CheatSheet.pdf"

        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, self.cheat_sheet_content)
            pdf.output(filename)
            self.status_label.configure(text=f"Cheat sheet saved as {filename}!", text_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Error saving PDF: {e}", text_color="red")


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = CheatSheetGeneratorApp(root)
    root.mainloop()
