from flask import render_template, flash, redirect, url_for
from datetime import datetime
from ilmo import app, db
from .models import KmpEntry
from .forms import KmpForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/kmp', methods=['GET', 'POST'])
def kmp():
    form = KmpForm()

    starttime = datetime(2015, 2, 26, 12, 00, 00)
    starttime_muut = datetime(2016, 3, 2, 12, 00)
    endtime = datetime(2016, 3, 10, 23, 59, 59)

    OTIT = 25
    SIK = 25

    otit = KmpEntry.query.filter_by(guild='otit').order_by('time').all()
    sik = KmpEntry.query.filter_by(guild='sik').order_by('time').all()
    muu = KmpEntry.query.filter_by(guild='muu').all()

    guilds = [
        {'name': 'OTiT',
        'quota': 25,
        'submissions': otit},
        {'name': 'SIK',
         'quota': 25,
         'submissions': sik},
        {'name': 'Muut',
         'quota': 0,
         'submissions': muu}
    ]
    count = KmpEntry.query.count()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta, {}'.format(form.name.data))
        sub = KmpEntry(
            form.name.data,
            form.email.data,
            form.phone.data,
            form.guild.data,
            form.sitsit.data,
            form.station.data
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
                           nowtime=datetime.now(),
                           starttime_muut=starttime_muut,
                           form=form,
                           otit=otit,
                           sik = sik,
                           muu=muu,
                           count=count,
                           guilds=guilds)