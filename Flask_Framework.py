from flask import Flask, request, render_template


app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
@app.route('/<id>')
def index(id):
    # print(id)
    # print(request.args)
    name = request.args.get('name')
    return render_template('index.html', name=name)


# app.run()
