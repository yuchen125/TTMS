# Generated by Django 2.1 on 2019-05-28 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=10, verbose_name='影厅名称')),
                ('cinema_detail', models.CharField(max_length=50, verbose_name='影厅描述')),
                ('cinema_row', models.IntegerField(verbose_name='影厅行座位')),
                ('cinema_column', models.IntegerField(verbose_name='影厅列座位')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=20, verbose_name='影片名称')),
                ('movie_detail', models.CharField(max_length=50, verbose_name='影片描述')),
                ('movie_price', models.IntegerField(verbose_name='影片价格')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_start_time', models.DateTimeField(verbose_name='开始时间')),
                ('plan_end_time', models.DateTimeField(verbose_name='结束时间')),
                ('plan_cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_plan', to='repository.Cinema')),
                ('plan_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_plan', to='repository.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_row', models.IntegerField(verbose_name='座位行')),
                ('seat_column', models.IntegerField(verbose_name='座位列')),
                ('seat_status', models.BooleanField(choices=[(0, '未售出'), (1, '已售出')], max_length=1, verbose_name='座位状态')),
                ('seat_cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_seat', to='repository.Cinema', verbose_name='影厅座位')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='账号')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('sex', models.BooleanField(choices=[(0, '男'), (1, '女')], max_length=1, verbose_name='性别')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='cinema_movie',
            field=models.ManyToManyField(related_name='movie_cinema', to='repository.Movie'),
        ),
    ]
