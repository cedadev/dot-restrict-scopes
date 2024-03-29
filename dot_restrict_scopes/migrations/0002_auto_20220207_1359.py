# Generated by Django 3.2.12 on 2022-02-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dot_restrict_scopes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="restrictedapplication",
            name="algorithm",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "No OIDC support"),
                    ("RS256", "RSA with SHA-2 256"),
                    ("HS256", "HMAC with SHA-2 256"),
                ],
                default="",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="restrictedapplication",
            name="authorization_grant_type",
            field=models.CharField(
                choices=[
                    ("authorization-code", "Authorization code"),
                    ("implicit", "Implicit"),
                    ("password", "Resource owner password-based"),
                    ("client-credentials", "Client credentials"),
                    ("openid-hybrid", "OpenID connect hybrid"),
                ],
                max_length=32,
            ),
        ),
    ]
