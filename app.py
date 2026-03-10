from flask import Flask, render_template, request

app = Flask(__name__)

# Plant tips database
tips = {
    "Tomato": "Water every 2-3 days. Needs full sunlight. Use compost fertilizer.",
    "Mint": "Keep soil moist. Needs partial sunlight. Harvest after 30-40 days.",
    "Chili": "Requires warm weather. Water regularly and use organic fertilizer.",
    "Coriander": "Needs moderate sunlight. Water lightly every day.",
    "Spinach": "Grow in cool weather. Water regularly and use organic compost."
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    
    if request.method == "POST":
        plant = request.form["plant"]
        result = tips.get(plant, "No tips available")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)