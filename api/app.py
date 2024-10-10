from flask import Flask, jsonify
from flask import request
import os, sys
from api.util.dnssec_badvalid import secrun, mapcrun
sys.path.append('E:/dpt-tool2/dpt-tool/dpt-tool')
from main import run
import io
f = io.StringIO()

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
        choice = data["choice"]
        value = data["value"]

        # run(choice,value)
        # M.ru
        # n(choice,value)
        # print( f.getvalue())
        return jsonify({'output':run(choice,value)})
    
    @app.route("/api/statr", methods=["POST"])
    def status2():
        data = request.get_json()
        domain = data["domain"]
        ip = data["ip"]
        fakeip = data["fakeip"]
        ttl = data["ttl"]

        # run(choice,value)
        # M.ru
        # n(choice,value)
        # print( f.getvalue())
        return jsonify({'output':secrun(domain,ip,fakeip,ttl)})
    
    @app.route("/api/map", methods=["POST"])
    def status3():
        data = request.get_json()
        ip = data["ip"]
        filepath='E:\\145\\web\\src\\views\\DetailDetect\\Leafletheat服务范围地图页面及数据\\test\\'

        os.startfile(filepath+ip+'.html')
        return 'ok'
    
    @app.route("/api/ma", methods=["POST"])
    def status4():
        data = request.get_json()
        ip = data["ip"]
        # filepath='E:\\145\\web\\src\\views\\DetailDetect\\Leafletheat服务范围地图页面及数据\\test\\'
        str = mapcrun(ip)
        str = str.replace("[None, None],", "")
        print("str")
        with open("E:\\145\\web\\src\\views\\DetailDetect\\Leafletheat服务范围地图页面及数据\\test\\var.js", 'w', encoding='utf-8') as f:
            f.write(str)

        os.startfile("E:\\145\\web\\src\\views\\DetailDetect\\Leafletheat服务范围地图页面及数据\\test\\var"+'.html')
        return 'ok'
        # run(choice,value)
        # M.ru
        # n(choice,value)
        # print( f.getvalue())

    return app

# def config_blueprints(app: Flask):
#     from api.detail.url import detail
 
#     app.register_blueprint(detail)