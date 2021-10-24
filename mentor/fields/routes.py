from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from mentor import db
from mentor.models import Work
from mentor.fields.forms import EntireJobForm

fields = Blueprint('fields', __name__)


@fields.route("/job/details", methods=['GET', 'POST'])
@login_required
def job_details(work_id):
    job = Work.query.get_or_404(work_id)

    return render_template('work.html',title= 'Job info'+ job.jobtitle, job=job)


