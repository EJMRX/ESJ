from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-super-secret-key-that-no-one-can-guess'

    # Register all blueprints
    from .website import routes as website_routes
    app.register_blueprint(website_routes.bp)

    from .bureau import routes as bureau_routes
    app.register_blueprint(bureau_routes.bp)

    from .catalogue import routes as catalogue_routes
    app.register_blueprint(catalogue_routes.bp)

    from .achats import routes as achats_routes
    app.register_blueprint(achats_routes.bp)

    from .ventes import routes as ventes_routes
    app.register_blueprint(ventes_routes.bp)

    from .stocks import routes as stocks_routes
    app.register_blueprint(stocks_routes.bp)

    from .annuaire import routes as annuaire_routes
    app.register_blueprint(annuaire_routes.bp)

    from .comptabilite import routes as comptabilite_routes
    app.register_blueprint(comptabilite_routes.bp)

    from .commande import routes as commande_routes
    app.register_blueprint(commande_routes.bp)

    from .options import routes as options_routes
    app.register_blueprint(options_routes.bp)

    return app