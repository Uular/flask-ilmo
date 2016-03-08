from flask import render_template, flash, redirect, url_for
from datetime import datetime
from ilmo import app, db
from .models import KmpEntry, HumuEntry
from .forms import KmpForm, HumuForm


@app.route('/', methods=['GET', 'POST'])
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
    form = HumuForm()
    avec = HumuForm(prefix='avec')

    starttime = datetime(2016, 2, 28, 12, 00, 00)
    othertime = datetime(2016, 3, 7, 12, 00)
    endtime = datetime(2016, 3, 9, 23, 59, 59)
    nowtime=datetime.now()

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

    if form.validate_on_submit() and (form.avec.data and avec.validate_on_submit):

        flash('Kiitos ilmoittautumisesta, {}'.format(form.name.data))
        sub = HumuEntry(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            guild=form.guild.data,
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('kmp'))
    elif form.is_submitted():
        flash("Ilmoittautuminen epäonnistui!")

    return render_template('humusitsit.html',
                           title='KMP 2016',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           othertime=othertime,
                           form=form,
                           avec=avec,
                           count=count,
                           guilds=guilds)