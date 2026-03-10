from flask import Flask, render_template, request

app = Flask(__name__)

tips = {
    "Tomato": [
        "Sunlight: Needs 6-8 hours of sunlight daily.",
        "Watering: Water every 2-3 days.",
        "Soil: Well-drained fertile soil.",
        "Fertilizer: Use compost or organic fertilizer.",
        "Harvest: Ready in 60-80 days."
    ],

    "Mint": [
        "Sunlight: Partial sunlight.",
        "Watering: Keep soil moist.",
        "Soil: Rich and moist soil.",
        "Fertilizer: Use organic compost.",
        "Harvest: Ready in 30-40 days."
    ],

    "Chili": [
        "Sunlight: Needs full sunlight.",
        "Watering: Water regularly.",
        "Soil: Well-drained soil.",
        "Fertilizer: Nitrogen-rich fertilizer.",
        "Harvest: Ready in 70-90 days."
    ],

    "Coriander": [
        "Sunlight: Moderate sunlight.",
        "Watering: Light watering daily.",
        "Soil: Loose soil.",
        "Fertilizer: Organic compost recommended.",
        "Harvest: Ready in 30-40 days."
    ],

    "Spinach": [
        "Sunlight: Partial sunlight.",
        "Watering: Keep soil moist.",
        "Soil: Rich organic soil.",
        "Fertilizer: Nitrogen fertilizer recommended.",
        "Harvest: Ready in 40-50 days."
    ]
}

wiki_links = {
    "Tomato": "https://en.wikipedia.org/wiki/Tomato",
    "Mint": "https://en.wikipedia.org/wiki/Mint",
    "Chili": "https://en.wikipedia.org/wiki/Chili_pepper",
    "Coriander": "https://en.wikipedia.org/wiki/Coriander",
    "Spinach": "https://en.wikipedia.org/wiki/Spinach"
}


@app.route("/", methods=["GET", "POST"])
def home():

    plant = None
    tip = None
    index = 0
    end = False
    wiki = None

    if request.method == "POST":

        plant = request.form["plant"]
        index = int(request.form.get("index", 0))

        plant_tips = tips.get(plant, [])

        if index < len(plant_tips):
            tip = plant_tips[index]
        else:
            end = True

        wiki = wiki_links.get(plant)

        index += 1

    return render_template("index.html",
                           plant=plant,
                           tip=tip,
                           index=index,
                           end=end,
                           wiki=wiki)


if __name__ == "__main__":
    app.run(debug=True)