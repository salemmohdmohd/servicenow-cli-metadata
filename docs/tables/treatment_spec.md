# Treatment Table Specification

## Table Details
- **Table Name**: `u_treatment`
- **Table Label**: Treatment Record
- **Extends**: Base Table
- **Auto Number**: Yes (format: TRT0001000)

## Field Specifications

### Treatment Details
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| patient | Reference | - | Yes | u_patient_record |
| appointment | Reference | - | No | u_appointment |
| treatment_date | Date/Time | - | Yes | - |
| treatment_type | Choice | - | Yes | Vaccination, Surgery, Examination, Dental, Diagnostic, Medication, Emergency, Grooming |
| primary_clinician | Reference | - | Yes | sys_user |
| assisting_staff | Reference | - | No | sys_user (multiple) |

### Clinical Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| diagnosis | String | 1000 | No | - |
| procedures_performed | String | 2000 | No | - |
| medications_prescribed | String | 1000 | No | - |
| dosage_instructions | String | 1000 | No | - |
| treatment_notes | String | 4000 | No | - |
| complications | String | 1000 | No | - |
| outcome | Choice | - | No | Successful, Partial Success, No Improvement, Complications, Referred |

### Billing Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| service_cost | Currency | - | No | - |
| medication_cost | Currency | - | No | - |
| total_cost | Currency | - | No | - |
| insurance_covered | Boolean | - | No | - |
| insurance_amount | Currency | - | No | - |
| patient_responsibility | Currency | - | No | - |
| payment_status | Choice | - | No | Pending, Partial, Paid, Insurance Pending, Write-off |

### Follow-up
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| follow_up_required | Boolean | - | No | - |
| follow_up_date | Date | - | No | - |
| follow_up_instructions | String | 1000 | No | - |
| discharge_instructions | String | 1000 | No | - |

### Inventory Usage
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| supplies_used | String | 1000 | No | - |
| medication_dispensed | String | 1000 | No | - |
| inventory_notes | String | 500 | No | - |

## Business Rules
1. **Auto-calculate Total Cost**: service_cost + medication_cost = total_cost
2. **Auto-calculate Patient Responsibility**: total_cost - insurance_amount
3. **Inventory Deduction**: Automatically reduce inventory when supplies/medications are used
4. **Treatment Validation**: Cannot create treatment without valid patient
5. **Date Validation**: Treatment date cannot be in the future

## Form Layout
1. **Treatment Info**: patient, appointment, treatment_date, treatment_type, primary_clinician
2. **Clinical Details**: diagnosis, procedures_performed, medications_prescribed, dosage_instructions
3. **Treatment Notes**: treatment_notes, complications, outcome
4. **Billing**: service_cost, medication_cost, total_cost, insurance_covered, insurance_amount, payment_status
5. **Follow-up**: follow_up_required, follow_up_date, follow_up_instructions, discharge_instructions
6. **Inventory**: supplies_used, medication_dispensed, inventory_notes

## Related Lists
- **Follow-up Appointments**: Future appointments related to this treatment
- **Billing Records**: Payment history for this treatment
