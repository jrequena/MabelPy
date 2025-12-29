# Use Case: ListUser

## Description
Use case to list a User.

## Request (DTO)
| Field | Type | Required |
|-------|------|----------|


## Response (DTO)
| Field | Type |
|-------|------|

| `items` | `List<User>` |


## Flow
1. Receive Request DTO.
2. Validate business rules.
3. Interact with `UserRepository`.
4. Return Response DTO.
