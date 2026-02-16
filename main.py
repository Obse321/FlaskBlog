from flask import Flask, render_template, request, url_for, flash, redirect
import datetime,time
from models import Models


app=Flask(__name__)
# Конфигурация приложения
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['JSON_AS_ASCII'] = False    # Для поддержки русских символов в JSON

classModels=Models()

@app.get("/")
@app.get('/index')
def main_blog():
    #classModels.create_post("Post1", "qwe", "me", date=str(datetime.datetime.now()))
    #classModels.create_post( "Post2", "qwe", "me", date=str(datetime.datetime.now()))

    posts=classModels.load_post()

    return render_template("index.html",posts=posts)

@app.get('/about')
def about():
    return render_template("about.html")


@app.get("/post/<int:id>")
def show_post(id):
    post=classModels.load_post()[id-1]
    return render_template("post.html",post=post)

@app.route("/create_post",methods=["GET", "POST"])
def create_post():
    if request.method=="POST":
        #данные с формы
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        if not title or not content or not author:
            flash('Все поля обязательны для заполнения!', 'error')
            return render_template('create_post.html')


        flash('Пост успешно создан!', 'success')
        classModels.create_post( title, content, author, date=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))

        return redirect(url_for('main_blog'))

    return render_template("create.html")


if __name__=="__main__":
    app.run(debug=True)