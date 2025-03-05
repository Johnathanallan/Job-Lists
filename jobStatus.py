import tkinter as tk
from tkinter import ttk, messagebox

def calculate_cost():
    try:
        float(project_name_entry.get())

       
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def save_invoice():
    job_lists_text = f"""
    --- Landscape Project Invoice ---
    Contract Signed Date: {contract_signed_date_entry.get()}
    Project Name: {project_name_entry.get()}
    Project Type: {project_type_var.get()}
    Project Progress: {project_progress_var.get()}
    HOA Approval: {hoa_approval_var.get()}
    Permitting: {permitting_var.get()}
    ----------------------------
    
    """
    with open("Job_Profile_Lists.txt", "w") as file:
        file.write(job_lists_text)
    messagebox.showinfo("Job Lists Saved", "Invoice has been saved as 'Job_Profile_Lists.txt'")



project_type = ["Ladscape", "Concrete", "Fencing", "Decking", "Paving", "Gardening", "Driveway", "Patio", "Turfing", "Brickwork", "Walling", "Drainage", "Water Features", "Lighting", "Irrigation", "Planting", "Maintenance", "Design", "Consultation", "Other"]
project_progress = ["Not Started", "In Progress", "Completed", "On Hold", "Cancelled", "HOA Approval", "Permitting", "Design", "Consultation", "Other"]
have_hoa = ["Yes", "No"]
have_permit = ["Yes", "No"]


root = tk.Tk()
root.title("Project Management")
root.geometry("300x300")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Contract Signed Date: ").grid(row=0, column=0)
contract_signed_date_entry = ttk.Entry(frame)
contract_signed_date_entry.grid(row=0, column=1)


ttk.Label(frame, text="Project Name: ").grid(row=1, column=0)
project_name_entry = ttk.Entry(frame)
project_name_entry.grid(row=1, column=1)

ttk.Label(frame, text="Project Type: ").grid(row=2, column=0)
project_type_var = tk.StringVar(value="Landscape")
project_type_menu = ttk.OptionMenu(frame, project_type_var, "Landscape", *project_type)
project_type_menu.grid(row=2, column=1)

ttk.Label(frame, text="Project Progress: ").grid(row=3, column=0)
project_progress_var = tk.StringVar(value="Not Started")
project_progress_menu = ttk.OptionMenu(frame, project_progress_var, "Not Started", *project_progress)
project_progress_menu.grid(row=3, column=1)

ttk.Label(frame, text="HOA Approval: ").grid(row=4, column=0)
hoa_approval_var = tk.StringVar(value="No")
hoa_approval_menu = ttk.OptionMenu(frame, hoa_approval_var, "No", *have_hoa)
hoa_approval_menu.grid(row=4, column=1)

ttk.Label(frame, text="Permitting: ").grid(row=5, column=0)
permitting_var = tk.StringVar(value="No")
permitting_menu = ttk.OptionMenu(frame, permitting_var, "No", *have_permit)
permitting_menu.grid(row=5, column=1)




save_button = ttk.Button(frame, text="Save Job lists", command=save_invoice)
save_button.grid(row=6, column=0, columnspan=2)





root.mainloop()






