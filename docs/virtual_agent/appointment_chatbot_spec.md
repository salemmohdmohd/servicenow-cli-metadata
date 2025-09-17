# Virtual Agent - Appointment Booking Chatbot

## Overview
AI-powered Virtual Agent for Main Street Veterinary Hospital to handle appointment booking, status inquiries, and basic information requests through natural language conversations.

## Virtual Agent Configuration

### Bot Details
- **Name**: Vet Appointment Assistant
- **Description**: Helps clients book appointments and get information
- **Channels**: Web Chat, Slack, SMS (future)
- **Language**: English (primary), Spanish (future expansion)
- **Availability**: 24/7 automated responses

### Conversation Topics

## 1. Appointment Booking Topic

### Intent: Book Appointment
**Training Phrases:**
- "I want to book an appointment"
- "Schedule a visit for my pet"
- "Can I make an appointment?"
- "Book appointment for [pet name]"
- "I need to see a vet"
- "Schedule checkup"

**Required Slots:**
```json
{
  "pet_name": {
    "type": "string",
    "prompt": "What's your pet's name?",
    "required": true
  },
  "owner_name": {
    "type": "string",
    "prompt": "What's your name?",
    "required": true
  },
  "phone_number": {
    "type": "phone",
    "prompt": "What's your phone number?",
    "required": true,
    "validation": "phone_format"
  },
  "preferred_date": {
    "type": "date",
    "prompt": "What date would you prefer?",
    "required": true,
    "validation": "future_date"
  },
  "appointment_type": {
    "type": "choice",
    "prompt": "What type of visit is this?",
    "choices": ["Routine Checkup", "Vaccination", "Sick Visit", "Emergency", "Follow-up"],
    "required": true
  },
  "reason_for_visit": {
    "type": "string",
    "prompt": "Can you briefly describe the reason for the visit?",
    "required": false
  }
}
```

**Conversation Flow:**
```
Bot: Hi! I'm here to help you book an appointment. What's your pet's name?
User: Buddy
Bot: Great! And what's your name?
User: Sarah Johnson
Bot: Thank you, Sarah. What's your phone number?
User: 555-123-4567
Bot: What date would you prefer for Buddy's appointment?
User: Tomorrow
Bot: What type of visit is this? You can choose: Routine Checkup, Vaccination, Sick Visit, Emergency, or Follow-up
User: Sick visit
Bot: Can you briefly describe what's concerning you about Buddy?
User: He's been limping
Bot: I understand Buddy has been limping. Let me check available appointments for tomorrow...

[System checks availability]

Bot: I found these available times tomorrow:
- 10:00 AM with Dr. Smith
- 2:30 PM with Dr. Jones
- 4:00 PM with Dr. Smith

Which time works best for you?
```

## 2. Check Appointment Status Topic

### Intent: Check Appointment
**Training Phrases:**
- "Check my appointment"
- "What time is my appointment?"
- "When is my pet's next visit?"
- "Appointment status"
- "Do I have an appointment scheduled?"

**Required Slots:**
```json
{
  "identifier": {
    "type": "string",
    "prompt": "I can look that up! What's your phone number or pet's name?",
    "required": true
  }
}
```

**System Integration:**
- Query u_appointment table
- Filter by owner phone or pet name
- Return upcoming appointments
- Provide appointment details

## 3. General Information Topic

### Intent: Clinic Information
**Training Phrases:**
- "What are your hours?"
- "Where are you located?"
- "Do you take emergencies?"
- "What services do you offer?"
- "How much does a checkup cost?"

**Response Templates:**
```json
{
  "hours": "We're open Monday-Friday 8 AM to 6 PM, Saturday 9 AM to 4 PM, and closed Sundays. Emergency services are available 24/7.",
  "location": "Main Street Veterinary Hospital is located at 123 Main Street, Anytown, State 12345. We're right next to the park!",
  "services": "We offer routine checkups, vaccinations, surgery, dental care, emergency services, and specialized treatments. Would you like to book an appointment?",
  "emergency": "Yes, we provide 24/7 emergency services. For immediate emergencies, please call (555) 123-VETS or come directly to our clinic."
}
```

## 4. Prescription Refill Topic

### Intent: Prescription Refill
**Training Phrases:**
- "I need a prescription refill"
- "Refill medication"
- "My pet needs more medicine"
- "Can you refill [medication name]?"

**Required Slots:**
```json
{
  "pet_name": {
    "type": "string",
    "prompt": "What's your pet's name?",
    "required": true
  },
  "medication_name": {
    "type": "string",
    "prompt": "What medication needs to be refilled?",
    "required": true
  },
  "owner_phone": {
    "type": "phone",
    "prompt": "What's your phone number for verification?",
    "required": true
  }
}
```

## Conversation Management

### Context Handling
- **Session Memory**: Remember user inputs throughout conversation
- **Context Switching**: Handle topic changes gracefully
- **Multi-turn Conversations**: Support complex booking flows

### Error Handling
```json
{
  "no_availability": "I don't see any available appointments for that date. Would you like to try a different date or be added to our waitlist?",
  "invalid_date": "I can only book appointments for future dates. What other date would work for you?",
  "system_error": "I'm having trouble accessing our scheduling system right now. Would you like me to have someone call you back, or you can call us at (555) 123-VETS?",
  "unclear_input": "I didn't quite understand that. Could you please rephrase your request?"
}
```

### Escalation Rules
1. **Complex Medical Questions**: Transfer to staff
2. **Billing Inquiries**: Route to billing department
3. **Emergencies**: Provide immediate contact information
4. **System Failures**: Offer callback or phone number
5. **Frustrated Users**: Escalate to human agent

## Integration Points

### ServiceNow Tables
```javascript
// Check availability
var appointment = new GlideRecord('u_appointment');
appointment.addQuery('appointment_date', 'BETWEEN', startTime, endTime);
appointment.addQuery('assigned_clinician', clinicianId);
appointment.query();

// Create appointment
var newAppt = new GlideRecord('u_appointment');
newAppt.initialize();
newAppt.patient = patientId;
newAppt.appointment_date = requestedDate;
newAppt.appointment_type = appointmentType;
newAppt.reason_for_visit = reason;
newAppt.appointment_status = 'Scheduled';
newAppt.insert();
```

### External Systems
- **SMS Integration**: Send confirmation texts
- **Email Integration**: Send appointment confirmations
- **Calendar Integration**: Add to staff calendars
- **EHR Integration**: Sync appointment data

## Natural Language Understanding

### Entity Recognition
```json
{
  "dates": ["tomorrow", "next week", "Monday", "June 15th"],
  "times": ["morning", "afternoon", "10 AM", "2:30 PM"],
  "pet_types": ["dog", "cat", "bird", "rabbit"],
  "urgency": ["emergency", "urgent", "routine", "ASAP"],
  "symptoms": ["limping", "vomiting", "not eating", "coughing"]
}
```

### Intent Classification
- **Booking Intent**: 95% confidence threshold
- **Information Intent**: 90% confidence threshold
- **Emergency Intent**: 99% confidence threshold
- **Fallback**: <90% confidence

## Performance Metrics

### Conversation Metrics
1. **Completion Rate**: Percentage of successful bookings
2. **Abandonment Rate**: Users who leave mid-conversation
3. **Escalation Rate**: Conversations transferred to humans
4. **Resolution Time**: Average time to complete booking
5. **User Satisfaction**: Post-conversation ratings

### Business Metrics
1. **Appointment Bookings**: Number of appointments booked via bot
2. **After-hours Engagement**: Usage outside business hours
3. **No-show Rate**: Comparison of bot vs human bookings
4. **Revenue Impact**: Appointments booked = revenue generated

## Training Data

### Sample Conversations
```
User: Hi, I need to book an appointment for my dog
Bot: I'd be happy to help you book an appointment! What's your dog's name?
User: Rex
Bot: Great! And what's your name?
User: Mike Thompson
Bot: Thank you, Mike. What's your phone number?
User: 555-987-6543
Bot: What date would you prefer for Rex's appointment?
User: This Friday
Bot: What type of visit is this? Routine Checkup, Vaccination, Sick Visit, Emergency, or Follow-up?
User: He needs his shots
Bot: Perfect! I'll look for vaccination appointments this Friday...
```

### Response Variations
- Confirmation messages (5+ variations)
- Greeting messages (3+ variations)
- Error messages (friendly, helpful tone)
- Closing messages (thank you + next steps)

## Testing Strategy

### Test Scenarios
1. **Happy Path**: Complete booking flow
2. **No Availability**: Handle fully booked days
3. **Emergency Scenarios**: Urgent appointment requests
4. **Error Recovery**: System failures and user mistakes
5. **Multi-pet Households**: Booking for multiple pets
6. **Returning Customers**: Existing patient bookings
