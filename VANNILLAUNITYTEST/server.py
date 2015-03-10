from flask import Flask, jsonify, send_file, request
import os
import mk_json


app = Flask(__name__)

def retr(thingy):
    return request.args.get(thingy, '')


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/data/<path:blah>', methods=['GET'])
def send_foo(blah = ""):
    blah = "/" + blah
    print retr("key")
    if(request.args.get("doSend", '')):
        if(request.args.get("doSend", '').lower()[0] == "y"):
            ray1=int(request.args.get("firstray", ''))
	    ray2=int(request.args.get("lastray", ''))
	    sample1=int(retr("firstsample"))
	    sample2=int(retr("lastsample"))
	    theNames=retr("names").split()
	    print theNames
            return jsonify(mk_json.convert(theFile=blah, first_ray=ray1, last_ray=ray2, first_sample=sample1, last_sample=sample2, names=theNames))

    if(retr("meta")):
        if(retr("meta").lower()[0] == "y"):
            variables = mk_json.getMeta(blah)
            return jsonify({"Vars" : variables})
	       
    if os.path.isfile(blah):
        stuff = os.listdir(os.path.dirname(blah))
    else:
        stuff = os.listdir((blah))
    stuff.append("..")
    stuff.sort()


    return jsonify({"Files" : stuff})

if __name__ == '__main__':
    app.debug = True;
    app.run()
