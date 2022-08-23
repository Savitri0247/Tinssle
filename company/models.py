from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
DOCUMENT_UPLOAD_CHOICES = (
    ('Business Bank Statement', 'Business Bank Statement'),
    ('Business Licence', 'Business Licence'),
    ('Certificate of Incorporation', 'Certificate Of Incorporations'),
    ('Goods and ServiceTax Registration', 'Goods and ServiceTax Registration'),
    ('Permanent Account Number', 'Permanent Account Number'),
    ('Shop Establishment Certificate', 'Shop Establishment Certificate'),
    ('Udhog Aadhar', 'Udhog Aadhar'),
    ('Utility Bill', 'Utility Bill'),

)


class Brand(models.Model):
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    proof_of_employement = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    brand_logo = models.ImageField(upload_to="image/", blank=True, null=True)
    industry = models.CharField(max_length=100)
    company_type = models.CharField(max_length=50)
    company_size = models.CharField(max_length=50)
    select_document = models.CharField(
        max_length=100, choices=DOCUMENT_UPLOAD_CHOICES)
    upload_document = models.ImageField(
        upload_to="image/", blank=True, null=True)


class MessageInfluencer(models.Model):
    msg = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='image1/', blank=True, null=True)
    sender = models.CharField(max_length=500)


class MessageBrand(models.Model):
    msg = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='image1/', blank=True, null=True)
    sender = models.CharField(max_length=100)


class BrandPost(models.Model):
    msg = models.CharField(max_length=500)
    file = models.ImageField(
        upload_to="postimage/", blank=True, null=True)
    video = models.FileField(upload_to='videos_uploaded_brand', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    add_external_links = models.CharField(max_length=500)
    tag = models.CharField(max_length=200)
    POST_CHOICE = (
        ('collaboration', 'collaboration'),
        ('paid promotion', 'paid promotion'),
        ('normal', 'normal'),
    )
    post_type = models.CharField(
        default='normal', max_length=100, choices=POST_CHOICE, blank=True, null=True)

    collaboration_with = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    companion_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100)

    def __str__(self):
        return self.companion_name
