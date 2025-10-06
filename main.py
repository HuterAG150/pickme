from flask import Flask, render_template, request, make_response, redirect, session 
import decouple

app = Flask(__name__)
app.config["SECRET_KEY"] = decouple.config("key")

x = "hello word"

@app.get('/')
def get_index():
    return render_template('index.html')

@app.post('/')
def post_index():
    return x
# settings html (выбор темы мин) сохранить настройки

@app.get('/settings')
def get_settings():
    return render_template('settings.html')

@app.post('/set-theme')
def set_theme():
    theme = request.form.get('theme', 'light')
    response = make_response(redirect('/settings'))
    response.set_cookie('theme', theme, max_age=365*24*60*60)  # Хранить 1 год
    return response

if __name__ == '__main__':
    app.run(debug=True)