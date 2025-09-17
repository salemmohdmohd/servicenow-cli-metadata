# ServiceNow Implementation Guide

## Overview
Complete implementation guide for deploying the Main Street Veterinary Hospital ServiceNow system. This guide provides step-by-step instructions for configuring tables, workflows, integrations, and security settings.

## Phase 1: Environment Setup and Configuration

### 1.1 Instance Preparation
```bash
# Access ServiceNow instance
URL: https://dev221089.service-now.com
Username: admin
Authentication: MFA required

# Initial setup checklist:
☐ Verify instance access and permissions
☐ Install required plugins
☐ Configure system properties
☐ Set up development environment
☐ Create application scope
```

### 1.2 Application Creation
**Navigate to**: System Applications > Studio
1. Create new application:
   - Name: "Veterinary ServiceNow"
   - Scope: "x_vet_main" (custom scope)
   - Version: "1.0.0"
   - Description: "Main Street Veterinary Hospital Management System"

### 1.3 Required Plugin Installation
```javascript
// Install required plugins via System Definition > Plugins
var plugins = [
    'com.glide.hub.integrations',           // Integration Hub
    'sn_hr_core',                          // HR Service Delivery
    'com.snc.integration.mssp',            // Microsoft Teams Integration
    'com.glide.cs.chatbot',                // Virtual Agent
    'com.glide.platform_insights',         // Performance Analytics
    'com.glide.discovery',                 // Discovery
    'sn_grc',                             // GRC
    'com.glide.service_portal'             // Service Portal
];

// Installation script (run in background script)
plugins.forEach(function(plugin) {
    var installer = new PluginInstaller();
    installer.installPlugin(plugin);
});
```

## Phase 2: Table Creation and Configuration

### 2.1 Patient Records Table
**Navigation**: System Definition > Tables
```javascript
// Create u_patient_record table
var table = new GlideTableCreator('u_patient_record', 'Patient Record');
table.addColumn('u_patient_id', 'string', 'Patient ID', 50);
table.addColumn('u_owner_name', 'string', 'Owner Name', 100);
table.addColumn('u_owner_phone', 'string', 'Owner Phone', 20);
table.addColumn('u_owner_email', 'email', 'Owner Email', 100);
table.addColumn('u_patient_name', 'string', 'Patient Name', 100);
table.addColumn('u_species', 'choice', 'Species');
table.addColumn('u_breed', 'string', 'Breed', 100);
table.addColumn('u_date_of_birth', 'glide_date', 'Date of Birth');
table.addColumn('u_gender', 'choice', 'Gender');
table.addColumn('u_weight', 'decimal', 'Weight (lbs)');
table.addColumn('u_microchip_number', 'string', 'Microchip Number', 50);
table.addColumn('u_medical_history', 'html', 'Medical History');
table.addColumn('u_allergies', 'string', 'Allergies', 500);
table.addColumn('u_medications', 'string', 'Current Medications', 500);
table.addColumn('u_emergency_contact', 'string', 'Emergency Contact', 200);
table.addColumn('u_insurance_provider', 'string', 'Insurance Provider', 100);
table.addColumn('u_last_visit_date', 'glide_date_time', 'Last Visit Date');
table.addColumn('u_ehr_id', 'string', 'EHR System ID', 50);
table.create();

// Configure choice lists
var species = new GlideChoiceList('u_patient_record', 'u_species');
species.addChoice('dog', 'Dog');
species.addChoice('cat', 'Cat');
species.addChoice('bird', 'Bird');
species.addChoice('rabbit', 'Rabbit');
species.addChoice('reptile', 'Reptile');
species.addChoice('other', 'Other');

var gender = new GlideChoiceList('u_patient_record', 'u_gender');
gender.addChoice('male', 'Male');
gender.addChoice('female', 'Female');
gender.addChoice('neutered', 'Neutered');
gender.addChoice('spayed', 'Spayed');
```

### 2.2 Appointment Table
```javascript
// Create u_appointment table
var appointment = new GlideTableCreator('u_appointment', 'Appointment');
appointment.addColumn('u_appointment_id', 'string', 'Appointment ID', 50);
appointment.addColumn('u_patient', 'reference', 'Patient');
appointment.addColumn('u_appointment_date', 'glide_date_time', 'Appointment Date/Time');
appointment.addColumn('u_appointment_type', 'choice', 'Appointment Type');
appointment.addColumn('u_veterinarian', 'reference', 'Veterinarian');
appointment.addColumn('u_technician', 'reference', 'Technician');
appointment.addColumn('u_status', 'choice', 'Status');
appointment.addColumn('u_duration', 'integer', 'Duration (minutes)');
appointment.addColumn('u_room', 'string', 'Room', 20);
appointment.addColumn('u_reason', 'string', 'Reason for Visit', 500);
appointment.addColumn('u_notes', 'html', 'Appointment Notes');
appointment.addColumn('u_diagnosis', 'string', 'Diagnosis', 500);
appointment.addColumn('u_treatment_plan', 'html', 'Treatment Plan');
appointment.addColumn('u_follow_up_required', 'boolean', 'Follow-up Required');
appointment.addColumn('u_follow_up_date', 'glide_date', 'Follow-up Date');
appointment.addColumn('u_total_cost', 'currency', 'Total Cost');
appointment.addColumn('u_payment_status', 'choice', 'Payment Status');
appointment.addColumn('u_ehr_appointment_id', 'string', 'EHR Appointment ID', 50);
appointment.create();

// Reference field configuration
appointment.setReference('u_patient', 'u_patient_record');
appointment.setReference('u_veterinarian', 'u_staff');
appointment.setReference('u_technician', 'u_staff');
```

### 2.3 Remaining Tables Implementation
Follow the same pattern for:
- `u_treatment` (Treatment Records)
- `u_staff_license` (Staff Licensing)
- `u_inventory_item` (Inventory Management)
- `u_vaccine_record` (Vaccination Records)

*[Detailed implementation available in `/docs/tables/` directory]*

## Phase 3: Business Rules and Automation

### 3.1 Patient Record Business Rules
```javascript
// Auto-generate Patient ID
var PatientIDGenerator = Class.create();
PatientIDGenerator.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    generatePatientID: function() {
        var prefix = 'VET';
        var timestamp = new GlideDateTime().getNumericValue();
        var random = Math.floor(Math.random() * 1000);
        return prefix + timestamp.toString().slice(-6) + random.toString().padStart(3, '0');
    },

    type: 'PatientIDGenerator'
});

// Business rule: Before insert on u_patient_record
(function executeRule(current, previous /*null when async*/) {
    if (current.isNewRecord() && current.u_patient_id.nil()) {
        var generator = new PatientIDGenerator();
        current.u_patient_id = generator.generatePatientID();
    }
})(current, previous);
```

### 3.2 Appointment Scheduling Rules
```javascript
// Prevent double booking
(function executeRule(current, previous /*null when async*/) {
    if (current.u_appointment_date.hasChanged() || current.u_veterinarian.hasChanged()) {
        var conflictCheck = new GlideRecord('u_appointment');
        conflictCheck.addQuery('u_veterinarian', current.u_veterinarian);
        conflictCheck.addQuery('u_appointment_date', current.u_appointment_date);
        conflictCheck.addQuery('u_status', '!=', 'cancelled');
        conflictCheck.addQuery('sys_id', '!=', current.sys_id);
        conflictCheck.query();

        if (conflictCheck.hasNext()) {
            gs.addErrorMessage('Veterinarian is already booked at this time');
            current.setAbortAction(true);
        }
    }
})(current, previous);
```

### 3.3 Inventory Management Automation
```javascript
// Low stock alert automation
(function executeRule(current, previous /*null when async*/) {
    if (current.u_quantity_on_hand.hasChanged()) {
        var currentQty = parseInt(current.u_quantity_on_hand);
        var reorderPoint = parseInt(current.u_reorder_point);

        if (currentQty <= reorderPoint && currentQty > 0) {
            // Create low stock alert
            var alert = new GlideRecord('u_inventory_alert');
            alert.initialize();
            alert.u_inventory_item = current.sys_id;
            alert.u_alert_type = 'Low Stock';
            alert.u_current_quantity = currentQty;
            alert.u_reorder_point = reorderPoint;
            alert.u_alert_date = new GlideDateTime();
            alert.insert();

            // Send Slack notification
            var slack = new SlackNotifier();
            slack.sendInventoryAlert(current);
        }
    }
})(current, previous);
```

## Phase 4: Workflow Configuration

### 4.1 Staff Onboarding Workflow
**Navigation**: Workflow > Workflow Editor

1. Create new workflow: "Veterinary Staff Onboarding"
2. Configure workflow activities:

```javascript
// Workflow stages and activities
var onboardingStages = [
    {
        name: 'Pre-boarding',
        activities: [
            'Send welcome email',
            'Prepare workspace',
            'Order equipment',
            'Schedule orientation'
        ]
    },
    {
        name: 'Documentation',
        activities: [
            'I-9 verification',
            'Tax forms completion',
            'Emergency contacts',
            'Direct deposit setup'
        ]
    },
    {
        name: 'Licensing & Compliance',
        activities: [
            'Veterinary license verification',
            'DEA registration check',
            'Background check completion',
            'Insurance documentation'
        ]
    },
    {
        name: 'Training & Orientation',
        activities: [
            'OSHA safety training',
            'ServiceNow system training',
            'Department orientation',
            'Shadowing assignments'
        ]
    },
    {
        name: 'System Access',
        activities: [
            'IT account creation',
            'Security badge issuance',
            'EHR system access',
            'Phone system setup'
        ]
    }
];
```

### 4.2 Appointment Booking Workflow
```javascript
// Automated appointment confirmation workflow
var AppointmentWorkflow = {
    sendConfirmation: function(appointmentId) {
        var appointment = new GlideRecord('u_appointment');
        if (appointment.get(appointmentId)) {
            var patient = appointment.u_patient.getRefRecord();

            // Email confirmation
            var email = new GlideEmailOutbound();
            email.setSubject('Appointment Confirmation - ' + patient.u_patient_name);
            email.setBody(this.generateConfirmationEmail(appointment, patient));
            email.setRecipient(patient.u_owner_email.toString());
            email.send();

            // SMS confirmation (if phone number provided)
            if (patient.u_owner_phone) {
                this.sendSMSConfirmation(appointment, patient);
            }

            // Calendar invite
            this.sendCalendarInvite(appointment, patient);
        }
    },

    sendReminder: function(appointmentId) {
        // 24-hour reminder automation
        var appointment = new GlideRecord('u_appointment');
        if (appointment.get(appointmentId)) {
            // Schedule reminder via scheduled job
            var reminder = new GlideScheduledJob();
            reminder.setName('Appointment Reminder - ' + appointment.u_appointment_id);
            reminder.setScript('new AppointmentWorkflow().executeReminder("' + appointmentId + '")');
            reminder.setRunDate(this.calculateReminderTime(appointment.u_appointment_date));
            reminder.schedule();
        }
    }
};
```

## Phase 5: Virtual Agent Configuration

### 5.1 Virtual Agent Setup
**Navigation**: Virtual Agent > Designer

1. Create new Virtual Agent: "VetBot"
2. Configure topics and intents:

```javascript
// Intent configuration for appointment booking
var appointmentBookingIntent = {
    name: 'Book Appointment',
    trainingPhrases: [
        'I need to book an appointment',
        'Schedule a visit for my pet',
        'Can I make an appointment?',
        'Book appointment for my dog',
        'Schedule vet visit'
    ],
    entities: [
        {name: 'pet_name', type: 'CUSTOM'},
        {name: 'date_time', type: 'DATE_TIME'},
        {name: 'appointment_type', type: 'CHOICE'}
    ],
    responses: [
        {
            text: 'I\'d be happy to help you book an appointment! Let me gather some information.',
            followUp: 'What is your pet\'s name?'
        }
    ]
};

// Conversation flow implementation
var VetBotFlow = {
    handleAppointmentBooking: function(conversation) {
        var slots = conversation.getSlots();

        if (!slots.pet_name) {
            return this.askForPetName();
        }
        if (!slots.date_time) {
            return this.askForDateTime();
        }
        if (!slots.appointment_type) {
            return this.askForAppointmentType();
        }

        // All information collected, book appointment
        return this.confirmAndBookAppointment(slots);
    },

    confirmAndBookAppointment: function(slots) {
        var appointment = new GlideRecord('u_appointment');
        appointment.initialize();
        appointment.u_patient_name = slots.pet_name;
        appointment.u_appointment_date = slots.date_time;
        appointment.u_appointment_type = slots.appointment_type;
        appointment.u_status = 'scheduled';
        appointment.insert();

        return 'Perfect! I\'ve scheduled an appointment for ' + slots.pet_name +
               ' on ' + slots.date_time + '. Confirmation number: ' + appointment.number;
    }
};
```

### 5.2 Live Agent Handoff
```javascript
// Configure escalation to human agents
var LiveAgentHandoff = {
    checkForHandoff: function(conversation) {
        var confidence = conversation.getConfidenceScore();
        var attempts = conversation.getAttemptCount();

        if (confidence < 0.5 || attempts > 3) {
            return this.initiateHandoff(conversation);
        }
        return false;
    },

    initiateHandoff: function(conversation) {
        var case = new GlideRecord('sn_customerservice_case');
        case.initialize();
        case.short_description = 'Virtual Agent Escalation';
        case.description = conversation.getTranscript();
        case.priority = '3';
        case.state = 'Open';
        case.insert();

        return 'Let me connect you with one of our team members who can better assist you.';
    }
};
```

## Phase 6: Dashboard and Reporting Setup

### 6.1 Performance Analytics Configuration
**Navigation**: Performance Analytics > Data Collector

```javascript
// Configure data collectors for veterinary metrics
var dataCollectors = [
    {
        name: 'Daily Appointments',
        table: 'u_appointment',
        indicator: 'count',
        frequency: 'daily',
        breakdown: ['u_appointment_type', 'u_veterinarian']
    },
    {
        name: 'Revenue Tracking',
        table: 'u_appointment',
        indicator: 'sum',
        field: 'u_total_cost',
        frequency: 'daily',
        breakdown: ['u_appointment_type']
    },
    {
        name: 'Patient Satisfaction',
        table: 'u_patient_feedback',
        indicator: 'average',
        field: 'u_satisfaction_score',
        frequency: 'weekly'
    }
];

// Automated dashboard creation
dataCollectors.forEach(function(collector) {
    var dc = new GlideRecord('pa_data_collector');
    dc.initialize();
    dc.name = collector.name;
    dc.table = collector.table;
    dc.indicator = collector.indicator;
    dc.frequency = collector.frequency;
    dc.insert();
});
```

### 6.2 Real-time Dashboard Widgets
```javascript
// KPI widget configuration
var KPIWidgets = {
    dailyAppointments: {
        type: 'Number',
        query: 'u_appointmentSTATEIN1,2,3^u_appointment_dateBETWEENjavascript:gs.daysAgoStart(0)@javascript:gs.daysAgoEnd(0)',
        aggregation: 'COUNT'
    },

    totalRevenue: {
        type: 'Currency',
        query: 'u_appointmentSTATEIN3^u_appointment_dateBETWEENjavascript:gs.daysAgoStart(30)@javascript:gs.daysAgoEnd(0)',
        field: 'u_total_cost',
        aggregation: 'SUM'
    },

    lowStockItems: {
        type: 'Number',
        query: 'u_inventory_item^u_quantity_on_hand<=u_reorder_point',
        aggregation: 'COUNT'
    }
};
```

## Phase 7: Integration Implementation

### 7.1 EHR Integration Setup
**Navigation**: System Web Services > Outbound > REST Message

```javascript
// EHR REST message configuration
var ehrRestMessage = new GlideRecord('sys_rest_message');
ehrRestMessage.initialize();
ehrRestMessage.name = 'VetConnect EHR Integration';
ehrRestMessage.endpoint = 'https://api.vetconnect.com/v2/';
ehrRestMessage.authentication_type = 'oauth2';
ehrRestMessage.insert();

// HTTP methods
var methods = [
    {name: 'GET Patient', http_method: 'GET', endpoint: '${endpoint}/patients/${patient_id}'},
    {name: 'POST Patient', http_method: 'POST', endpoint: '${endpoint}/patients'},
    {name: 'PUT Patient', http_method: 'PUT', endpoint: '${endpoint}/patients/${patient_id}'},
    {name: 'GET Appointments', http_method: 'GET', endpoint: '${endpoint}/appointments'}
];

methods.forEach(function(method) {
    var httpMethod = new GlideRecord('sys_rest_message_fn');
    httpMethod.rest_message = ehrRestMessage.sys_id;
    httpMethod.function_name = method.name;
    httpMethod.http_method = method.http_method;
    httpMethod.endpoint = method.endpoint;
    httpMethod.insert();
});
```

### 7.2 MID Server Configuration
```bash
# MID Server installation and configuration
# Download MID Server from ServiceNow instance
# Extract to /opt/servicenow/mid_server/

# Configure config.xml
cat > /opt/servicenow/mid_server/agent/config.xml << EOF
<parameter name="name" value="VeterinaryHospital_MID"/>
<parameter name="url" value="https://dev221089.service-now.com"/>
<parameter name="mid.instance.username" value="mid.server"/>
<parameter name="mid.instance.password" value="encrypted_password"/>
<parameter name="mid.ssl.use_ssl" value="true"/>
EOF

# Start MID Server
cd /opt/servicenow/mid_server/agent
chmod +x start.sh
./start.sh
```

## Phase 8: Security and Access Control

### 8.1 Role Configuration
```javascript
// Create veterinary-specific roles
var roles = [
    {
        name: 'x_vet_main.veterinarian',
        description: 'Licensed veterinarian access',
        includes: ['x_vet_main.staff_base']
    },
    {
        name: 'x_vet_main.technician',
        description: 'Veterinary technician access',
        includes: ['x_vet_main.staff_base']
    },
    {
        name: 'x_vet_main.receptionist',
        description: 'Front desk and scheduling access',
        includes: ['x_vet_main.staff_base']
    },
    {
        name: 'x_vet_main.manager',
        description: 'Practice manager access',
        includes: ['x_vet_main.veterinarian', 'x_vet_main.reports']
    }
];

roles.forEach(function(role) {
    var roleRecord = new GlideRecord('sys_user_role');
    roleRecord.initialize();
    roleRecord.name = role.name;
    roleRecord.description = role.description;
    roleRecord.insert();
});
```

### 8.2 Access Control Rules (ACLs)
```javascript
// Patient record access control
var patientACL = {
    table: 'u_patient_record',
    operation: 'read',
    condition: function() {
        // Veterinarians and technicians can read all records
        if (gs.hasRole('x_vet_main.veterinarian') || gs.hasRole('x_vet_main.technician')) {
            return true;
        }
        // Receptionists can only read basic info
        if (gs.hasRole('x_vet_main.receptionist')) {
            return current.canRead('u_patient_name,u_owner_name,u_owner_phone');
        }
        return false;
    }
};

// Controlled substance access
var controlledSubstanceACL = {
    table: 'u_inventory_item',
    operation: 'write',
    condition: function() {
        if (current.u_controlled_substance == true) {
            return gs.hasRole('x_vet_main.veterinarian') || gs.hasRole('x_vet_main.pharmacy');
        }
        return gs.hasRole('x_vet_main.staff_base');
    }
};
```

## Phase 9: Testing and Validation

### 9.1 Unit Testing
```javascript
// Test suite for patient record functionality
var PatientRecordTest = Class.create();
PatientRecordTest.prototype = Object.extendsObject(TestSuite, {

    testPatientCreation: function() {
        var patient = new GlideRecord('u_patient_record');
        patient.initialize();
        patient.u_owner_name = 'John Doe';
        patient.u_patient_name = 'Buddy';
        patient.u_species = 'dog';
        patient.u_breed = 'Golden Retriever';
        patient.insert();

        this.assertEquals('VET', patient.u_patient_id.toString().substring(0, 3));
        this.assertNotNull(patient.sys_id);
    },

    testAppointmentScheduling: function() {
        var appointment = new GlideRecord('u_appointment');
        appointment.initialize();
        appointment.u_patient = this.createTestPatient();
        appointment.u_appointment_date = '2025-01-15 10:00:00';
        appointment.u_veterinarian = this.getTestVeterinarian();
        appointment.insert();

        this.assertEquals('scheduled', appointment.u_status.toString());
    },

    type: 'PatientRecordTest'
});
```

### 9.2 Integration Testing
```javascript
// EHR integration test
var EHRIntegrationTest = {
    testPatientSync: function() {
        var patient = this.createTestPatient();
        var ehrSync = new EHRSyncProcessor();
        var result = ehrSync.syncPatientToEHR(patient);

        this.assertTrue(result.success);
        this.assertNotNull(patient.u_ehr_id);
    },

    testAppointmentSync: function() {
        var appointment = this.createTestAppointment();
        var ehrSync = new EHRSyncProcessor();
        var result = ehrSync.syncAppointmentToEHR(appointment);

        this.assertTrue(result.success);
        this.assertNotNull(appointment.u_ehr_appointment_id);
    }
};
```

## Phase 10: Go-Live and Monitoring

### 10.1 Production Deployment Checklist
```bash
# Pre-deployment checklist
☐ All tables created and configured
☐ Business rules tested and validated
☐ Workflows deployed and active
☐ Integrations tested in dev environment
☐ User acceptance testing completed
☐ Security reviews passed
☐ Performance testing completed
☐ Backup and rollback procedures documented
☐ Staff training completed
☐ Support procedures established
```

### 10.2 Go-Live Monitoring
```javascript
// Production monitoring script
var ProductionMonitor = {
    checkSystemHealth: function() {
        var healthChecks = [
            this.checkTablePerformance(),
            this.checkIntegrationStatus(),
            this.checkWorkflowExecution(),
            this.checkUserActivity(),
            this.checkErrorLogs()
        ];

        healthChecks.forEach(function(check) {
            if (!check.passed) {
                this.alertSupport(check);
            }
        }.bind(this));
    },

    generateGoLiveReport: function() {
        var report = {
            appointments_created: this.countRecords('u_appointment', 1),
            patients_registered: this.countRecords('u_patient_record', 1),
            integrations_active: this.checkActiveIntegrations(),
            user_adoption: this.calculateUserAdoption(),
            system_performance: this.getPerformanceMetrics()
        };

        return report;
    }
};

// Schedule monitoring job
var monitor = new GlideScheduledJob();
monitor.setName('Veterinary System Health Check');
monitor.setScript('new ProductionMonitor().checkSystemHealth()');
monitor.setRunInterval(300); // 5 minutes
monitor.schedule();
```

### 10.3 Post Go-Live Support
```javascript
// Support ticket automation
var SupportAutomation = {
    categorizeIssue: function(incident) {
        var keywords = {
            'appointment': 'Scheduling',
            'patient': 'Patient Management',
            'login': 'Access Issues',
            'integration': 'System Integration',
            'slow': 'Performance'
        };

        var description = incident.short_description.toString().toLowerCase();

        Object.keys(keywords).forEach(function(keyword) {
            if (description.includes(keyword)) {
                incident.category = keywords[keyword];
                incident.assignment_group = this.getAssignmentGroup(keywords[keyword]);
            }
        }.bind(this));
    },

    escalateIfCritical: function(incident) {
        var criticalKeywords = ['down', 'critical', 'emergency', 'urgent'];
        var description = incident.description.toString().toLowerCase();

        if (criticalKeywords.some(keyword => description.includes(keyword))) {
            incident.priority = '1';
            incident.state = 'In Progress';
            this.notifyManagement(incident);
        }
    }
};
```

This comprehensive implementation guide provides the complete roadmap for deploying the Main Street Veterinary Hospital ServiceNow system, from initial setup through production monitoring and support.
