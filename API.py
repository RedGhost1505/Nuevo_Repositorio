from flask import Flask, render_template, jsonify, abort, request

app=Flask(__name__)

uri='/api/'
persona={'name':'Alex', 'matricula':'1234'}

tasks=[{
        'id':1, 
        'name':'cocinar algo bien sabroso', 
        'status': False
        }, 
        {'id':2, 
         'name':'limpiar la casa', 
         'status': False
         }, 
]


@app.route("/")
def hello_world():
    return render_template("index.html", data=persona)

#API


@app.route(uri, methods=['GET'])
def getTasks():
    return jsonify({'tasks':tasks})

@app.route(uri+'/<int:id>', methods=['GET'])
def get_task(id):
    this_task=0
    for task in tasks:
        if task['id']==id:
            this_task=task
    if this_task==0:
        abort(404)
    return jsonify({'task':this_task})

@app.route(uri, methods =['POST'])
def create_task():
    if request.json:
        task = {
            'id': len(tasks)+1,
            'name': request.json['name'],
            'status': False 
        }
        tasks.append(task)
        return jsonify({'tasks':tasks}), 201
    else:
        abort(404)

@app.route(uri+'/<int:id>', methods= ['PUT'])
def update_task(id):
    if request.json:
        this_task




if __name__=='__main__':
    app.run(debug=True)

