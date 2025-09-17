# Patient Record Table Specification

## Table Details
- **Table Name**: `u_patient_record`
- **Table Label**: Patient Record
- **Extends**: Base Table
- **Auto Number**: Yes (format: PAT0001000)

## Field Specifications

### Patient Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| patient_name | String | 100 | Yes | - |
| species | Choice | - | Yes | Dog, Cat, Bird, Rabbit, Reptile, Other |
| breed | String | 100 | No | - |
| date_of_birth | Date | - | No | - |
| gender | Choice | - | No | Male, Female, Unknown |
| weight | Decimal | - | No | - |
| microchip_id | String | 50 | No | - |
| color_markings | String | 255 | No | - |

### Owner Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| owner_name | String | 100 | Yes | - |
| owner_phone | Phone Number | - | Yes | - |
| owner_email | Email | - | No | - |
| owner_address | String | 255 | No | - |
| emergency_contact | String | 100 | No | - |
| emergency_phone | Phone Number | - | No | - |

### Medical Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| allergies | String | 1000 | No | - |
| current_medications | String | 1000 | No | - |
| medical_notes | String | 4000 | No | - |
| vaccination_status | Choice | - | No | Up to Date, Overdue, Unknown, Not Required |
| last_visit_date | Date | - | No | - |
| next_visit_due | Date | - | No | - |

### Status Fields
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| active | Boolean | - | Yes | - |
| patient_status | Choice | - | Yes | Active, Inactive, Deceased, Transferred |

## Form Layout
1. **Patient Info Section**: patient_name, species, breed, date_of_birth, gender, weight, microchip_id
2. **Owner Info Section**: owner_name, owner_phone, owner_email, owner_address
3. **Emergency Contact Section**: emergency_contact, emergency_phone
4. **Medical Info Section**: allergies, current_medications, vaccination_status, medical_notes
5. **Status Section**: active, patient_status, last_visit_date, next_visit_due

## Access Controls
- **Front Desk**: Read/Write all fields
- **Clinicians**: Read/Write medical fields, Read owner info
- **Managers**: Read all fields
- **Billing**: Read contact and billing-related fields
