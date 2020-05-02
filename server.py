from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.wsgi_app = app.wsgi_app
app.config['SECRET_KEY'] = 'hard to guess'
UPLOAD_FOLDER = 'uploads'


@app.route('/upload',methods=['POST'])
def myupload():
    myfile = request.files['file']
    myfile.save(os.path.join(UPLOAD_FOLDER, myfile.filename))

    print('{} received in {}/'.format(myfile.filename,UPLOAD_FOLDER))

    ###### your process
    t = {
        'keywords':{
                    'a':0.9,
                    'b':0.1,
                    },
        'summary':{
                    1:'aaaaaa',
                    2:'bbbbbb',
                    3:'cccccc',
                    },
        }
    ######



    return jsonify(t)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001,threaded=True)
