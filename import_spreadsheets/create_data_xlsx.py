import pandas as pd
import os

# Get the directory path
dir_path = "/Users/salemmohd/Documents/GitHub/sn-cli-metadata/import_spreadsheets"
os.chdir(dir_path)

# Create Patient Records Data
patient_data = {
    "Patient Name": [
        "Buddy",
        "Whiskers",
        "Rex",
        "Mittens",
        "Charlie",
        "Luna",
        "Max",
        "Bella",
    ],
    "Owner Name": [
        "John Smith",
        "Sarah Johnson",
        "Mike Davis",
        "Lisa Chen",
        "Robert Brown",
        "Emily Wilson",
        "David Garcia",
        "Jennifer Taylor",
    ],
    "Owner Phone": [
        "(555) 123-4567",
        "(555) 234-5678",
        "(555) 345-6789",
        "(555) 456-7890",
        "(555) 567-8901",
        "(555) 678-9012",
        "(555) 789-0123",
        "(555) 890-1234",
    ],
    "Owner Email": [
        "john.smith@email.com",
        "sarah.j@email.com",
        "mdavis@email.com",
        "lisa.chen@email.com",
        "rbrown@email.com",
        "emily.w@email.com",
        "david.g@email.com",
        "jennifer.t@email.com",
    ],
    "Species": ["dog", "cat", "dog", "cat", "dog", "cat", "dog", "cat"],
    "Breed": [
        "Golden Retriever",
        "Maine Coon",
        "German Shepherd",
        "Domestic Shorthair",
        "Labrador Mix",
        "Persian",
        "Border Collie",
        "Siamese",
    ],
    "Date of Birth": [
        "2019-03-15",
        "2020-11-22",
        "2018-07-08",
        "2021-05-10",
        "2017-12-03",
        "2019-09-14",
        "2020-01-28",
        "2022-04-06",
    ],
    "Gender": [
        "neutered",
        "spayed",
        "male",
        "female",
        "neutered",
        "spayed",
        "male",
        "spayed",
    ],
    "Weight": [65.5, 12.3, 78.2, 8.7, 72.1, 11.8, 55.4, 9.2],
    "Microchip Number": [
        "982000123456789",
        "982000234567890",
        "982000345678901",
        "982000456789012",
        "982000567890123",
        "982000678901234",
        "982000789012345",
        "982000890123456",
    ],
    "Medical History": [
        "Healthy adult dog. Previous ACL surgery 2022.",
        "Indoor cat. History of urinary issues.",
        "Working dog. Joint supplements.",
        "Young healthy cat. Recently adopted.",
        "Senior dog. Arthritis management.",
        "Indoor cat. Regular grooming needed.",
        "Active dog. No major health issues.",
        "Young cat. All vaccinations current.",
    ],
    "Allergies": [
        "None known",
        "Chicken",
        "None known",
        "Fish",
        "None known",
        "None known",
        "Grass pollen",
        "None known",
    ],
    "Current Medications": [
        "Heartworm prevention monthly",
        "Urinary health formula food",
        "Joint supplement daily",
        "None",
        "Arthritis medication twice daily",
        "None",
        "Allergy medication as needed",
        "None",
    ],
    "Emergency Contact": [
        "Jane Smith (555) 987-6543",
        "Mike Johnson (555) 876-5432",
        "Sarah Davis (555) 765-4321",
        "David Chen (555) 654-3210",
        "Mary Brown (555) 543-2109",
        "Tom Wilson (555) 432-1098",
        "Maria Garcia (555) 321-0987",
        "Mark Taylor (555) 210-9876",
    ],
    "Insurance Provider": [
        "PetSure Insurance",
        "VetCare Plus",
        "Healthy Paws",
        "ASPCA Insurance",
        "Embrace Pet Insurance",
        "Petplan",
        "Trupanion",
        "FIGO Pet Insurance",
    ],
}

# Create Appointment Data
appointment_data = {
    "Patient Name": [
        "Buddy",
        "Whiskers",
        "Rex",
        "Mittens",
        "Charlie",
        "Luna",
        "Max",
        "Bella",
    ],
    "Appointment Date": [
        "2025-09-20 10:00:00",
        "2025-09-20 14:30:00",
        "2025-09-21 09:15:00",
        "2025-09-21 11:00:00",
        "2025-09-22 15:45:00",
        "2025-09-23 10:30:00",
        "2025-09-23 14:00:00",
        "2025-09-24 16:15:00",
    ],
    "Appointment Type": [
        "routine_checkup",
        "vaccination",
        "consultation",
        "routine_checkup",
        "medication_review",
        "grooming",
        "vaccination",
        "routine_checkup",
    ],
    "Veterinarian": [
        "Dr. Smith",
        "Dr. Johnson",
        "Dr. Smith",
        "Dr. Martinez",
        "Dr. Johnson",
        "Dr. Martinez",
        "Dr. Smith",
        "Dr. Johnson",
    ],
    "Status": [
        "scheduled",
        "scheduled",
        "scheduled",
        "scheduled",
        "scheduled",
        "scheduled",
        "scheduled",
        "scheduled",
    ],
    "Duration": [60, 30, 45, 60, 30, 90, 30, 60],
    "Room": [
        "Room 1",
        "Room 2",
        "Room 1",
        "Room 3",
        "Room 2",
        "Grooming",
        "Room 3",
        "Room 1",
    ],
    "Reason": [
        "Annual wellness exam",
        "Annual vaccinations",
        "Joint pain evaluation",
        "6-month kitten checkup",
        "Arthritis medication adjustment",
        "Full grooming service",
        "Puppy vaccination series",
        "Kitten health check",
    ],
    "Total Cost": [150.00, 85.00, 120.00, 90.00, 75.00, 65.00, 95.00, 110.00],
    "Payment Status": [
        "pending",
        "pending",
        "pending",
        "pending",
        "pending",
        "pending",
        "pending",
        "pending",
    ],
}

# Create Staff License Data
staff_license_data = {
    "Staff Member": [
        "Dr. Smith",
        "Dr. Johnson",
        "Dr. Martinez",
        "Nurse Williams",
        "Tech Anderson",
    ],
    "License Type": [
        "veterinary_license",
        "veterinary_license",
        "veterinary_license",
        "veterinary_technician",
        "veterinary_technician",
    ],
    "License Number": [
        "VET-12345-CA",
        "VET-23456-CA",
        "VET-34567-CA",
        "VT-45678-CA",
        "VT-56789-CA",
    ],
    "Issuing Authority": [
        "California Veterinary Medical Board",
        "California Veterinary Medical Board",
        "California Veterinary Medical Board",
        "California Veterinary Medical Board",
        "California Veterinary Medical Board",
    ],
    "Issue Date": [
        "2018-06-15",
        "2019-03-22",
        "2020-01-10",
        "2019-09-05",
        "2021-04-18",
    ],
    "Expiration Date": [
        "2026-06-15",
        "2027-03-22",
        "2028-01-10",
        "2025-09-05",
        "2027-04-18",
    ],
    "License Status": ["active", "active", "active", "pending_renewal", "active"],
    "Specialty Area": [
        "Small Animal Medicine",
        "Emergency Medicine",
        "Surgery",
        "Veterinary Nursing",
        "Laboratory Technology",
    ],
    "CE Hours Required": [40, 40, 40, 20, 20],
    "CE Hours Completed": [45, 42, 38, 18, 22],
}

# Create Inventory Data
inventory_data = {
    "Item Code": [
        "MED-HW-001",
        "VAC-RAB-001",
        "SUP-SYR-010",
        "MED-ANT-001",
        "VAC-DHPP-001",
        "SUP-GLV-LRG",
        "MED-FLEA-001",
        "SUP-BAND-001",
    ],
    "Item Name": [
        "Heartgard Plus - Medium Dogs",
        "Rabies Vaccine",
        "10ml Syringes",
        "Amoxicillin 250mg",
        "DHPP Vaccine",
        "Examination Gloves Large",
        "Flea Prevention Topical",
        "Medical Bandages",
    ],
    "Category": [
        "medications",
        "vaccines",
        "supplies",
        "medications",
        "vaccines",
        "supplies",
        "medications",
        "supplies",
    ],
    "Brand": [
        "Merial",
        "Zoetis",
        "Medline",
        "Pfizer",
        "Zoetis",
        "Cardinal Health",
        "Bayer",
        "Johnson & Johnson",
    ],
    "Unit of Measure": ["box", "vial", "box", "bottle", "vial", "box", "dose", "roll"],
    "Quantity on Hand": [15, 25, 8, 12, 18, 45, 22, 35],
    "Reorder Point": [5, 10, 5, 3, 8, 20, 10, 15],
    "Reorder Quantity": [20, 30, 15, 10, 25, 50, 30, 40],
    "Unit Cost": [45.99, 12.50, 24.99, 89.99, 15.75, 18.99, 28.50, 8.99],
    "Supplier": [
        "Merial Pharmaceuticals",
        "Zoetis",
        "Medline Industries",
        "Pfizer Animal Health",
        "Zoetis",
        "Cardinal Health",
        "Bayer Animal Health",
        "Johnson & Johnson",
    ],
    "Storage Location": [
        "Pharmacy Refrigerator",
        "Vaccine Refrigerator",
        "Supply Cabinet A",
        "Pharmacy Cabinet",
        "Vaccine Refrigerator",
        "Supply Room B",
        "Pharmacy Cabinet",
        "Supply Cabinet A",
    ],
    "Controlled Substance": [False, False, False, False, False, False, False, False],
    "Auto Order": [True, True, True, True, True, True, True, True],
}

# Create Treatment Data
treatment_data = {
    "Patient Name": ["Buddy", "Whiskers", "Rex", "Mittens", "Charlie"],
    "Treatment Date": [
        "2025-08-15 10:30:00",
        "2025-09-01 14:15:00",
        "2025-08-28 11:00:00",
        "2025-08-22 15:30:00",
        "2025-09-05 16:20:00",
    ],
    "Treatment Type": [
        "routine_checkup",
        "emergency",
        "medication",
        "vaccination",
        "therapy",
    ],
    "Veterinarian": [
        "Dr. Smith",
        "Dr. Martinez",
        "Dr. Johnson",
        "Dr. Smith",
        "Dr. Johnson",
    ],
    "Diagnosis": [
        "Healthy - annual exam",
        "Urinary blockage",
        "Arthritis flare-up",
        "Vaccination routine",
        "Joint therapy",
    ],
    "Treatment Description": [
        "Complete wellness examination. All systems normal.",
        "Emergency catheterization for urinary blockage.",
        "Arthritis medication adjustment.",
        "Annual vaccination series administered.",
        "Physical therapy for joint mobility.",
    ],
    "Medications Prescribed": [
        "None",
        "Antibiotics, pain medication",
        "Updated arthritis medication",
        "None",
        "Joint supplement",
    ],
    "Treatment Outcome": [
        "successful",
        "successful",
        "ongoing",
        "successful",
        "ongoing",
    ],
    "Follow-up Required": [False, True, True, False, True],
    "Cost": [165.00, 450.00, 85.00, 95.00, 120.00],
}

# Create Vaccine Record Data
vaccine_data = {
    "Patient Name": ["Buddy", "Rex", "Mittens", "Luna", "Max"],
    "Vaccine Name": [
        "Rabies Vaccine",
        "DHPP Vaccine",
        "FVRCP Vaccine",
        "Rabies Vaccine",
        "DHPP Vaccine",
    ],
    "Vaccine Type": ["rabies", "dhpp", "fvrcp", "rabies", "dhpp"],
    "Manufacturer": ["Zoetis", "Zoetis", "Zoetis", "Zoetis", "Zoetis"],
    "Lot Number": [
        "RAB2025001",
        "DHPP2025001",
        "FVRCP2025001",
        "RAB2025002",
        "DHPP2025002",
    ],
    "Expiration Date": [
        "2026-12-31",
        "2026-11-30",
        "2026-10-31",
        "2026-12-31",
        "2026-11-30",
    ],
    "Administration Date": [
        "2025-08-15",
        "2025-08-28",
        "2025-08-22",
        "2025-09-10",
        "2025-09-15",
    ],
    "Administering Veterinarian": [
        "Dr. Smith",
        "Dr. Johnson",
        "Dr. Smith",
        "Dr. Martinez",
        "Dr. Smith",
    ],
    "Dosage": ["1ml", "1ml", "1ml", "1ml", "1ml"],
    "Route of Administration": [
        "subcutaneous",
        "subcutaneous",
        "subcutaneous",
        "subcutaneous",
        "subcutaneous",
    ],
    "Next Due Date": [
        "2026-08-15",
        "2026-08-28",
        "2026-08-22",
        "2026-09-10",
        "2026-09-15",
    ],
    "Cost": [25.00, 30.00, 28.00, 25.00, 30.00],
    "Compliance Status": [
        "compliant",
        "compliant",
        "compliant",
        "compliant",
        "compliant",
    ],
}

# Create Excel files
try:
    with pd.ExcelWriter("patient_records_data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(patient_data).to_excel(
            writer, index=False, sheet_name="Patient Records"
        )

    with pd.ExcelWriter("appointments_data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(appointment_data).to_excel(
            writer, index=False, sheet_name="Appointments"
        )

    with pd.ExcelWriter("staff_licenses_data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(staff_license_data).to_excel(
            writer, index=False, sheet_name="Staff Licenses"
        )

    with pd.ExcelWriter("inventory_data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(inventory_data).to_excel(
            writer, index=False, sheet_name="Inventory"
        )

    with pd.ExcelWriter("treatments_data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(treatment_data).to_excel(
            writer, index=False, sheet_name="Treatments"
        )

    with pd.ExcelWriter("vaccine_records_data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(vaccine_data).to_excel(
            writer, index=False, sheet_name="Vaccine Records"
        )

    print("✅ Successfully created all XLSX files with actual data!")
    print("Files created:")
    print("- patient_records_data.xlsx")
    print("- appointments_data.xlsx")
    print("- staff_licenses_data.xlsx")
    print("- inventory_data.xlsx")
    print("- treatments_data.xlsx")
    print("- vaccine_records_data.xlsx")

except Exception as e:
    print(f"❌ Error creating files: {e}")
