from flask import Flask, render_template, request, redirect, url_for
def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)

    posts = []
    
    @app.route('/')
    def hello_world():
        return render_template('index.html')
    
    @app.route("/post/<post_id>", methods = ["GET", "POST"])
    def id_ent(post_id):
        return "El ID del post es: " + post_id
    
    @app.route('/buzon', methods=['GET', 'POST'])
    def buzon():
        if request.method == 'POST':
            # Procesa el formulario
            llave = request.form.get('llave')
            valor = request.form.get('valor')
            
            posts.append({'llave': llave, 'valor': valor})
            return redirect(url_for('ver_posts'))

        return render_template('buzon.html')
    
    @app.route('/posts')
    def ver_posts():
        # Renderizar una plantilla que muestre las entradas
        return render_template('posts.html', posts=posts)

    return app
