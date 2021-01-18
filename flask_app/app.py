import os
from flask import Flask ,render_template,request
app = Flask(__name__)

@app.route('/')
def app_root():
    return os.environ.get('PATH', 'no app name')

@app.route('/formulaire')
def index():
  print("Merci")
  return render_template("index.html")

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')