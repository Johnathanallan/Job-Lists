import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from fpdf import FPDF
import re
from datetime import datetime
from tkinter import filedialog

def validate_inputs():
    if not contract_signed_date_entry.get().strip():
        messagebox.showerror("Input Error", "Contract Signed Date cannot be empty!")
        return False

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", contract_signed_date_entry.get()):
        messagebox.showerror("Input Error", "Invalid date format! Use YYYY-MM-DD.")
        return False

    try:
        # Remove commas and ensure it is a valid number
        float(contract_total_entry.get().replace(',', ''))
    except ValueError:
        messagebox.showerror("Input Error", "Contract Total must be a valid number!")
        return False
    
    return True

def save_invoice():
    if not validate_inputs():
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Job_Profile_Lists_{timestamp}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    job_lists_text = f"""
    --- Landscape Project Manager Lists ---
    Contract Signed Date: {contract_signed_date_entry.get()}
    Salesperson: {salesperson_entry.get()}
    Contract Total: {contract_total_entry.get()}
    Project Name: {project_name_entry.get()}
    Project Type: {project_type_var.get()}
    Project Progress: {project_progress_var.get()}
    HOA Approval: {hoa_approval_var.get()}
    Permitting: {permitting_var.get()}
    Contract total with Admin Fee: {admin_fee()}
    Image Path: {image_path}
    ----------------------------
    """
    
    pdf.multi_cell(0, 10, job_lists_text)
    
    if image_path:
        pdf.image(image_path, x=12, y=pdf.get_y() + 10, w=100)

    
    pdf.output(filename)
    messagebox.showinfo("Job Lists Saved", f"Invoice has been saved as '{filename}'")

def admin_fee():
    total = float(contract_total_entry.get().replace(',', ''))
    admin_fee = 299
    new_Total = total + admin_fee
   
    return new_Total

def clear_fields():
    contract_signed_date_entry.set_date(datetime.today())
    contract_total_entry.delete(0, tk.END)
    project_name_entry.delete(0, tk.END)
    project_type_var.set("Landscape")
    project_progress_var.set("Not Started")
    hoa_approval_var.set("No")
    permitting_var.set("No")

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        global image_path
        image_path = file_path
        messagebox.showinfo("Image Selected", f"Image has been selected: {file_path}")


project_type = ["Landscape", "Concrete", "Fencing", "Decking", "Paving", "Gardening", "Driveway", "Patio", "Turfing", "Brickwork", "Walling", "Drainage", "Water Features", "Lighting", "Irrigation", "Planting", "Maintenance", "Design", "Consultation", "Other"]
project_progress = ["Not Started", "In Progress", "Completed", "On Hold", "Cancelled", "HOA Approval", "Permitting", "Design", "Consultation", "Other"]
have_hoa = ["Yes", "No"]
have_permit = ["Yes", "No"]

root = tk.Tk()
root.title("Project Management")
root.geometry("500x500")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Contract Signed Date: ").grid(row=0, column=0, padx=5, pady=5)
contract_signed_date_entry = DateEntry(frame, width=27, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
contract_signed_date_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Salesperson: ").grid(row=1, column=0, padx=5, pady=5)
salesperson_entry = ttk.Entry(frame, width=30)
salesperson_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Contract Total: ").grid(row=2, column=0, padx=5, pady=5)
contract_total_entry = ttk.Entry(frame, width=30)
contract_total_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame, text="Project Name: ").grid(row=3, column=0, padx=5, pady=5)
project_name_entry = ttk.Entry(frame, width=30)
project_name_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame, text="Project Type: ").grid(row=4, column=0, padx=5, pady=5)
project_type_var = tk.StringVar(value="Landscape")
project_type_menu = ttk.OptionMenu(frame, project_type_var, "Landscape", *project_type)
project_type_menu.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame, text="Project Progress: ").grid(row=5, column=0, padx=5, pady=5)
project_progress_var = tk.StringVar(value="Not Started")
project_progress_menu = ttk.OptionMenu(frame, project_progress_var, "Not Started", *project_progress)
project_progress_menu.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(frame, text="HOA Approval: ").grid(row=6, column=0, padx=5, pady=5)
hoa_approval_var = tk.StringVar(value="No")
hoa_approval_menu = ttk.OptionMenu(frame, hoa_approval_var, "No", *have_hoa)
hoa_approval_menu.grid(row=6, column=1, padx=5, pady=5)

ttk.Label(frame, text="Permitting: ").grid(row=7, column=0, padx=5, pady=5)
permitting_var = tk.StringVar(value="No")
permitting_menu = ttk.OptionMenu(frame, permitting_var, "No", *have_permit)
permitting_menu.grid(row=7, column=1, padx=5, pady=5)

#i want to add a button to add an image to the pdf

upload_image = ttk.Button(frame, text="Upload Image", command=upload_image)
upload_image.grid(row=8, column=0, columnspan=2, pady=10)


save_button = ttk.Button(frame, text="Save Job Lists", command=save_invoice)
save_button.grid(row=9, column=0, columnspan=2, pady=10)

clear_button = ttk.Button(frame, text="Clear Fields", command=clear_fields)
clear_button.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
