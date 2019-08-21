from mporm.fields import TimeField


class Model:
    created_at = TimeField(default="NOW()", not_null=True)
    updated_at = TimeField(default=None, auto_update=True)
