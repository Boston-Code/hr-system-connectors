# HR System Connectors

REST connector definitions and data transformation scripts for HR authoritative source integrations.
These connectors feed employee lifecycle events into **Saviynt EIC** for automated provisioning.

## Supported Systems

| System | Type | Status | Owner |
|---|---|---|---|
| Workday | REST (RAAS) | ✅ Production | People Technology |
| ADP Workforce Now | REST | ✅ Production | HR IT |
| SuccessFactors | OData API | 🔄 In Progress | People Technology |

## How It Works
1. HR system fires event (hire, transfer, terminate)
2. Connector retrieves full employee record
3. Transformation script normalizes to Saviynt user schema
4. Saviynt EIC evaluates rules and triggers provisioning workflows

## Adding a New Connector
See `docs/connector-guide.md` for step-by-step instructions.
