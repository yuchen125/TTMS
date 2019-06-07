from django.db import models


# Create your models here.
class Cinema(models.Model):
    cinema_name = models.CharField(max_length=10, verbose_name='影厅名称')
    cinema_detail = models.CharField(max_length=50, verbose_name='影厅描述')
    cinema_row = models.IntegerField(verbose_name='影厅行座位')
    cinema_column = models.IntegerField(verbose_name='影厅列座位')

    class Mate:
        db_table = 'cinema'

    def __str__(self):
        return self.cinema_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=20, verbose_name='影片名称')
    movie_detail = models.CharField(max_length=50, verbose_name='影片描述')
    movie_price = models.IntegerField(verbose_name='影片价格')

    class Mate:
        db_table = 'movie'

    def __str__(self):
        return self.movie_name


class Plan(models.Model):
    plan_start_time = models.DateTimeField(verbose_name='开始时间')
    plan_end_time = models.DateTimeField(verbose_name='结束时间')
    plan_movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movie_plan')
    plan_cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, related_name='cinema_plan')

    class Mate:
        db_table = 'plan'

    def __str__(self):
        return '%d-%s-%s-%s' % (
            self.id, self.plan_movie.movie_name, self.plan_cinema.cinema_name, self.plan_start_time.time())


class Seat(models.Model):
    seat_cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, related_name='cinema_seat', verbose_name='影厅座位')
    seat_row = models.IntegerField(verbose_name='座位行')
    seat_column = models.IntegerField(verbose_name='座位列')

    class Mate:
        db_table = 'seat'


class Ticket(models.Model):
    ticket_plan = models.ForeignKey('Plan', on_delete=models.CASCADE, verbose_name='plan_ticket')
    ticket_row = models.IntegerField()
    ticket_column = models.IntegerField()

    class Mate:
        db_table = 'ticket'
