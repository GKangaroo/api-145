from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.app_context().push()
    config_blueprints(app)
    # deploy_mode = os.environ.get(DEPLOY_MODE)
    # if deploy_mode == "PROD":
    #     app.config.from_object(config.ProductionConfig)
    # else:
    #     klass_name = "%sConfig" % deploy_mode
    #     conf_klass = getattr(config, klass_name, config.DevelopmentConfig)
    #     app.config.from_object(conf_klass)
    # config_log(app)
    # config_database(app)
    # config_cache(app)
    # config_hooks(app)
    
    # config_attr(app)
    # config_jwt(app)

    @app.route("/api/status")
    def status():
        return "ok"

    return app

def config_blueprints(app: Flask):
    # from libra.auth import auth
    # from libra.dag import dag
    # from libra.filter_condition import filter_cond
    # from libra.history import history
    # from libra.info import info
    # from libra.record import record
    # from libra.rule import rule
    # from libra.shares import shares

    # app.register_blueprint(dag)
    # app.register_blueprint(record)