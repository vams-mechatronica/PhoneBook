from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class PhoneBookCustomerCare(models.Model):
    companyName = models.CharField(_("Company Name"), max_length=50,null=True,blank=True)
    companyLocation = models.CharField(_("Company Location"), max_length=50,null=True,blank=True)
    country = models.CharField(_("Country"), max_length=50,null=True,blank=True)
    contactNo = models.CharField(_("Contact No"), max_length=50,null=True,blank=True)
    status = models.BooleanField(_("Status"),null=True,blank=True)

    def __str__(self) -> str:
        return self.companyName