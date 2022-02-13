from  flask import Flask, render_template

app=Flask(__name__)


@app.route("/expressions/")
def hello_world():

    #interpolation
    color = "brown"
    animal_one = "fox"
    animal_two ="dog"

    #addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    #string concatention
    first_name = "Caption"
    last_name = "Marvel"

    kwargs = {
        "color":color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount" : donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template(
        "expressions.html", **kwargs
        )

@app.route("/data-structures/")
def render_data_structures():
    movies =[
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand" : "tesla",
        "model" : "model S",
        "year" : "2020"
    }

    return render_template("data_sturcture.html", movies=movies, car=car)

    

app.run(host="127.0.0.1", port=5555, debug=True)
