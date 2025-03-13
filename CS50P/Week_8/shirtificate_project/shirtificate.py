from fpdf import FPDF

class Shirtificate:
    def __init__(self, name: str):
        """
        Initializes the Shirtificate with a user's name.

        :param name: The name of the user to be displayed on the shirt.
        """
        self.name = name
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")

    def create_pdf(self):
        # Creates a new PDF with the CS50 Shirtificate design.
        self.pdf.add_page()
        self._add_title()
        self._add_shirt_image()
        self._add_name()
        self._save_pdf()

    def _add_title(self):
        # Adds the title 'CS50 Shirtificate' at the top of the PDF.
        self.pdf.set_font("Arial", style="B", size=24)
        self.pdf.cell(0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    def _add_shirt_image(self):
        # Adds the CS50 shirt image and centers it in the PDF.
        self.pdf.image("shirtificate.png", x=15, y=50, w=180)

    def _add_name(self):
        # Overlays the user's name on the shirt with white text.
        self.pdf.set_font("Arial", style="B", size=18)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.text(x=65, y=120, txt=f"{self.name} took CS50P")

    def _save_pdf(self):
        # Saves the generated PDF as 'shirtificate.pdf'.
        self.pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    name = input("Enter your name: ")
    shirtificate = Shirtificate(name)
    shirtificate.create_pdf()
    print("Shirtificate generated as 'shirtificate.pdf'")
