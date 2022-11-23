from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('code', models.CharField(max_length=10)),
                ('tag', models.CharField(max_length=50, null=True)),
                ('time_zone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_send_time', models.DateTimeField()),
                ('text', models.TextField()),
                ('tag', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('end_send_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('S', 'send'), ('N', 'not send')], max_length=1)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='mailings.contact')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='mailings.mailing')),
            ],
        ),
    ]
