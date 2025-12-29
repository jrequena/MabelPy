# Post

Core domain entity for Post.

## Fields

| Name | Type | Nullable | Validation | Description |
|------|------|----------|------------|-------------|
| id | int | No | None | No description provided. |
| title | string | No | None | No description provided. |
| content | string | No | None | No description provided. |
| user | Relationship(BelongsTo User) | Yes | None | No description provided. |
