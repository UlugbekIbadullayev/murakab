from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel

class Event(BaseModel):
    organizer = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, related_name='events',related_query_name='events')

    title = models.CharField(_("title"), max_length=50)
    overview = models.TextField(_("overview"))
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"))

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
