from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, DeliveryForm, ClientForm, CourierForm, SalaryCourierForm, SalaryServiceForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Delivery, Service, Courier, Client
from werkzeug.urls import url_parse
from datetime import datetime, date
from datetime import timedelta

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('delivery'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('delivery')
        return redirect(next_page)
    # return render_template('login.html', display='none', form=form)
    return render_template('login.html', display='none', form=form, login_data=User.query.all())

@app.route('/delivery', methods=['GET', 'POST'])
@login_required
def delivery():
    form = DeliveryForm()
    delivery = Delivery()
    if form.validate_on_submit():
        delivery.author = current_user
        delivery.courier = Courier.query.filter_by(name=form.courier.data).first()
        delivery.client = Client.query.filter_by(name=form.client.data).first()

        delivery.delivery_num = form.number.data
        delivery.delivery_cost = form.cost.data
        delivery.delivery_time = datetime.utcnow() + timedelta(hours=3)
        db.session.add(delivery)
        db.session.commit()
        return redirect(url_for('path_list'))
    return render_template('delivery.html', form=form, client_data=Client.query.all(), courier_data=Courier.query.all())

@app.route('/client', methods=['GET', 'POST'])
@login_required
def client():
    form = ClientForm()
    client = Client()
    if form.validate_on_submit():
        client.service_to_client = Service.query.filter_by(name=form.service.data).first()
        client.name = form.username.data.strip()
        client.tel = form.phone.data.strip()
        client.metro, client.exit_num = form.station.data.split('(')
        client.metro = client.metro.strip()
        if client.exit_num:
            client.exit_num = client.exit_num.replace(')', '').strip()
        client.info = form.about.data
        client.cost = form.cost.data
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('client'))
    return render_template('client.html', form=form, service_data=Service.query.all())

@app.route('/courier', methods=['GET', 'POST'])
@login_required
def courier():
    form = CourierForm()
    courier = Courier()
    if form.validate_on_submit():
        courier.name = form.username.data.strip()
        courier.tel = form.phone.data.strip()
        db.session.add(courier)
        db.session.commit()
        return redirect(url_for('courier'))
    return render_template('courier.html', form=form)

@app.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    return render_template('history.html', deliveries=Delivery.query.all())

@app.route('/salary', methods=['GET', 'POST'])
@login_required
def salary():
    formCourier = SalaryCourierForm()
    formService = SalaryServiceForm()
    if formCourier.validate_on_submit():
        try:
            courier_delivery = Delivery.query.filter_by(courier_id=Courier.query.filter_by(name=formCourier.courier.data).first().id)
            s = sum([d.client.cost - 50 for d in courier_delivery if d.delivery_time.date() == datetime.today().date()])
            return render_template('salary.html', form_courier=formCourier, form_service=formService, courier_data=Courier.query.all(), service_data=Service.query.all(), courier=s, service=False)
        except:
            pass

    if formService.validate_on_submit():
        service_delivery = Delivery.query.filter_by(courier_id=Service.query.filter_by(name=formService.service.data).first().id)
        try:
            s = sum([50 for d in service_delivery if d.delivery_time.date() == datetime.today().date()])
            return render_template('salary.html', form_courier=formCourier, form_service=formService, courier_data=Courier.query.all(), service_data=Service.query.all(), courier=False, service=s)
        except:
            pass
    return render_template('salary.html', form_courier=formCourier, form_service=formService, courier_data=Courier.query.all(), service_data=Service.query.all(), courier=False, service=False)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/path_list', methods=['GET', 'POST'])
@login_required
def path_list():
    return render_template('page.html', delivery=Delivery.query.all()[-1])