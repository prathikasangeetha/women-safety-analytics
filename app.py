from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    crime_rate = float(request.form['crime_rate'])
    street_lighting = float(request.form['street_lighting'])
    crowd_density = float(request.form['crowd_density'])
    police_patrol = float(request.form['police_patrol'])
    cctv = float(request.form['cctv'])
    emergency_services = float(request.form['emergency_services'])
    transport = float(request.form['transport'])
    road_condition = float(request.form['road_condition'])
    population_density = float(request.form['population_density'])
    hospitals = float(request.form['hospitals'])
    police_stations = float(request.form['police_stations'])
    complaints = float(request.form['complaints'])
    awareness = float(request.form['awareness'])

    area_type = request.form['area_type']
    time_of_day = request.form['time_of_day']

    score = (
        street_lighting +
        police_patrol +
        cctv +
        emergency_services +
        transport +
        road_condition +
        hospitals +
        police_stations +
        awareness
    ) * 5

    score = score - (crime_rate * 3)
    score = score - (complaints * 2)

    if area_type == "Urban":
        score += 5
    elif area_type == "Semi-Urban":
        score += 3

    if time_of_day == "Night":
        score -= 10
    elif time_of_day == "Evening":
        score -= 5

    if score >= 80:
        prediction = "SAFE AREA"
    elif score >= 50:
        prediction = "MODERATELY SAFE AREA"
    else:
        prediction = "UNSAFE AREA"

    return render_template(
        'index.html',
        prediction=f"{prediction} (Safety Score: {round(score, 2)})"
    )

if __name__ == '__main__':
    app.run(debug=True)