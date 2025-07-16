from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import ContatosForm
from app.models import Contato

@app.route('/')
def homepage():
    usuario = 'Franke'
    idade = 24
    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)

@app.route('/contato/', methods=['GET', 'POST'])
def contato_view():
    form = ContatosForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('contato.html', form=form, context=context)

@app.route('/contato/lista/')
def contato_lista():
    pesquisa = request.args.get('pesquisa', '')
    dados = Contato.query.order_by(Contato.nome)
    if pesquisa:
        dados = dados.filter(Contato.nome.contains(pesquisa))
    context = {'dados': dados.all()}
    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>')
def contatoDetail(id):
    obj = Contato.query.get(id)
    return render_template('contato-detail.html', obj=obj)
