from django.db import models

# Create your models here.
"""

"""
class LongTermPermit(models.Model):
    photo = models.ImageField(upload_to='permit_photos')
    applicant_name = models.CharField(max_length=100)
    employer_name = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100)
    trainee_at_expiry = models.CharField(max_length=100)
    long_term_trainee = models.CharField(max_length=100)
    condition = models.TextField()
    variation_of_conditions = models.TextField()
    authorized_officer = models.CharField(max_length=100)
    permit_number = models.CharField(max_length=20, unique=True, blank=True)

    # Override the save method to generate the permit number
    def save(self, *args, **kwargs):
        if not self.permit_number:
            year = str(self.date_from.year)
            permit_count = LongTermPermit.objects.filter(date_from__year=self.date_from.year).count() + 1
            letter = chr(ord('A') + permit_count - 1)
            self.permit_number = f"{permit_count}/{year}/{letter}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.applicant_name

class EmergencyWorkPermit(models.Model):
    pass

class RecruitersLicense(models.Model):
    pass

class WorkExemptionPermit(models.Model):
    pass