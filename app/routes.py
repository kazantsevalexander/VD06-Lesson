from flask import Flask, render_template, request, redirect, url_for
from app import app

# Список для хранения данных пользователей
users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Проверка, что все поля заполнены
        if name and city and hobby and age:
            # Добавление данных пользователя в список
            users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))

    # Рендеринг шаблона с переданными данными пользователей
    return render_template('blog.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
