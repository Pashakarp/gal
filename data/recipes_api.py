from flask import jsonify, Blueprint, request

from data import db_session
from data.models import Recipe


blueprint = Blueprint('recipes_api', __name__, template_folder='templates')


@blueprint.route('/api/recipes')
def get_recipes():
    session = db_session.create_session()
    recipes = session.query(Recipe).all()
    return jsonify(
        {
            'recipes':
                [item.to_dict(only=('title', 'ingredients', 'steps', 'about', 'photo'))
                 for item in recipes]
        }
    )


@blueprint.route('/api/recipe/<int:recipe_id>', methods=['GET'])
def get_one_recipe(recipe_id):
    session = db_session.create_session()
    recipe = session.query(Recipe).get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'recipe': recipe.to_dict(only=('title', 'ingredients', 'steps', 'about', 'photo'))
        }
    )
