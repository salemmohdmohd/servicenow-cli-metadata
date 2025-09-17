# Vaccine Record Table Specification

## Table Details
- **Table Name**: `u_vaccine_record`
- **Table Label**: Vaccine Record
- **Extends**: Base Table
- **Auto Number**: Yes (format: VAC0001000)

## Field Specifications

### Patient and Vaccine Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| patient | Reference | - | Yes | u_patient_record |
| vaccine_name | Choice | - | Yes | Rabies, DHPP, Bordetella, Lyme Disease, Canine Influenza, FVRCP, FeLV, FIV, Other |
| vaccine_type | Choice | - | Yes | Core, Non-Core, Legally Required |
| manufacturer | String | 100 | No | - |
| lot_number | String | 50 | No | - |
| serial_number | String | 50 | No | - |
| expiration_date | Date | - | No | - |

### Administration Details
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| administered_date | Date | - | Yes | - |
| administered_by | Reference | - | Yes | sys_user |
| administration_route | Choice | - | No | Subcutaneous, Intramuscular, Intranasal, Oral |
| dosage | String | 50 | No | - |
| injection_site | Choice | - | No | Left Shoulder, Right Shoulder, Left Hip, Right Hip, Scruff, Other |
| clinic_location | String | 100 | No | - |

### Scheduling and Compliance
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| vaccine_series | Choice | - | No | Initial, Booster, Annual, 3-Year, As Needed |
| series_number | Integer | - | No | - |
| next_due_date | Date | - | No | - |
| frequency_months | Integer | - | No | - |
| compliance_status | Choice | - | Yes | Current, Due Soon, Overdue, Not Required |
| legal_requirement | Boolean | - | No | - |

### Reaction Monitoring
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| pre_vaccine_health | Choice | - | No | Normal, Sick, Recovering, Pregnant, Nursing |
| reaction_observed | Boolean | - | No | - |
| reaction_type | Choice | - | No | None, Mild Lethargy, Swelling, Allergic Reaction, Anaphylaxis, Other |
| reaction_severity | Choice | - | No | None, Mild, Moderate, Severe |
| reaction_notes | String | 1000 | No | - |
| follow_up_required | Boolean | - | No | - |

### Certificate and Documentation
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| certificate_number | String | 50 | No | - |
| certificate_issued | Boolean | - | No | - |
| certificate_document | Attachment | - | No | - |
| tag_number | String | 50 | No | - |
| official_record | Boolean | - | No | - |

### Cost and Billing
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| vaccine_cost | Currency | - | No | - |
| administration_fee | Currency | - | No | - |
| total_cost | Currency | - | No | - |
| covered_by_package | Boolean | - | No | - |
| payment_status | Choice | - | No | Pending, Paid, Insurance Pending, Waived |

### Administrative Fields
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| appointment | Reference | - | No | u_appointment |
| treatment | Reference | - | No | u_treatment |
| vaccine_protocol | String | 200 | No | - |
| veterinarian_notes | String | 1000 | No | - |
| reminder_sent | Boolean | - | No | - |
| reminder_date | Date | - | No | - |

## Business Rules
1. **Auto-calculate Next Due Date**: Based on administered_date + frequency_months
2. **Compliance Status Logic**:
   - Current: next_due_date > current_date + 30 days
   - Due Soon: next_due_date within 30 days
   - Overdue: next_due_date < current_date
3. **Reminder System**: Send notifications 30 days before next_due_date
4. **Reaction Monitoring**: Flag patients with previous severe reactions
5. **Certificate Generation**: Auto-generate certificates for legally required vaccines
6. **Series Tracking**: Track multi-dose vaccine series completion

## Form Layout
1. **Patient & Vaccine**: patient, vaccine_name, vaccine_type, manufacturer, lot_number
2. **Administration**: administered_date, administered_by, administration_route, dosage, injection_site
3. **Schedule & Compliance**: vaccine_series, next_due_date, frequency_months, compliance_status, legal_requirement
4. **Reaction Monitor**: pre_vaccine_health, reaction_observed, reaction_type, reaction_severity, reaction_notes
5. **Documentation**: certificate_number, certificate_issued, tag_number, official_record
6. **Billing**: vaccine_cost, administration_fee, total_cost, payment_status
7. **Notes**: veterinarian_notes, vaccine_protocol

## Related Lists
- **Follow-up Appointments**: Future vaccine appointments
- **Reaction History**: Previous vaccine reactions for this patient
- **Certificate Records**: Generated vaccination certificates

## Scheduled Jobs
1. **Daily Compliance Check**: Update compliance_status for all records
2. **Reminder Notifications**: Send vaccine due reminders to owners
3. **Certificate Expiration**: Alert for expiring legal certificates
