from flask import render_template, flash, redirect, url_for
import wtforms
from datetime import datetime
from ilmo import app, db
from .models import KmpEntry, HumuEntry, OksEntry
from .forms import KmpForm, HumuForm, OksForm


@app.route('/kmp', methods=['GET', 'POST'])
def kmp():
    form = KmpForm()

    starttime = datetime(2016, 2, 28, 12, 00, 00)
    othertime = datetime(2016, 3, 7, 12, 00)
    endtime = datetime(2016, 3, 9, 23, 59, 59)
    nowtime=datetime.now()

    otit = KmpEntry.query.filter_by(guild='otit').order_by('time').all()
    sik = KmpEntry.query.filter_by(guild='sik').order_by('time').all()
    muu = KmpEntry.query.filter_by(guild='muu').order_by('time').all()

    guilds = [
        {'name': 'OTiT',
         'quota': 23,
         'submissions': otit},
        {'name': 'SIK',
         'quota': 23,
         'submissions': sik},
        {'name': 'Muut',
         'quota': 0,
         'submissions': muu}
    ]
    count = KmpEntry.query.count()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta, {}'.format(form.name.data))
        sub = KmpEntry(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            guild=form.guild.data,
            station=form.station.data,
            friends=form.friends.data,
            nationality=form.nationality.data,
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('kmp'))
    elif form.is_submitted():
        flash("Ilmoittautuminen epäonnistui!")

    return render_template('kmp.html',
                           title='KMP 2016',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           othertime=othertime,
                           form=form,
                           otit=otit,
                           sik = sik,
                           muu=muu,
                           count=count,
                           guilds=guilds)


@app.route('/sitsit', methods=['GET', 'POST'])
def sitsit():




    starttime = datetime(2016, 3, 14, 12, 00, 00)
    if app.debug:
        starttime = datetime(2016, 2, 14, 12, 00, 00)
    othertime = datetime(2016, 3, 22, 23, 59, 59)
    endtime = datetime(2016, 3, 22, 23, 59, 59)
    nowtime=datetime.now()

    main_choices = [('otit', 'OTiT'), ('olo', 'OLO'), ('communica', 'Communica')]
    if nowtime > othertime:
        main_choices.append(('muu', 'Muu'))

    class MainForm(HumuForm):
        guild = wtforms.RadioField('Kilta',
                       choices=main_choices)

    main = MainForm()
    avec = HumuForm(prefix='avec')

    otit = HumuEntry.query.filter_by(guild='otit').order_by('time').all()
    olo = HumuEntry.query.filter_by(guild='olo').order_by('time').all()
    communica = HumuEntry.query.filter_by(guild='communica').order_by('time').all()
    muu = HumuEntry.query.filter_by(guild='muu').order_by('time').all()

    guilds = [
        {'name': 'OTiT',
         'quota': 40,
         'submissions': otit},
        {'name': 'OLO',
         'quota': 35,
         'submissions': olo},
        {'name': 'Communica',
         'quota': 25,
         'submissions': communica },
        {'name': 'Muut',
         'quota': 0,
         'submissions': muu}
    ]
    count = HumuEntry.query.count()

    success = main.validate_on_submit()
    avec_success = bool(main.avec.raw_data) == bool(avec.validate_on_submit())
    print("b", bool(main.avec.raw_data), avec.validate_on_submit())
    print("a", success, avec_success)

    if success and avec_success:
        mainsub = HumuEntry(
            name=main.name.data,
            email=main.email.data,
            phone=main.phone.data,
            guild=main.guild.data,
            alcohol_free=main.alcohol_free.data,
            allergies=main.allergies.data,
            wine=main.wine.data,
            mild=main.mild.data
        )

        if main.avec.data:
            if avec.guild.data == "muu":
                avec.guild.data = main.guild.data
            avecsub = HumuEntry(
                name=avec.name.data,
                email=avec.email.data,
                phone=avec.phone.data,
                guild=avec.guild.data,
                alcohol_free=avec.alcohol_free.data,
                allergies=avec.allergies.data,
                wine=avec.wine.data,
                mild=avec.wine.data,
                is_avec=True
            )
            mainsub.avec = avecsub
            db.session.add(avecsub)
        db.session.add(mainsub)
        db.session.commit()

        flash('Kiitos ilmoittautumisesta, {}'.format(main.name.data))
        return redirect(url_for('sitsit'))

    elif main.is_submitted():
        flash("Ilmoittautuminen epäonnistui!")

    return render_template('humusitsit.html',
                           title='Humanöörisitsit',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           othertime=othertime,
                           form=main,
                           avec=avec,
                           count=count,
                           guilds=guilds)


@app.route('/', methods=['GET', 'POST'])
@app.route('/oks', methods=['GET', 'POST'])
def oks():

    starttime = datetime(2016, 3, 22, 12, 00, 00)
    if app.debug:
        starttime = datetime(2015, 2, 14, 12, 00, 00)
    othertime = datetime(2016, 3, 31, 23, 59, 59)
    endtime = datetime(2016, 3, 29, 23, 59, 59)
    nowtime=datetime.now()

    main_choices = [('otit', 'OTiT'), ('sik', 'SIK'), ('blanko', 'Blanko'), ('tietotekniikka', 'Henkilökunta - Tietotekniikka'), ('tlt', 'Henkilökunta - Tietoliikennetekniikka'), ('sähkö', 'Henkilökunta - Sähkötekniikka'), ('tol', 'Henkilökunta - Tietojenkäsittely')]
    if nowtime > othertime:
        main_choices.append(('muu', 'Muu'))

    class MainForm(OksForm):
        guild = wtforms.RadioField('Kilta',
                       choices=main_choices)

    main = MainForm()

    guilds = []
    for choice in main_choices:
        subs = OksEntry.query.filter_by(guild=choice[0]).order_by('time').all()
        guild = {
            'name': choice[1],
            'submissions': subs,
            'quota': 0
        }
        if choice[0] in ('sik', 'otit', 'blanko'):
            guild['quota'] = 20
        guilds.append(guild)

    print(guilds)

    count = OksEntry.query.count()

    success = main.validate_on_submit()

    if success:
        mainsub = OksEntry(
            name=main.name.data,
            email=main.email.data,
            phone=main.phone.data,
            guild=main.guild.data,
            alcohol_free=main.alcohol_free.data,
            allergies=main.allergies.data,
            wine=main.wine.data,
            mild=main.mild.data
        )

        db.session.add(mainsub)
        db.session.commit()

        flash('Kiitos ilmoittautumisesta, {}'.format(main.name.data))
        return redirect(url_for('sitsit'))

    elif main.is_submitted():
        flash("Ilmoittautuminen epäonnistui!")

    return render_template('oks.html',
                           title='Opetuksenkehittämisseminaari',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           othertime=othertime,
                           form=main,
                           count=count,
                           guilds=guilds)
