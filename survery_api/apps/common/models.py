from django.db.models import Model, BooleanField, DateField


# Create your models here.
class BaseModel(Model):
    created_on = DateField(auto_now_add=True)
    update_on = DateField(auto_now=True)
    is_active = BooleanField(default=True)
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True

    def recover(self):
        self.is_deleted = False

    def de_activate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
