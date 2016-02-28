from flask import render_template, flash, redirect, url_for
from datetime import datetime
from ilmo import app, db
from .models import KmpEntry
from .forms import KmpForm


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
