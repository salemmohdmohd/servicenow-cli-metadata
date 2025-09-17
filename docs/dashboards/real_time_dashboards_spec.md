# Real-Time Dashboards Specification

## Overview
Comprehensive dashboard suite for Main Street Veterinary Hospital providing real-time insights into operations, performance, and compliance metrics.

## Dashboard Architecture

### Dashboard Categories
1. **Executive Dashboard** - High-level KPIs and strategic metrics
2. **Operations Dashboard** - Daily operational metrics and alerts
3. **Clinical Dashboard** - Patient care and treatment metrics
4. **Compliance Dashboard** - Regulatory and policy compliance
5. **Financial Dashboard** - Revenue and billing performance
6. **Staff Performance Dashboard** - Employee productivity and satisfaction

## 1. Executive Dashboard

### Key Performance Indicators (KPIs)
```json
{
  "patient_satisfaction": {
    "metric": "Average satisfaction score",
    "target": ">4.5/5.0",
    "source": "u_satisfaction_response",
    "update_frequency": "real-time"
  },
  "revenue_ytd": {
    "metric": "Year-to-date revenue",
    "target": "$2.5M",
    "source": "u_treatment.total_cost",
    "update_frequency": "daily"
  },
  "appointment_utilization": {
    "metric": "Schedule utilization rate",
    "target": ">85%",
    "source": "u_appointment",
    "update_frequency": "hourly"
  },
  "compliance_rate": {
    "metric": "Overall compliance score",
    "target": ">98%",
    "source": "u_staff_license + u_vaccine_record",
    "update_frequency": "daily"
  }
}
```

### Widgets
1. **Revenue Trend Chart** (6-month rolling)
2. **Patient Volume Gauge** (current vs target)
3. **Satisfaction Score Meter** (current rating)
4. **Compliance Status Grid** (by department)
5. **Alert Summary Panel** (critical items requiring attention)

### Drill-down Capabilities
- Revenue by service type
- Patient satisfaction by clinician
- Compliance details by staff member
- Appointment trends by time period

## 2. Operations Dashboard

### Real-time Metrics
```json
{
  "current_wait_time": {
    "calculation": "AVG(check_in_time - appointment_date)",
    "display": "minutes",
    "alert_threshold": ">20 minutes"
  },
  "today_appointments": {
    "total_scheduled": "COUNT(u_appointment WHERE appointment_date = today)",
    "completed": "COUNT(u_appointment WHERE status = 'Completed' AND appointment_date = today)",
    "in_progress": "COUNT(u_appointment WHERE status = 'In Progress')",
    "remaining": "scheduled - completed - in_progress"
  },
  "room_utilization": {
    "rooms_occupied": "COUNT(u_appointment WHERE status = 'In Progress')",
    "total_rooms": 6,
    "utilization_rate": "rooms_occupied / total_rooms * 100"
  },
  "staff_availability": {
    "clinicians_available": "COUNT(sys_user WHERE active = true AND role = 'clinician' AND NOT IN current_appointments)",
    "support_staff_available": "COUNT(sys_user WHERE active = true AND role = 'support')"
  }
}
```

### Widgets
1. **Live Appointment Board** (current day schedule)
2. **Wait Time Gauge** (real-time average)
3. **Room Status Grid** (occupied/available)
4. **Staff Status Panel** (available/busy/off-duty)
5. **Emergency Alert Banner** (critical notifications)
6. **Patient Flow Chart** (check-in to check-out times)

### Alert Conditions
- Wait time >20 minutes
- Room utilization >90%
- Emergency appointments
- Staff shortages
- Equipment failures

## 3. Clinical Dashboard

### Patient Care Metrics
```json
{
  "treatment_outcomes": {
    "successful_treatments": "COUNT(u_treatment WHERE outcome = 'Successful')",
    "complications": "COUNT(u_treatment WHERE outcome = 'Complications')",
    "success_rate": "successful_treatments / total_treatments * 100"
  },
  "vaccination_compliance": {
    "up_to_date": "COUNT(u_vaccine_record WHERE compliance_status = 'Current')",
    "overdue": "COUNT(u_vaccine_record WHERE compliance_status = 'Overdue')",
    "compliance_rate": "up_to_date / (up_to_date + overdue) * 100"
  },
  "follow_up_tracking": {
    "due_today": "COUNT(u_treatment WHERE follow_up_date = today)",
    "overdue": "COUNT(u_treatment WHERE follow_up_date < today AND follow_up_required = true)",
    "completed": "COUNT(u_treatment WHERE follow_up_completed = true)"
  }
}
```

### Widgets
1. **Treatment Outcome Pie Chart** (success/complications/ongoing)
2. **Vaccination Status Gauge** (compliance percentage)
3. **Follow-up Queue List** (patients requiring follow-up)
4. **Medication Inventory Alert** (low stock items)
5. **Patient History Timeline** (recent treatments by patient)

### Clinical Alerts
- Vaccination overdue >30 days
- Follow-up appointments overdue
- Medication inventory below minimum
- Treatment complications requiring review
- Patient allergy alerts

## 4. Compliance Dashboard

### Regulatory Compliance
```json
{
  "staff_licensing": {
    "current_licenses": "COUNT(u_staff_license WHERE license_status = 'Active')",
    "expiring_soon": "COUNT(u_staff_license WHERE days_until_expiration <= 30)",
    "expired": "COUNT(u_staff_license WHERE license_status = 'Expired')",
    "compliance_rate": "current_licenses / total_staff * 100"
  },
  "continuing_education": {
    "compliant_staff": "COUNT(u_staff_license WHERE ce_compliance_status = 'Compliant')",
    "ce_compliance_rate": "compliant_staff / total_staff * 100"
  },
  "controlled_substances": {
    "inventory_reconciled": "DATE(last_dea_reconciliation)",
    "discrepancies": "COUNT(inventory_discrepancies)",
    "audit_ready": "BOOLEAN(all_records_current)"
  }
}
```

### Widgets
1. **License Status Matrix** (staff vs license types)
2. **Expiration Calendar** (upcoming renewals)
3. **CE Progress Bars** (by staff member)
4. **Controlled Substance Log** (recent transactions)
5. **Audit Readiness Indicator** (pass/fail status)

### Compliance Alerts
- License expiring within 30 days
- CE hours deficient
- Missing documentation
- Controlled substance discrepancies
- Audit preparation deadlines

## 5. Financial Dashboard

### Revenue Analytics
```json
{
  "daily_revenue": {
    "services": "SUM(u_treatment.service_cost WHERE treatment_date = today)",
    "medications": "SUM(u_treatment.medication_cost WHERE treatment_date = today)",
    "total": "services + medications"
  },
  "payment_status": {
    "collected": "SUM(u_treatment.total_cost WHERE payment_status = 'Paid')",
    "pending": "SUM(u_treatment.total_cost WHERE payment_status = 'Pending')",
    "insurance_pending": "SUM(u_treatment.total_cost WHERE payment_status = 'Insurance Pending')"
  },
  "monthly_trends": {
    "current_month": "SUM(u_treatment.total_cost WHERE MONTH(treatment_date) = current_month)",
    "previous_month": "SUM(u_treatment.total_cost WHERE MONTH(treatment_date) = previous_month)",
    "growth_rate": "(current_month - previous_month) / previous_month * 100"
  }
}
```

### Widgets
1. **Revenue Trend Line Chart** (6-month history)
2. **Payment Collection Funnel** (billed → collected)
3. **Service Mix Pie Chart** (revenue by service type)
4. **Outstanding Balances Grid** (aged receivables)
5. **Insurance Claims Status** (submitted/approved/denied)

## 6. Staff Performance Dashboard

### Productivity Metrics
```json
{
  "clinician_metrics": {
    "appointments_per_day": "COUNT(u_appointment) / clinician / day",
    "average_appointment_duration": "AVG(actual_duration_minutes)",
    "patient_satisfaction_by_clinician": "AVG(satisfaction_score) GROUP BY clinician",
    "treatment_success_rate": "successful_treatments / total_treatments BY clinician"
  },
  "efficiency_metrics": {
    "schedule_adherence": "on_time_appointments / total_appointments * 100",
    "overtime_hours": "SUM(hours_worked > 8) BY staff_member",
    "patient_throughput": "patients_seen / hours_worked"
  }
}
```

### Widgets
1. **Staff Performance Scorecard** (individual metrics)
2. **Schedule Adherence Chart** (on-time vs delayed)
3. **Patient Satisfaction by Clinician** (bar chart)
4. **Workload Distribution** (appointments per staff member)
5. **Training Progress Tracker** (CE requirements)

## Dashboard Configuration

### Update Frequencies
- **Real-time**: Wait times, room status, emergency alerts
- **Hourly**: Appointment metrics, staff availability
- **Daily**: Revenue, compliance status, patient satisfaction
- **Weekly**: Trend analysis, performance reviews
- **Monthly**: Executive summaries, strategic planning

### Access Controls
```json
{
  "executive_dashboard": ["hospital_admin", "executive", "manager"],
  "operations_dashboard": ["manager", "front_desk", "supervisor"],
  "clinical_dashboard": ["clinician", "vet_tech", "manager"],
  "compliance_dashboard": ["compliance_officer", "manager", "hr"],
  "financial_dashboard": ["billing", "manager", "executive"],
  "staff_performance": ["manager", "hr", "supervisor"]
}
```

### Mobile Responsiveness
- Responsive design for tablets and phones
- Touch-friendly interface elements
- Simplified mobile layouts
- Critical alerts push notifications
- Offline capability for essential metrics

## Technical Implementation

### Data Sources
```javascript
// Real-time appointment data
var appointments = new GlideAggregate('u_appointment');
appointments.addQuery('appointment_date', '>=', gs.beginningOfToday());
appointments.addQuery('appointment_date', '<=', gs.endOfToday());
appointments.addAggregate('COUNT');
appointments.groupBy('appointment_status');

// Wait time calculation
var waitTimes = new GlideAggregate('u_appointment');
waitTimes.addQuery('check_in_time', '!=', '');
waitTimes.addQuery('appointment_date', '>=', gs.beginningOfToday());
waitTimes.addAggregate('AVG', 'wait_time_minutes');
```

### Performance Optimization
- Cached queries for frequently accessed data
- Incremental data refreshes
- Asynchronous loading for complex calculations
- Database indexing on dashboard fields
- CDN for static dashboard assets
