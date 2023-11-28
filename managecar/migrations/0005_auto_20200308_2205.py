# Generated by Django 3.0.3 on 2020-03-08 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('managecar', '0004_auto_20200308_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='pic_url',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('BLUE', 'น้ำเงิน'), ('RED', 'แดง'), ('PINK', 'ชมพู'), ('ORANGE', 'ส้ม'), ('BLACK', 'ดำ'), ('WHI', 'ขาว'), ('SILVER', 'เงิน'), ('BRONZ', 'บรอนซ์'), ('YELLOW', 'เหลือง')], max_length=10),
        ),
    ]
