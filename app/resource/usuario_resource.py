from flask import Blueprint, request, jsonify
from app.mapping.usuario_schema import UsuarioSchema
from app.service.usuario_service import UsuarioService
from app.service.response_message import ResponseBuilder
from app.mapping.response_schema import ResponseSchema
from app.mapping.usuario_schema import UsuarioSchema

# Definimos el Blueprint
user_bp = Blueprint('usuarios', __name__, url_prefix="/usuarios")

# Instancias de schemas y service
usuario_service = UsuarioService()
response_schema = ResponseSchema()
usuario_schema = UsuarioSchema()


@user_bp.route('', methods=['POST'])
def post():
    """
    POST /CREAR NUEVO USUARIO
    """
    try:
        # 1. Obtener JSON del request
        data = request.get_json()

        # 2. Pasar al service para validación y guardado
        usuario = usuario_service.crear_usuario(data)

        # 3. Devolver respuesta formateada
        return jsonify(response_schema.dump({
            "status": "success",
            "data": usuario_schema.dump(usuario),
            "message": "Usuario creado correctamente"
        })), 201

    except Exception as e:
        return jsonify(response_schema.dump({
            "status": "error",
            "data": None,
            "message": str(e)
        })), 400

@user_bp.route('', methods=['GET'])
def list_users():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    users = usuario_service.lista_usuario(page=page, per_page=per_page)
    return jsonify({
        "users": [u.to_dict() for u in users.items],
        "total": users.total,
        "pages": users.pages,
        "current_page": users.page
    })


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    builder = ResponseBuilder()
    user = usuario_service.obtener_usuario_id(user_id)
    if not user:
        builder.add_message("Usuario no encontrado").add_status_code(404)
        return response_schema.dump(builder.build()), 404

    data = usuario_schema.dump(user)
    builder.add_message("Usuario encontrado").add_status_code(200).add_data(data)
    return response_schema.dump(builder.build()), 200

@user_bp.route('/<string:usuario>', methods=['GET'])
def get_by_username(usuario):
    builder = ResponseBuilder()
    usuario = usuario_service.obtener_usuario(usuario)
    if not usuario:
        builder.add_message("Usuario no encontrado").add_status_code(404)
        return response_schema.dump(builder.build()), 404

    data = usuario_schema.dump(usuario)
    builder.add_message("Usuario encontrado").add_status_code(200).add_data(data)
    return response_schema.dump(builder.build()), 200


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    builder = ResponseBuilder()
    success = usuario_service.borra_usuario(user_id)
    if not success:
        builder.add_message("Usuario no encontrado").add_status_code(404)
        return response_schema.dump(builder.build()), 404

    builder.add_message("Usuario eliminado").add_status_code(204)
    # 204 No Content típicamente no retorna body, pero Marshmallow lo incluirá vacío.
    return response_schema.dump(builder.build()), 204





