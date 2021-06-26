from flask import Flask,render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    intro = db.Column(db.String(300), nullable=False, )
    text = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return '<Name %r>' % self.name



@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    articles = Articles.query.order_by(Articles.date.desc()).all() #от новых постов к старым!!!!!
    return render_template('posts.html' , articles=articles)

@app.route('/posts/<int:id>')
def posts_detail(id):
    article = Articles.query.get(id) #от новых постов к старым!!!!!
    return render_template('post_detail.html' , article=article)

@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Articles(title=title,intro=intro,text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При добавлении статьи произошла ошибка'     
    else:
        return render_template('create-article.html')



if __name__ == '__main__':
    app.run(debug=True)
