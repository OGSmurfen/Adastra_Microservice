from flask import Blueprint, jsonify
import psycopg2
import pandas as pd

blueprint = Blueprint('select', __name__, url_prefix='/select')

@blueprint.route("/all", methods=["GET"])
def select_func():
    try:
        conn = psycopg2.connect(
            dbname='cool_db',
            user='cool_user',
            password='1234',
            host='db',
            port=5432
        )

        query = """
            SELECT users.*, cars.model
            FROM users
            LEFT JOIN cars ON users.id = cars.owner_id
        """
        
        df = pd.read_sql(query, conn)
        
        result = df.to_dict(orient='records')

        conn.close()

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})