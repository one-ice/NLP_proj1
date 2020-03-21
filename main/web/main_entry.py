from flask import Flask, redirect

from web import key_extractor

app = Flask(__name__, instance_relative_config=True, template_folder='static/templates')

app.register_blueprint(key_extractor.bp)


@app.route('/')
def redir_1st_proj():
    return redirect('/key_extractor')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
