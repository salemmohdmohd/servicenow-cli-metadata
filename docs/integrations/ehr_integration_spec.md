# EHR Integration Specification

## Overview
Integration between Main Street Veterinary Hospital ServiceNow platform and Electronic Health Record (EHR) system for seamless patient data synchronization.

## Integration Architecture

### Connection Method
- **Protocol**: REST API with JSON payload
- **Authentication**: OAuth 2.0 with JWT tokens
- **Transport**: HTTPS with TLS 1.3
- **MID Server**: Required for secure on-premise EHR connectivity
- **Data Format**: HL7 FHIR R4 standard for medical data

### Integration Patterns
1. **Real-time Sync**: Critical patient data updates
2. **Scheduled Batch**: Daily patient record synchronization
3. **Event-driven**: Triggered by specific actions (new appointment, treatment)
4. **On-demand**: Manual sync for data verification

## Data Mapping

### Patient Record Synchronization
**ServiceNow → EHR Mapping:**
```
u_patient_record.patient_name → Patient.name
u_patient_record.species → Patient.extension.species
u_patient_record.breed → Patient.extension.breed
u_patient_record.date_of_birth → Patient.birthDate
u_patient_record.gender → Patient.gender
u_patient_record.microchip_id → Patient.identifier.microchip
u_patient_record.owner_name → Patient.contact.name
u_patient_record.owner_phone → Patient.contact.telecom.phone
u_patient_record.owner_email → Patient.contact.telecom.email
u_patient_record.allergies → AllergyIntolerance.code
u_patient_record.medical_notes → Patient.extension.notes
```

### Appointment Integration
**Bidirectional Sync:**
```
u_appointment.patient → Appointment.subject
u_appointment.appointment_date → Appointment.start
u_appointment.duration_minutes → Appointment.minutesDuration
u_appointment.appointment_type → Appointment.serviceType
u_appointment.assigned_clinician → Appointment.participant.actor
u_appointment.reason_for_visit → Appointment.reasonCode
u_appointment.appointment_status → Appointment.status
```

### Treatment Record Sync
**ServiceNow → EHR:**
```
u_treatment.patient → Encounter.subject
u_treatment.treatment_date → Encounter.period.start
u_treatment.diagnosis → Condition.code
u_treatment.procedures_performed → Procedure.code
u_treatment.medications_prescribed → MedicationRequest.medicationCodeableConcept
u_treatment.treatment_notes → Encounter.note
```

## API Endpoints

### EHR System Endpoints
```
GET /api/v1/patients → Retrieve patient list
GET /api/v1/patients/{id} → Get specific patient
POST /api/v1/patients → Create new patient
PUT /api/v1/patients/{id} → Update patient
GET /api/v1/appointments → Retrieve appointments
POST /api/v1/appointments → Create appointment
PUT /api/v1/appointments/{id} → Update appointment
GET /api/v1/treatments → Retrieve treatment records
POST /api/v1/treatments → Create treatment record
```

### ServiceNow Integration Endpoints
```
POST /api/now/table/u_patient_record → Create patient
PUT /api/now/table/u_patient_record/{sys_id} → Update patient
POST /api/now/table/u_appointment → Create appointment
PUT /api/now/table/u_appointment/{sys_id} → Update appointment
POST /api/now/table/u_treatment → Create treatment
```

## Integration Workflows

### 1. New Patient Registration
**Trigger**: New patient created in EHR
**Process:**
1. EHR sends webhook notification to ServiceNow
2. ServiceNow MID Server receives patient data
3. Data validation and transformation
4. Create u_patient_record in ServiceNow
5. Confirm successful creation to EHR
6. Update patient with ServiceNow record ID

### 2. Appointment Synchronization
**Trigger**: Appointment scheduled in either system
**Process:**
1. Source system creates appointment
2. Real-time sync to target system
3. Conflict detection and resolution
4. Staff notification of new/changed appointment
5. Calendar updates in both systems

### 3. Treatment Documentation
**Trigger**: Treatment completed in ServiceNow
**Process:**
1. Clinician completes treatment record
2. Data validation and compliance check
3. Sync treatment data to EHR
4. Update patient medical history
5. Generate billing records
6. Archive completed treatment

### 4. Daily Reconciliation
**Scheduled Process (Daily at 2 AM):**
1. Compare patient records between systems
2. Identify discrepancies
3. Generate reconciliation report
4. Auto-resolve minor differences
5. Flag major conflicts for manual review
6. Update audit logs

## Error Handling

### Connection Failures
- **Retry Logic**: Exponential backoff (1, 2, 4, 8 seconds)
- **Circuit Breaker**: Stop attempts after 5 consecutive failures
- **Fallback**: Queue operations for later processing
- **Notification**: Alert IT team of persistent failures

### Data Validation Errors
- **Schema Validation**: Ensure data format compliance
- **Business Rule Validation**: Check for logical inconsistencies
- **Duplicate Detection**: Prevent creation of duplicate records
- **Error Logging**: Detailed logs for troubleshooting

### Security Considerations
- **Token Refresh**: Automatic OAuth token renewal
- **Rate Limiting**: Respect EHR system API limits
- **Data Encryption**: All data encrypted in transit and at rest
- **Audit Trail**: Complete logging of all integration activities

## Monitoring and Alerting

### Key Metrics
1. **Sync Success Rate**: Percentage of successful data transfers
2. **Response Time**: Average API response times
3. **Error Rate**: Frequency of integration failures
4. **Data Accuracy**: Percentage of records matching between systems
5. **Uptime**: Integration service availability

### Alert Conditions
- Sync failure rate > 5%
- API response time > 5 seconds
- Authentication failures
- Data validation errors
- MID Server connectivity issues

## Configuration Management

### Environment Settings
```json
{
  "ehr_api_base_url": "https://ehr.mainstreetvet.com/api/v1",
  "oauth_client_id": "servicenow_integration",
  "sync_frequency": "real-time",
  "batch_schedule": "0 2 * * *",
  "retry_attempts": 5,
  "timeout_seconds": 30
}
```

### Data Transformation Rules
- Date/time format standardization
- Species code mapping
- Status value translation
- Unit of measure conversion
- Custom field mapping
