from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dict = {}
        for column in self.__table__.columns:
            dict[column.name] = getattr(self, column.name)
        return dict


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return jsonify(random_cafe.to_dict())
    # return jsonify(
    #     {
    #         "cafe": {
    #             # "id": random_cafe.id,
    #             "name": random_cafe.name,
    #             "map_url": random_cafe.map_url,
    #             "img_url": random_cafe.img_url,
    #             "location": random_cafe.location,
    #             "amenities": {
    #                 "seats": random_cafe.seats,
    #                 "has_toilet": random_cafe.has_toilet,
    #                 "has_wifi": random_cafe.has_wifi,
    #                 "has_sockets": random_cafe.has_sockets,
    #                 "can_take_calls": random_cafe.can_take_calls,
    #                 "coffee_price": random_cafe.coffee_price,
    #             },
    #         }
    #     }
    # )


@app.route("/all")
def get_all_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafe_list = [cafe.to_dict() for cafe in all_cafes]
    return jsonify({"cafes": cafe_list})


@app.route("/search")
def search_cafe_by_location():
    location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=location).first()
    if cafe != None:
        return jsonify(cafe.to_dict())
    return {"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}
    pass


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    cafe_name = request.args.get("name")
    cafe_map_url = request.args.get("map_url")
    cafe_img_url = request.args.get("img_url")
    cafe_location = request.args.get("location")
    cafe_has_sockets = False
    if request.args.get("has_sockets").lower() == "true":
        cafe_has_sockets = True
    cafe_has_toilet = False
    if request.args.get("has_toilet").lower() == "true":
        cafe_has_toilet = True
    cafe_has_wifi = False
    if request.args.get("has_wifi").lower() == "true":
        cafe_has_wifi = True
    cafe_can_take_calls = False
    if request.args.get("can_take_calls").lower() == "true":
        cafe_can_take_calls = True
    cafe_seats = request.args.get("seats")
    cafe_coffee_price = request.args.get("coffee_price")

    new_cafe = Cafe(
        name=cafe_name,
        map_url=cafe_map_url,
        img_url=cafe_img_url,
        location=cafe_location,
        has_sockets=cafe_has_sockets,
        has_toilet=cafe_has_toilet,
        has_wifi=cafe_has_wifi,
        can_take_calls=cafe_can_take_calls,
        seats=cafe_seats,
        coffee_price=cafe_coffee_price,
    )
    db.session.add(new_cafe)
    db.session.commit()
    return {"response": {"success": "Successfully added the new cafe."}}


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        # db.session.update(cafe, {"coffee_price": request.args.get("new_price")})
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        # return {"success": "Successfully updated the cafe price."}
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # return {"error": {"Not Found": "Sorry, a cafe wit that id was not found in the database."}}
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    print(api_key)
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted the cafe."}), 200
        else:
            return (
                jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}),
                404,
            )
    else:
        return jsonify(error={"Access Denied": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == "__main__":
    app.run(debug=True)
