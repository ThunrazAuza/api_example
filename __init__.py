from flask import Flask, request, render_template 
def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    
    @app.route('/')
    def hello_world():
        return "Bienvenido de vuelta a tu API, Thunraz"
    
    @app.route("/triangulo/<triangulo>")
    def triangulo(triangulo):
        return "Cuando yo la vi: " + triangulo
    
    @app.route("/post/<post_id>", methods = ["GET", "POST"])
    def id_ent(post_id):
        return "El ID del post es: " + post_id
    
    @app.route("/buzon", methods=["POST", "GET"])
    def buzon():
        print(request.form)
        return render_template("/buzon.html")

    return app
