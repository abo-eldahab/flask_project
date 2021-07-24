from flask import Flask, make_response , render_template, request
# from flask import url_for
from flask_sqlalchemy import SQLAchemy

# import xmlrpc.client
#
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'


# def _login(url, db, username, password):
#     common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#     uid = common.authenticate(db, username, password, {})
#     return uid
#
#
# def _get_objects(url):
#     return xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#
#
# def _check_access_right(models, db, uid, password, object, list_access):
#     if isinstance(list_access, list) and isinstance(object, str):
#         for access in list_access:
#             ret = models.execute_kw(db, uid, password,
#                                     object, 'check_access_rights',
#                                     [access], {'raise_exception': False})
#             if not ret:
#                 return ret
#         return True
#     return False
#
#
# def _get_identifiers_object(models, db, uid, password, object, list_conditions=[], offest=0, limit=0):
#     if isinstance(list_conditions, list) and isinstance(object, str):
#         return models.execute_kw(db, uid, password,
#                                  object, 'search',
#                                  [list_conditions],
#                                  {'offset': offest, 'limit': limit})
#     return []
#
#
# def _get_objects_by_identifiers(models, db, uid, password, object, ids, list_fields=[]):
#     if isinstance(object, str):
#         result = models.execute_kw(db, uid, password, object, 'read', [ids], {'fields': list_fields})
#         return result
#     return []
#
#
# def _get_objects_with_fields(models, db, uid, password, object, list_conditions=[], list_fields=[], limit=0):
#     if isinstance(object, str):
#         return models.execute_kw(db, uid, password,
#                                  object, 'search_read',
#                                  [list_conditions],
#                                  {'fields': list_fields, 'limit': limit})
#     return []
#
#
# def _create_object(models, db, uid, password, object, list_fields):
#     if isinstance(object, str):
#         id = models.execute_kw(db, uid, password, object, 'create', list_fields)
#     return id
#
#
# def _update_objects(models, db, uid, password, object, ids, new_dic_fields):
#     if isinstance(object, str):
#         models.execute_kw(db, uid, password, object, 'write', [ids, new_dic_fields])
#
#
# def _delete_objects(models, db, uid, password, object, ids):
#     if isinstance(object, str):
#         models.execute_kw(db, uid, password, object, 'unlink', [ids])
#
# def _get_parameter():
#     url = 'http://127.0.0.135:8135'
#     db = 'brimore13'
#     username = 'admin'
#     password = 'admin'
#
#     return url,db,username,password
#
# @app.route('/')
# def index():
#
#     url, db, username, password = _get_parameter()
#
#     uid = _login(url, db, username, password)
#
#     models = _get_objects(url)
#
#     return str(url)  + ' ' + str(db) + ' ' + str(username)  + ' ' + str(password)
#
#
if __name__ == '__main__':
    app.run()