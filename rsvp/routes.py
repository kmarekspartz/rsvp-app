from flask import request, flash, render_template, redirect
from rsvp import app, Session
from rsvp.models import RSVPForm, RSVP


@app.route('/', methods=['GET', 'POST'])
def rsvp_view():
    form = RSVPForm(request.form)
    if request.method == 'POST' and form.validate():
        session = Session()
        rsvp = RSVP()
        form.populate_obj(rsvp)
        session.add(rsvp)
        flash('Thanks for the RSVP')
        return redirect('/')
    return render_template('rsvp.html', form=form)
