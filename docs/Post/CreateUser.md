# CreateUser

Crear un usuario con validaciones de email y reglas de negocio para estado inicial

**Repository**: `PostRepository`

## Input

| Field | Type | Required |
|-------|------|----------|
| name | string | Yes |
| email | string | Yes |
| status | UserStatus | No |

## Output

| Field | Type |
|-------|------|
| data | User |
