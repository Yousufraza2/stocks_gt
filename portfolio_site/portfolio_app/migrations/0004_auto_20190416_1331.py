# Generated by Django 2.2 on 2019-04-16 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_auto_20190404_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['symbol']},
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Symbol'),
        ),
        migrations.AlterField(
            model_name='stockpick',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockpicks', to='portfolio_app.Portfolio'),
        ),
    ]
