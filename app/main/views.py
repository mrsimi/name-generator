from flask import render_template, request, url_for
from app.main import bp
from app.main.forms import GenerateForm
from app.utils.generator import GenerateNames

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = GenerateForm()
    if request.method == 'GET':
        return render_template('main/index.html', app_concept="", form=form, app_concept_to_list='')
    else:
        if form.validate_on_submit():
            resp_names = GenerateNames(form.app_concept.data)
            
            return render_template('main/index.html', app_concept=form.app_concept.data, form=form,
                                app_concept_to_list= resp_names.run_algo(10))
    
    return render_template('main/index.html', app_concept="", form=form, app_concept_to_list='')

# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     form = GenerateForm()
#     if form.validate_on_submit():
#         resp_names = GenerateNames(form.app_concept.data)
#     return render_template('main/index.html', app_concept=form.app_concept.data, form=form,
#                                 app_concept_to_list= resp_names.split_to_list())