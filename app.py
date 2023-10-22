from flask import Flask,render_template , request,json
import requests
app = Flask(__name__)

@app.route('/')
def load_html():
    return render_template("index.html")

@app.route('/review',methods=['POST'])
def post_data():
    city=request.form.get('city')
    mertrics=request.form.get('units')
    appid=request.form.get('appid')
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q' :city,
          'appid' :'b2f7276693524dc1283929277faa0eae' ,
          'units':mertrics}
    data = requests.get(url,params=params)
    response = data.json()
    return f"data {response}"


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)
   
