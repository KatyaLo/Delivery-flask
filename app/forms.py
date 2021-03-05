from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class CourierForm(FlaskForm):
    username = StringField('ФИО', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[DataRequired()])
    submit = SubmitField('Добавить курьера')

class SalaryCourierForm(FlaskForm):
    courier = StringField('Курьер', validators=[DataRequired()])
    submit = SubmitField('Рассчет ЗП курьера')

class SalaryServiceForm(FlaskForm):
    service = StringField('Сервис', validators=[DataRequired()])
    submit = SubmitField('Рассчет ЗП сервиса')

class DeliveryForm(FlaskForm):
    number = IntegerField('Номер заказа', validators=[DataRequired()])
    cost = IntegerField('Стоимость заказа', validators=[DataRequired()])
    client = StringField('Клиент', validators=[DataRequired()])
    courier = StringField('Курьер', validators=[DataRequired()])
    submit = SubmitField('Создать путевой лист')

class ClientForm(FlaskForm):
    username = StringField('ФИО', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[DataRequired()])
    service = StringField('Сервис', validators=[DataRequired()])
    station = StringField('Станция метро (номер выхода)', validators=[DataRequired()])
    cost = IntegerField('Стоимость доставки', validators=[DataRequired()])
    about = TextAreaField('Описание маршрута', validators=[DataRequired()])
    
    submit = SubmitField('Добавить клиента')
