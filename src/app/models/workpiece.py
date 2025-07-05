from tortoise import Model, fields


class Workpiece(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    status = fields.CharField(max_length=255, default="正常")
    info = fields.TextField(null=True)

    class Meta:
        table = "workpiece"
