import os

from flask import Flask
from flask_cors import cross_origin

from JEAPIs.APIBlueprints.Test.Test import Test

app = Flask(__name__)


class RestfulAPIHandler:
    app.secret_key = os.urandom(16)
    app.register_blueprint(Test)
    '''
    全部資料：GET + 名稱
    特定資料：GET + 名稱 + id
    新增一筆資料：POST + 名稱
    修改特定資料：PUT + 名稱 + id
    刪除特定資料：DELETE + 名稱 + id
    '''

    # 捕抓例外路徑
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(self, path):
        return f'Path : {path} not exist'

    @app.route(r'/')
    @cross_origin()
    def main_page(self):
        return 'Success'


if __name__ == "__main__":
    RestfulAPIHandler = RestfulAPIHandler()
    app.debug = True
    app.run()
