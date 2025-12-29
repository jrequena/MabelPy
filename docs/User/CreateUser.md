# Use Case: CreateUser

## Description
Use case to create a User.

## Request (DTO)
| Field | Type | Required |
|-------|------|----------|

| `name` | `string` | Yes |

| `email` | `string` | Yes |

| `status` | `UserStatus` | Yes |

| `created_at` | `datetime` | Yes |


## Response (DTO)
| Field | Type |
|-------|------|

| `id` | `int` |

| `name` | `string` |

| `email` | `string` |

| `status` | `UserStatus` |

| `created_at` | `datetime` |


## Flow
1. Receive Request DTO.
2. Validate business rules.
3. Interact with `UserRepository`.
4. Return Response DTO.
