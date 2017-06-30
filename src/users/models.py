from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Model for User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(default=0)

    # RegEx
    phone_regex = RegexValidator(regex=r'^(?:\+?63)?[09]\d{9,12}$', message="Format: '+639999999999, 09999999999, 0744449999'. Up to 13 digits allowed.")
    num_regex = RegexValidator(regex=r'[0-9]', message="Numbers are only, up to 12 digits allowed.")

    # Personal Info
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=6, null=True)
    birthdate = models.DateField()
    civil_status = models.CharField(max_length=64, null=True)
    tel_no = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    mobile_no = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    address = models.TextField(blank=True, null=True)
    religion = models.CharField(max_length=64, null=True)
    nationality = models.CharField(max_length=64, null=True)

    # Bank Account
    bank_name = models.CharField(max_length=64, blank=True)
    bank_no = models.IntegerField(blank=True, null=True)

    # Salary and Allowance
    basic_salary = models.DecimalField(max_digits=11, decimal_places=2, null=True);
    monthly_allowance = models.DecimalField(max_digits=11, decimal_places=2, null=True);

    # Contribution Details
    tin_no = models.CharField(validators=[num_regex], max_length=12, blank=True)
    sss_no = models.CharField(validators=[num_regex], max_length=10, blank=True)
    gsis_no = models.CharField(validators=[num_regex], max_length=12, blank=True)
    pagibig_no = models.CharField(validators=[num_regex], max_length=12, blank=True)
    philhealth_no = models.CharField(validators=[num_regex], max_length=12, blank=True)

    tin_contribution = models.DecimalField(max_digits=11, decimal_places=2, null=True);
    sss_contribution = models.DecimalField(max_digits=11, decimal_places=2, null=True);
    gsis_contribution = models.DecimalField(max_digits=11, decimal_places=2, null=True);
    pagibig_contribution = models.DecimalField(max_digits=11, decimal_places=2, null=True);
    philhealth_contribution = models.DecimalField(max_digits=11, decimal_places=2, null=True);

    # Employment Info
    position = models.IntegerField(default=0, blank=True)
    department = models.IntegerField(default=0, blank=True)
    entry_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Modification log
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

# Model for User Roles
class Role(models.Model):
    code = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.code

    def __int__(self):
        return self.id

# Model for User Postion
class Position(models.Model):
    position = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.position

    def __int__(self):
        return self.id

# Model for User Department
class Department(models.Model):
    department = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.department

    def __int__(self):
        return self.id
