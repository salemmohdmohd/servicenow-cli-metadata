# ServiceNow Table Creation Guide

## Step-by-Step Instructions for Creating Tables in ServiceNow Studio

### Prerequisites
1. Ensure you're in ServiceNow Studio
2. Your "Veterinary ServiceNow" application is selected
3. You have table creation permissions

### Table Creation Process

#### 1. Create Patient Record Table
```
Navigation: Studio → Create Application File → Data Model → Table
- Table Label: Patient Record
- Table Name: u_patient_record (auto-generated)
- Extends: Choose "Base Table"
- Auto Number: Enable with format "PAT0001000"
```

**Add Fields (in order):**
1. patient_name (String, 100, Mandatory)
2. species (Choice: Dog,Cat,Bird,Rabbit,Reptile,Other)
3. breed (String, 100)
4. date_of_birth (Date)
5. gender (Choice: Male,Female,Unknown)
6. weight (Decimal)
7. microchip_id (String, 50)
8. owner_name (String, 100, Mandatory)
9. owner_phone (Phone Number, Mandatory)
10. owner_email (Email)
11. owner_address (String, 255)
12. emergency_contact (String, 100)
13. emergency_phone (Phone Number)
14. allergies (String, 1000)
15. current_medications (String, 1000)
16. medical_notes (String, 4000)
17. vaccination_status (Choice: Up to Date,Overdue,Unknown,Not Required)
18. patient_status (Choice: Active,Inactive,Deceased,Transferred)

#### 2. Create Appointment Table
```
Navigation: Studio → Create Application File → Data Model → Table
- Table Label: Appointment
- Table Name: u_appointment
- Extends: Base Table
- Auto Number: Enable with format "APT0001000"
```

**Add Fields:**
1. patient (Reference to u_patient_record, Mandatory)
2. appointment_date (Date/Time, Mandatory)
3. duration_minutes (Integer)
4. appointment_type (Choice: Routine Checkup,Vaccination,Surgery,Emergency,Follow-up,Dental,Grooming)
5. appointment_status (Choice: Scheduled,Confirmed,In Progress,Completed,Cancelled,No Show)
6. assigned_clinician (Reference to sys_user, Mandatory)
7. assigned_room (Choice: Room 1,Room 2,Room 3,Surgery Suite,Examination Room A,Examination Room B)
8. reason_for_visit (String, 500, Mandatory)
9. symptoms (String, 1000)
10. check_in_time (Date/Time)
11. check_out_time (Date/Time)

#### 3. Create Treatment Table
```
Navigation: Studio → Create Application File → Data Model → Table
- Table Label: Treatment Record
- Table Name: u_treatment
- Extends: Base Table
- Auto Number: Enable with format "TRT0001000"
```

**Add Fields:**
1. patient (Reference to u_patient_record, Mandatory)
2. appointment (Reference to u_appointment)
3. treatment_date (Date/Time, Mandatory)
4. treatment_type (Choice: Vaccination,Surgery,Examination,Dental,Diagnostic,Medication,Emergency,Grooming)
5. primary_clinician (Reference to sys_user, Mandatory)
6. diagnosis (String, 1000)
7. procedures_performed (String, 2000)
8. medications_prescribed (String, 1000)
9. treatment_notes (String, 4000)
10. service_cost (Currency)
11. total_cost (Currency)
12. payment_status (Choice: Pending,Partial,Paid,Insurance Pending,Write-off)

### After Creating Each Table:
1. **Configure Form Layout**: Organize fields into logical sections
2. **Set Up List Views**: Create views for different user roles
3. **Configure Access Controls**: Set permissions for front desk, clinicians, etc.
4. **Test the Table**: Create a few sample records

### Business Rules to Add:
1. **Auto-calculate fields** (e.g., total_cost, wait_time)
2. **Data validation** (e.g., appointment dates, required fields)
3. **Status workflows** (e.g., appointment progression)

### Next Steps After Table Creation:
1. Create sample data for testing
2. Build reports and dashboards
3. Set up integrations with external systems
4. Configure Virtual Agent for appointment booking
