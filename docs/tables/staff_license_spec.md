# Staff License Table Specification

## Table Details
- **Table Name**: `u_staff_license`
- **Table Label**: Staff License
- **Extends**: Base Table
- **Auto Number**: Yes (format: LIC0001000)

## Field Specifications

### Staff Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| staff_member | Reference | - | Yes | sys_user |
| license_type | Choice | - | Yes | Veterinarian, Veterinary Technician, Veterinary Assistant, Specialist, Relief Staff |
| license_category | Choice | - | No | DVM, LVT, CVT, RVT, Specialist Certification |
| license_number | String | 50 | Yes | - |
| issuing_authority | String | 100 | Yes | - |
| issuing_state | Choice | - | Yes | AL, AK, AZ, AR, CA, CO, CT, DE, FL, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY |

### License Dates
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| issue_date | Date | - | Yes | - |
| expiration_date | Date | - | Yes | - |
| renewal_due_date | Date | - | No | - |
| last_renewed_date | Date | - | No | - |
| grace_period_end | Date | - | No | - |

### Status and Compliance
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| license_status | Choice | - | Yes | Active, Expired, Suspended, Revoked, Pending Renewal, Under Review |
| compliance_status | Choice | - | Yes | Compliant, Expiring Soon, Expired, Non-Compliant |
| days_until_expiration | Integer | - | No | - |
| renewal_reminder_sent | Boolean | - | No | - |
| renewal_reminder_date | Date | - | No | - |

### Continuing Education
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| ce_hours_required | Integer | - | No | - |
| ce_hours_completed | Integer | - | No | - |
| ce_compliance_status | Choice | - | No | Compliant, Deficient, Not Required |
| ce_deadline | Date | - | No | - |

### Documentation
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| license_document | Attachment | - | No | - |
| renewal_documentation | Attachment | - | No | - |
| notes | String | 1000 | No | - |
| audit_trail | String | 2000 | No | - |

## Business Rules
1. **Auto-calculate Days Until Expiration**: expiration_date - current_date
2. **Auto-set Compliance Status**: Based on days_until_expiration (30+ days = Compliant, 1-30 days = Expiring Soon, <0 = Expired)
3. **Renewal Reminder**: Send notification 60 days, 30 days, and 7 days before expiration
4. **CE Hours Validation**: ce_hours_completed cannot exceed ce_hours_required
5. **Status Workflow**: Track license status changes with audit trail

## Form Layout
1. **Staff & License Info**: staff_member, license_type, license_category, license_number, issuing_authority, issuing_state
2. **Important Dates**: issue_date, expiration_date, renewal_due_date, last_renewed_date
3. **Status**: license_status, compliance_status, days_until_expiration
4. **Continuing Education**: ce_hours_required, ce_hours_completed, ce_compliance_status, ce_deadline
5. **Documentation**: license_document, renewal_documentation, notes
6. **Reminders**: renewal_reminder_sent, renewal_reminder_date

## Scheduled Jobs
1. **Daily License Check**: Update compliance_status and days_until_expiration
2. **Renewal Reminder**: Send email notifications based on expiration dates
3. **CE Compliance Check**: Monitor continuing education requirements
