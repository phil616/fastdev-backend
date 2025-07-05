from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)

    class Meta:
        table = "users"
