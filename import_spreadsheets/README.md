# ServiceNow Table Import Spreadsheets

## Overview
This directory contains CSV spreadsheets formatted for importing table structures into ServiceNow Studio for the Veterinary ServiceNow application.

## Import Instructions

### Step 1: Access ServiceNow Studio
1. Log into your ServiceNow instance: `https://dev221089.service-now.com`
2. Navigate to **System Applications > Studio**
3. Open your "Veterinary ServiceNow" application

### Step 2: Import Tables Using Data Sources
1. Go to **System Import Sets > Load Data**
2. Choose **Create table from spreadsheet** option
3. Upload each CSV file in the following order:

## Recommended Import Order

### 1. Patient Record Table
- **File**: `patient_record_table_import.csv`
- **Table Name**: `u_patient_record`
- **Table Label**: "Patient Record"
- **Auto Number**: Yes
- **Create Module**: Yes

### 2. Staff License Table
- **File**: `staff_license_table_import.csv`
- **Table Name**: `u_staff_license`
- **Table Label**: "Staff License"
- **Auto Number**: Yes
- **Create Module**: Yes

### 3. Inventory Item Table
- **File**: `inventory_item_table_import.csv`
- **Table Name**: `u_inventory_item`
- **Table Label**: "Inventory Item"
- **Auto Number**: Yes
- **Create Module**: Yes

### 4. Appointment Table
- **File**: `appointment_table_import.csv`
- **Table Name**: `u_appointment`
- **Table Label**: "Appointment"
- **Auto Number**: Yes
- **Create Module**: Yes
- **Note**: Import after Patient Record (has reference field)

### 5. Treatment Table
- **File**: `treatment_table_import.csv`
- **Table Name**: `u_treatment`
- **Table Label**: "Treatment"
- **Auto Number**: Yes
- **Create Module**: Yes
- **Note**: Import after Patient Record and Appointment

### 6. Vaccine Record Table
- **File**: `vaccine_record_table_import.csv`
- **Table Name**: `u_vaccine_record`
- **Table Label**: "Vaccine Record"
- **Auto Number**: Yes
- **Create Module**: Yes
- **Note**: Import after Patient Record and Inventory Item

## Important Notes

### Field Type Mapping
- **String**: Text field with specified max length
- **Choice**: Dropdown with predefined options (values separated by semicolons)
- **Reference**: Link to another table
- **Date/Date Time**: Date/timestamp fields
- **Boolean**: True/false checkbox
- **Integer**: Whole numbers
- **Decimal**: Numbers with decimal places
- **Currency**: Money values
- **HTML**: Rich text fields
- **Email**: Email address validation

### Choice List Values
Choice fields include predefined options. ServiceNow will create choice lists automatically:

**Species**: dog, cat, bird, rabbit, reptile, other
**Gender**: male, female, neutered, spayed
**Appointment Type**: routine_checkup, vaccination, surgery, emergency, dental, grooming, consultation
**Status Fields**: Various status options for each table

### Reference Fields
Reference fields link tables together:
- `u_patient` → Links to Patient Record table
- `u_staff` → Links to Staff/User table
- `u_appointment` → Links to Appointment table
- `u_inventory_item` → Links to Inventory Item table

## Post-Import Configuration

After importing all tables:

### 1. Configure Reference Fields
- Verify reference fields point to correct tables
- Set up reference qualifiers if needed
- Configure dependent fields

### 2. Set Up Choice Lists
- Review and modify choice list values
- Add additional options as needed
- Set default values

### 3. Configure Display Fields
- Set which fields appear in lists
- Configure form layouts
- Set mandatory fields

### 4. Add Business Rules
- Implement auto-generation of IDs
- Add validation rules
- Set up notifications

## Alternative Import Method: Excel Files

If you prefer Excel format:
1. Open any CSV file in Excel
2. Save as `.xlsx` format
3. Use the same import process in ServiceNow

## Troubleshooting

### Common Issues:
1. **Reference field errors**: Import referenced tables first
2. **Choice list issues**: Verify semicolon-separated values
3. **Field length errors**: Check max length specifications
4. **Mandatory field issues**: Ensure required fields are marked correctly

### Import Validation:
After each import:
1. Verify table structure in **System Definition > Tables**
2. Check field properties and types
3. Test creating a record manually
4. Verify choice lists are populated

## Next Steps After Import

Once all tables are imported:
1. Create Business Rules (auto-ID generation, validation)
2. Design Forms and Lists
3. Set up Workflows
4. Configure Security (ACLs)
5. Build Virtual Agent
6. Set up Integrations

## Support Files

All table specifications are documented in detail in:
- `/docs/tables/` - Complete field specifications
- `/docs/implementation/deployment_guide.md` - Full implementation guide

The CSV files in this directory provide the exact structure needed for ServiceNow table creation with proper field types, lengths, and relationships.
