def transform_workday_user(raw: dict) -> dict:
    """
    Normalize a Workday worker record to the Saviynt user schema.
    """
    status = "Active"
    if raw.get("Termination_Date"):
        status = "Inactive"
    elif raw.get("Leave_of_Absence") == "true":
        status = "Suspended"

    return {
        "username":     raw.get("Employee_ID", "").lower(),
        "firstName":    raw.get("Legal_First_Name", "").strip(),
        "lastName":     raw.get("Legal_Last_Name", "").strip(),
        "email":        raw.get("Work_Email", "").lower(),
        "department":   raw.get("Cost_Center_Name"),
        "jobTitle":     raw.get("Job_Title"),
        "manager":      raw.get("Manager_Employee_ID"),
        "hireDate":     raw.get("Hire_Date"),
        "statuskey":    status,
        "userType":     "Employee" if raw.get("Worker_Type") == "Regular" else "Contractor",
        "location":     raw.get("Location_Name"),
        "costCenter":   raw.get("Cost_Center_Code"),
    }
