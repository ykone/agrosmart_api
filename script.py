from flask import Flask,jsonify,request
from PIL import Image
from statistics import mean

app = Flask(__name__) #creating the Flask class object

@app.route('/', methods = ['POST']) #decorator drfines the
def home():
    print('befoore if test')
    if(request.method == 'POST'):
        print('test')
        file = request.files['file']
        im = Image.open(file.stream, 'r')

#         im = Image.open('humus.jpg','r')
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        val=mean(pix_val_flat)
        pixels= [17.3,45,61.6,86.6,126.6]
        l=[0,0,0,0,0]
        aom= [5,3.5,2.5,2,1.5]
        for x in range(5):
            l[x]=abs(pixels[x]-val)
        print(min(l))
        print("Average Oraganic Matter Content is : ", aom[l.index(min(l))])

        return jsonify(aom[l.index(min(l))])
    return 'RAS'

if __name__ =='__main__':
    app.run(host = 'https://app-hackathon-iu-2022.herokuapp.com', debug = True)

#app.run(host, port, debug, options)
#host : The default hostname is 127.0.0.1, i.e. localhost.
#port : The port number to which the server is listening to. The default port number is 5000.
#debug : The default is false. It provides debug information if it is set to true.
#options : It contains the information to be forwarded to the server.
