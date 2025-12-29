# Entity: User

Core domain entity.

## Fields

| Name | Type | Nullable | Validation | Description |
|------|------|----------|------------|-------------|

| `id` | `int` | No | None | No description provided. |

| `name` | `string` | No | None | No description provided. |

| `email` | `string` | No | None | No description provided. |

| `status` | `UserStatus` | No | None | No description provided. |

| `created_at` | `datetime` | No | None | No description provided. |


## Domain Rules
- Managed as a strictly typed DTO.
- Immutable by default.
- Validation performed at constructor level.
