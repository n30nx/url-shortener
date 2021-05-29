from flask_sqlalchemy import SQLAlchemy 
import flask
import random

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

f = ""

class shortener(db.Model):


    id = db.Column(db.Integer, primary_key = True)
    url_short = db.Column(db.String(300), nullable = False)
    redirect_url = db.Column(db.String(300), nullable = False)


    def __repr__(self):

        return '<url %r>' % self.id

def short():

    global f

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

    while len(f) < 6:
        v = random.randint(0, 100)
        if v > 50:
            f += alphabet[random.randint(0, len(alphabet) - 1)]
        else:
            f += str(random.randint(0,9))

    return f

@app.route('/', methods = ['GET', 'POST'])
def main():

    urls = shortener.query.order_by(shortener.url_short).all()
    l = flask.request.args.get('s')
    

    if l != None:
        try:
            site = shortener.query.filter_by(url_short=str(l)).first()
            return flask.redirect(site.redirect_url)

        except:
            return flask.render_template('index.html', urls=urls)


    else:

        if flask.request.method == 'POST':
            url_content = flask.request.form['content']
            while 1:
                s = short()
                x = shortener.query.filter_by(url_short=s).first()
                if x == None:
                    break
                else:
                    continue



            new_content = shortener(url_short = s , redirect_url = url_content)

            try:
                db.session.add(new_content)
                db.session.commit()
                return flask.redirect('/')
            except Exception as e:
                print(e)
            
        else:
            try:
                return flask.render_template('index.html', urls=urls)
            except Exception as e:
                print(e)
                
    
    
    return flask.render_template('index.html', urls=urls)


if __name__ == "__main__":

    app.run(debug = True, port = 5000)
