from flask_sqlalchemy import SQLAlchemy
import flask
import random


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

alphabet = [chr(i) for i in range(97, 123)]


class shortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_short = db.Column(db.String(300), nullable=False)
    redirect_url = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<url %r>' % self.id
    

def short() -> str:
    return "".join(random.sample(alphabet, 6))


@app.route('/', methods=['GET', 'POST'])
def main():
    urls = shortener.query.order_by(shortener.url_short).all()
    short_url = flask.request.args.get('s')

    if short_url is not None:
        site = shortener.query.filter_by(
                    url_short=short_url
               ).first()

        if site is not None:
            return flask.redirect(site.redirect_url)

        else:
            return flask.render_template('404.html')

    else:
        if flask.request.method == 'POST':
            url_content = flask.request.form['content']
            while True:
                s = short()
                qeury = shortener.query.filter_by(url_short=s).first()
                if query is None:
                    break
                else:
                    continue

            new_content = shortener(url_short=s, redirect_url=url_content)

            try:
                db.session.add(new_content)
                db.session.commit()
                return flask.redirect('/')
            except Exception as e:
                print(e)

        else:
            return flask.render_template('index.html', urls=urls)

    return flask.render_template('index.html', urls=urls)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
