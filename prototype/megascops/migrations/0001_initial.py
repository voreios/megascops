# Generated by Django 4.2.5 on 2023-10-30 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=255)),
                ('target_audience', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('registration_start_date', models.DateField()),
                ('registration_end_date', models.DateField()),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.conference')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.event')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('keywords', models.CharField(max_length=255)),
                ('submission_date', models.DateTimeField()),
                ('submission_status', models.CharField(max_length=255)),
                ('file_path', models.CharField(max_length=255)),
                ('external_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('registration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionEvaluation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('evaluation_start_date', models.DateTimeField()),
                ('evaluation_end_date', models.DateTimeField()),
                ('tags', models.CharField(max_length=255)),
                ('evaluation_status', models.CharField(max_length=255)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.user')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.submission')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionChanges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modification_date', models.DateTimeField()),
                ('modified_field', models.CharField(max_length=255)),
                ('previous_value', models.TextField()),
                ('new_value', models.TextField()),
                ('modifying_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.user')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.submission')),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.user'),
        ),
        migrations.AddField(
            model_name='submission',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.event'),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_date', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.participant')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.user'),
        ),
        migrations.CreateModel(
            name='EvaluationComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_date', models.DateTimeField()),
                ('comment_text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.user')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.submissionevaluation')),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.activity')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megascops.event'),
        ),
    ]
