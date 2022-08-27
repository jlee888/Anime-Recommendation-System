from flask import Flask, render_template, request, redirect, url_for, session

from anime import setup, get_recommendation

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        anime_title  = request.form['anime_title']
        print('---------------')
        print(f"Input anime title: {anime_title}")
        print('---------------')

        genres_id, anime_id_at, ultimate_binary_list = setup()
        recommend_list = get_recommendation(anime_title, genres_id, anime_id_at, ultimate_binary_list)
        print('---------------')
        print(f"Recommend list: {recommend_list}")
        print('---------------')
        session.clear()
        session['recommend_list'] = recommend_list

        return redirect(url_for('result', anime_title=anime_title))
        return render_template('result.html', anime_title=anime_title, recommend_list = recommend_list)
        
    return render_template('home.html', title="Home Page")

@app.route('/result/<anime_title>')
def result(anime_title):
    recommend_list =  session['recommend_list']
    return render_template("result.html", title="Result Page", anime_title=anime_title, input=anime_title, recommend_list=recommend_list)


if __name__ == '__main__':

    app.run(port=5001, debug=True)