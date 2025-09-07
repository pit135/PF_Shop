import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('stock', models.PositiveIntegerField(default=0)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(choices=[('jersey', 'Jersey'), ('shoes', 'Shoes'), ('ball', 'Ball'), ('accessory', 'Accessory')], max_length=50)),
                ('is_featured', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
