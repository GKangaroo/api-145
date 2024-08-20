from flask import Flask
from flask import request
def create_app() -> Flask:
    app = Flask(__name__)
    app.app_context().push()
    # config_blueprints(app)
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

    @app.route("/api/start", methods=["POST"])
    def status1():
        data = request.get_json()
        print(data)
    return app

# def config_blueprints(app: Flask):
#     from api.detail.url import detail
 
#     app.register_blueprint(detail)