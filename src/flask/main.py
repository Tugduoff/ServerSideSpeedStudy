from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def read_root():
    return jsonify({"message": "Hello World"})

@app.route('/items/<int:item_id>')
def read_item(item_id):
    q = request.args.get('q')
    return jsonify({"item_id": item_id, "q": q})

@app.route('/user/<int:user_id>/workspace/<int:workspace_id>/board/<int:board_id>/list/<int:list_id>/card/<int:card_id>')
def read_card(user_id, workspace_id, board_id, list_id, card_id):
    return jsonify({"user_id": user_id, "workspace_id": workspace_id, "board_id": board_id, "list_id": list_id, "card_id": card_id})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
