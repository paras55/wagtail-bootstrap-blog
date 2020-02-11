# Generated by Django 2.0 on 2019-09-01 13:34

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190901_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='copywritingsettings',
            name='testimonial',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())), blank=True, null=True),
        ),
    ]