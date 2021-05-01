from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Teachers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Kids(models.Model):

    gender_choices = (
        ('muski', 'Muski'),
        ('zenski', 'Zenski')
    )

    preschool_choices = (
        ('da', 'Da'),
        ('ne', 'Ne')
    )

    living_choices = (
        ('oba roditelja', 'Oba roditelja'),
        ('jednim roditeljem', 'Jednim roditeljem'),
        ('bez roditelja', 'Bez roditelja')
    )

    kindergarten_program_choice = (
        ('primarni program', 'Primarni program'),
        ('kraci program', 'Kraci program')
    )

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100, blank=True, null=True)
    city_birthday = models.CharField(max_length=100, blank=True, null=True)
    custom_id = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=gender_choices, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    contact_phone = models.CharField(max_length=100, blank=True, null=True)
    family_size = models.IntegerField(null=True, blank=True)
    living_with = models.CharField(max_length=100, choices=living_choices, null=True, blank=True)
    number_of_preschool_kids_in_family = models.IntegerField(null=True, blank=True)
    kid_already_been_in_kindergarten = models.CharField(max_length=100, choices=preschool_choices, null=True, blank=True ,default=False)

    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_education_level = models.CharField(max_length=200, blank=True, null=True)
    father_company = models.CharField(max_length=200, blank=True, null=True)

    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_education_level = models.CharField(max_length=200, blank=True, null=True)
    mother_company = models.CharField(max_length=200, blank=True, null=True)

    parent_notes = models.CharField(max_length=500, blank=True, null=True)

    program_choice = models.CharField(max_length=100, choices=kindergarten_program_choice, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Payment(models.Model):
    user = models.ForeignKey(Kids, on_delete=models.CASCADE, blank=True, null=True)
    bank_paper_id = models.IntegerField(null=True, blank=True)
    payment_date = models.CharField(max_length=100, null=True, blank=True)
    paid = models.FloatField(default=0, null=True, blank=True)
    need_to_pay = models.FloatField(default=0, null=True, blank=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['bank_paper_id']


