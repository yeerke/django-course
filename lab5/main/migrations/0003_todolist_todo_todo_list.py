# Generated by Django 4.0.4 on 2022-05-04 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_is_done_task_is_completed_alter_task_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='main.todolist'),
            preserve_default=False,
        ),
    ]
