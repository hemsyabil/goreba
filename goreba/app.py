from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cleaning')
def cleaning():
    return render_template('services/cleaning/index.html')


@app.route('/rennovation')
def woodworking():
    return render_template('services/rennovation/index.html')


@app.route('/portfolio')
def portfolio_management():
    return render_template('services/portfolio/index.html')


@app.route('/software')
def software_solution():
    return render_template('services/software/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
