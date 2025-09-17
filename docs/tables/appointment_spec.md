# Appointment Table Specification

## Table Details
- **Table Name**: `u_appointment`
- **Table Label**: Appointment
- **Extends**: Base Table
- **Auto Number**: Yes (format: APT0001000)

## Field Specifications

### Appointment Details
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| patient | Reference | - | Yes | u_patient_record |
| appointment_date | Date/Time | - | Yes | - |
| duration_minutes | Integer | - | No | - |
| appointment_type | Choice | - | Yes | Routine Checkup, Vaccination, Surgery, Emergency, Follow-up, Dental, Grooming |
| appointment_status | Choice | - | Yes | Scheduled, Confirmed, In Progress, Completed, Cancelled, No Show |
| priority | Choice | - | No | Low, Normal, High, Emergency |

### Staff Assignment
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| assigned_clinician | Reference | - | Yes | sys_user |
| assigned_room | Choice | - | No | Room 1, Room 2, Room 3, Surgery Suite, Examination Room A, Examination Room B |
| support_staff | Reference | - | No | sys_user (multiple) |

### Visit Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| reason_for_visit | String | 500 | Yes | - |
| symptoms | String | 1000 | No | - |
| pre_visit_notes | String | 1000 | No | - |
| post_visit_notes | String | 1000 | No | - |
| treatment_plan | String | 1000 | No | - |

### Scheduling
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| scheduled_by | Reference | - | Yes | sys_user |
| check_in_time | Date/Time | - | No | - |
| check_out_time | Date/Time | - | No | - |
| wait_time_minutes | Integer | - | No | - |
| actual_duration_minutes | Integer | - | No | - |

### Follow-up
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| follow_up_required | Boolean | - | No | - |
| follow_up_date | Date | - | No | - |
| follow_up_notes | String | 500 | No | - |

## Business Rules
1. **Prevent Double Booking**: Same clinician cannot have overlapping appointments
2. **Room Availability**: Room cannot be double-booked
3. **Auto-Calculate Wait Time**: When check_in_time and appointment_date are set
4. **Status Progression**: Scheduled → Confirmed → In Progress → Completed
5. **Emergency Priority**: Emergency appointments override normal scheduling

## Form Layout
1. **Appointment Details**: patient, appointment_date, duration_minutes, appointment_type, priority
2. **Assignment**: assigned_clinician, assigned_room, support_staff
3. **Visit Info**: reason_for_visit, symptoms, pre_visit_notes
4. **Status**: appointment_status, scheduled_by, check_in_time, check_out_time
5. **Follow-up**: follow_up_required, follow_up_date, follow_up_notes, post_visit_notes

## Related Lists
- **Treatments**: u_treatment records linked to this appointment
- **Billing**: Charges and payments for this visit
