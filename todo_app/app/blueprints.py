from flask import Blueprint

# Create blueprint
tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def list_tasks():
    # Your code here
    pass