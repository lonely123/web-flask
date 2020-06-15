from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)

import uuid
csrf_tokens = dict()

@main.route("/admin")
def index():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens[token] = u.role
    b=Board.all()
    if u.role==1:
        return render_template('board/admin_index.html',b=b,token=token)
    else:
        return redirect(url_for('topic.index'))




@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Board.new(form)
    return redirect(url_for('.index'))


@main.route("/delete")
def delete():
    id = int(request.args.get('id'))
    token = request.args.get('token')
    u = current_user()
    # 判断 token 是否是我们给的
    if token in csrf_tokens and csrf_tokens[token] == 1:
        csrf_tokens.pop(token)
        if u is not None:
            print('删除 board 用户是', u, id)
            Board.delete(id)
            return redirect(url_for('.index'))
        else:
            abort(404)
    else:
        abort(403)