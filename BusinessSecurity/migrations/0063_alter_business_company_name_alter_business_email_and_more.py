# Generated by Django 4.1.3 on 2022-11-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BusinessSecurity", "0062_auto_20220425_1247"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="company_name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="business",
            name="email",
            field=models.EmailField(max_length=255, verbose_name="Company Email"),
        ),
        migrations.AlterField(
            model_name="business",
            name="industry_type",
            field=models.CharField(
                choices=[
                    ("software_companies", "Software Companies"),
                    ("government_agencies", "Government Agencies"),
                    ("law_enforcement", "Law Enforcement"),
                    ("financial_institutes", "Financial Institutes"),
                    ("telecommunication_companies", "Telecommunication Companies"),
                    ("wealth_management", "Wealth Management"),
                    ("educational_institutes", "Educational Institute"),
                    ("isp_companies", "ISP Companies"),
                    ("ecommerce_business", "Ecommerce Business"),
                    ("law_firm", "Law Firm"),
                    ("small_and_medium_business", "Small and Medium Business"),
                    ("health_care_institutes", "Health Care Institutes"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="business",
            name="website",
            field=models.URLField(default="https://", max_length=255),
        ),
        migrations.AlterField(
            model_name="events",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="events",
            name="category",
            field=models.CharField(
                choices=[
                    ("for_business_security", "For Business CyberSecurity"),
                    ("for_personal_security", "For Personal CyberSecurity"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="events",
            name="event_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="events",
            name="medium",
            field=models.CharField(
                choices=[("online", "Online"), ("offline", "Offline")], max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="events",
            name="speaker",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="events",
            name="status",
            field=models.CharField(
                choices=[
                    ("active", "Active"),
                    ("completed", "completed"),
                    ("canceled", "canceled"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="inputfields",
            name="placeholder",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="inputfields",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "text"),
                    ("number", "number"),
                    ("file", "file"),
                    ("select", "select"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="service_title",
            field=models.CharField(max_length=255, verbose_name="Service Title"),
        ),
        migrations.AlterField(
            model_name="servicecategory",
            name="category_name",
            field=models.CharField(max_length=255, verbose_name="Category Name"),
        ),
        migrations.AlterField(
            model_name="subscriptionbasedpackage",
            name="duration_type",
            field=models.CharField(
                choices=[("month", "Month"), ("year", "Year")],
                default="month",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="subscriptionbasedpackage",
            name="package_name",
            field=models.CharField(max_length=255, verbose_name="Package Name"),
        ),
        migrations.AlterField(
            model_name="subscriptionfeatures",
            name="feature",
            field=models.CharField(max_length=255, verbose_name="Feature"),
        ),
        migrations.AlterField(
            model_name="subscriptionfeatures",
            name="feature_name",
            field=models.CharField(max_length=255, verbose_name="Feature Name"),
        ),
        migrations.AlterField(
            model_name="subscriptionservices",
            name="service_title",
            field=models.CharField(max_length=255, verbose_name="Service Title"),
        ),
        migrations.AlterField(
            model_name="subservice",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="usersbusiness",
            name="position",
            field=models.CharField(default="staff", max_length=255),
        ),
        migrations.AlterField(
            model_name="usersbusiness",
            name="privilege",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("general_admin", "General Admin"),
                    ("general_staff", "General Staff"),
                ],
                default="general_staff",
                max_length=255,
            ),
        ),
    ]
