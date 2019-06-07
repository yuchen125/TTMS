from django import forms
from django.forms import fields
from django.core.exceptions import ValidationError
from repository import models
from django.forms import widgets


class CinemaForm(forms.Form):
    id = fields.IntegerField(
        required=True,
        error_messages={
            'required': '不能为空',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入影厅编号'})
    )
    cinema_name = fields.CharField(
        required=True,
        max_length=10,
        error_messages={
            'required': '影院名称不能为空',
            'max_length': '名字太长了',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入影厅名称'})
    )
    cinema_detail = fields.CharField(
        required=True,
        max_length=50,
        error_messages={
            'required': '影院描述不能为空',
            'max_length': '名字太长了',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入影厅描述'})
    )
    cinema_row = fields.IntegerField(
        required=True,
        max_value=10,
        error_messages={
            'required': '不能为空',
            'invalid': '必须为数字',
            'max_value': '数字太大了',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入座位行数'})
    )
    cinema_column = fields.IntegerField(
        required=True,
        max_value=10,
        error_messages={
            'required': '不能为空',
            'invalid': '必须为数字',
            'max_value': '数字太大了',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入座位列数'})
    )

    def clean_cinema_name(self):
        v = self.cleaned_data['cinema_name']
        if models.Cinema.objects.filter(cinema_name=v).count():
            raise ValidationError('影院已存在')
        return v

    def clean_id(self):
        v = self.cleaned_data['id']
        if models.Cinema.objects.filter(id=v).count():
            raise ValidationError('影院编号已存在')
        return v


class MovieForm(forms.Form):
    movie_name = fields.CharField(
        required=True,
        max_length=20,
        error_messages={
            'required': '影院名称不能为空',
            'max_length': '名字太长了',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入影片名称'})
    )
    movie_detail = fields.CharField(
        required=True,
        max_length=50,
        error_messages={
            'required': '影院描述不能为空',
            'max_length': '名字太长了',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入影片描述'})
    )
    movie_price = fields.IntegerField(
        required=True,
        error_messages={
            'required': '不能为空',
            'invalid': '必须为数字',
        },
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入影片价格'})
    )

    def clean_movie_name(self):
        v = self.cleaned_data['movie_name']
        if models.Movie.objects.filter(movie_name=v).count():
            raise ValidationError('影片已存在')
        return v


class PlanForm(forms.Form):
    time_list = [(0, '2019-5-28 8:00:00'), (1, '2019-5-28 10:30:00'), (2, '2019-5-28 13:00:00'),
                 (3, '2019-5-28 15:30:00')]
    plan_start_time = fields.IntegerField(
        required=True,
        error_messages={
            'required': '开始时间不能为空',
            'invalid': '时间格式不正确，应为year-month-day hh:mm:ss格式',
        },
        widget=widgets.Select(attrs={'class': 'form-control'},
                              choices=time_list)
    )
    plan_end_time = fields.DateTimeField(
        required=True,
        error_messages={
            'required': '结束时间不能为空',
            'invalid': '时间格式不正确，应为year-month-day hh:mm:ss格式'
        },
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    plan_movie = forms.ModelChoiceField(
        queryset=models.Movie.objects.all(),
        required=True,
        widget=widgets.Select(attrs={'class': 'form-control'})
    )
    plan_cinema = forms.ModelChoiceField(
        queryset=models.Cinema.objects.all(),
        required=True,
        error_messages={
            'required': '不能为空',
        },
        widget=widgets.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        value_dict = self.cleaned_data
        cinema = value_dict.get('plan_cinema')
        start_time = value_dict.get('plan_start_time')
        end_time = value_dict.get('plan_end_time')
        t = int(start_time)
        time_list = [(0, '2019-5-28 08:00:00'), (1, '2019-5-28 10:30:00'), (2, '2019-5-28 13:00:00'),
                     (3, '2019-5-28 15:30:00')]
        plan_start_time = time_list[t][1]
        if models.Plan.objects.filter(plan_cinema=cinema,
                                      plan_start_time=plan_start_time).count():
            raise ValidationError('计划安排失败')
        return self.cleaned_data


class TicketForm(forms.Form):
    ticket_plan = forms.ModelChoiceField(
        queryset=models.Plan.objects.all(),
        required=True,
        error_messages={
            'required': '计划不能为空',
        },
        widget=widgets.Select(attrs={'class': 'form-control'})
    )
    ticket_row = fields.IntegerField(
        required=True,
        error_messages={
            'required': '座位行不能为空',
            'invalid': '输入格式错误'
        },
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    ticket_column = fields.IntegerField(
        required=True,
        error_messages={
            'required': '座位列不能为空',
            'invalid': '输入格式错误'
        },
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        value_dict = self.cleaned_data
        plan = value_dict.get('ticket_plan')
        row = value_dict.get('ticket_row')
        column = value_dict.get('ticket_column')
        if models.Ticket.objects.filter(ticket_plan_id=plan, ticket_column=column, ticket_row=row).count():
            raise ValidationError('该票已被购买')
        if models.Plan.objects.filter(id=plan.id,
                                      plan_cinema__cinema_seat__seat_column=column,
                                      plan_cinema__cinema_seat__seat_row=row).count() == 0:
            raise ValidationError('座位不存在')
        return self.cleaned_data
