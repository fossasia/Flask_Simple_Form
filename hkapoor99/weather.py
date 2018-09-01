from flask import request, Flask , render_template
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		location = request.form.get('addloc')
		URL1 = "https://maps.googleapis.com/maps/api/geocode/json"
		PARAMS1 = {'address':location}
		r1 = requests.get(url=URL1, params=PARAMS1)
		data1 = r1.json()
		if data1['status']=='ZERO_RESULTS' or data1['status']=='OVER_QUERY_LIMIT':
			ans = 'No Results Found!'
		else:
			latitude = int(data1['results'][0]['geometry']['location']['lat'])
			longitude = int(data1['results'][0]['geometry']['location']['lng'])

			PARAM2 = {'lat':latitude, 'lon':longitude, 'APPID':[Enter APP ID Here]}


			URL2 = "http://api.openweathermap.org/data/2.5/weather"

			r2 = requests.get(url = URL2, params=PARAM2);

			data2 = r2.json()

			temp = data2['main']['temp']

			ans = int(temp-273)
		
		return render_template("index.html", answer=ans)

if __name__ == "__main__":
	app.run(port=8000, debug=True, use_reloader=True)
	
