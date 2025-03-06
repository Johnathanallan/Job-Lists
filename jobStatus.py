import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from fpdf import FPDF
import re
from datetime import datetime

#function to give input error for the contract signed date, contract total,

def validate_inputs():
    if not contract_signed_date_entry.get().strip():
        messagebox.showerror("Input Error", "Contract Signed Date cannot be empty!")
        return False
    
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", contract_signed_date_entry.get()):
        messagebox.showerror("Input Error", "Invalid date format! Use YYYY-MM-DD.")
        return False
    
    try:
        float(contract_total_entry.get())  # Ensure it is a valid number
    except ValueError:
        messagebox.showerror("Input Error", "Contract Total must be a valid number!")
        return False


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
    Contract Total: {contract_total_entry.get()}
    Project Name: {project_name_entry.get()}
    Project Type: {project_type_var.get()}
    Project Progress: {project_progress_var.get()}
    HOA Approval: {hoa_approval_var.get()}
    Permitting: {permitting_var.get()}
    ----------------------------
    """

    for line in job_lists_text.strip().split("\n"):
        pdf.cell(200, 10, txt=line, ln=True, align="L")
    
    pdf.output(filename)
    messagebox.showinfo("Job Lists Saved", f"Invoice has been saved as '{filename}'")

def clear_fields():
    contract_signed_date_entry.set_date(datetime.today())
    contract_total_entry.delete(0, tk.END)
    project_name_entry.delete(0, tk.END)
    project_type_var.set("Landscape")
    project_progress_var.set("Not Started")
    hoa_approval_var.set("No")
    permitting_var.set("No")

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

ttk.Label(frame, text="Contract Total: ").grid(row=1, column=0, padx=5, pady=5)
contract_total_entry = ttk.Entry(frame, width=30)
contract_total_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Project Name: ").grid(row=2, column=0, padx=5, pady=5)
project_name_entry = ttk.Entry(frame, width=30)
project_name_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame, text="Project Type: ").grid(row=3, column=0, padx=5, pady=5)
project_type_var = tk.StringVar(value="Landscape")
project_type_menu = ttk.OptionMenu(frame, project_type_var, "Landscape", *project_type)
project_type_menu.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame, text="Project Progress: ").grid(row=4, column=0, padx=5, pady=5)
project_progress_var = tk.StringVar(value="Not Started")
project_progress_menu = ttk.OptionMenu(frame, project_progress_var, "Not Started", *project_progress)
project_progress_menu.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame, text="HOA Approval: ").grid(row=5, column=0, padx=5, pady=5)
hoa_approval_var = tk.StringVar(value="No")
hoa_approval_menu = ttk.OptionMenu(frame, hoa_approval_var, "No", *have_hoa)
hoa_approval_menu.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(frame, text="Permitting: ").grid(row=6, column=0, padx=5, pady=5)
permitting_var = tk.StringVar(value="No")
permitting_menu = ttk.OptionMenu(frame, permitting_var, "No", *have_permit)
permitting_menu.grid(row=6, column=1, padx=5, pady=5)

save_button = ttk.Button(frame, text="Save Job Lists", command=save_invoice)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

clear_button = ttk.Button(frame, text="Clear Fields", command=clear_fields)
clear_button.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
