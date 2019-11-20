# imports
from flask import Flask, request
from flask import jsonify
from .resnet50 import process_img_path, resnet_model

def create_app():
    app = Flask(__name__)
    

    # ResNet50(weights='imagenet')
    # dummy_url = 'https://wordpress.accuweather.com/wp-content/uploads/2018/05/forest-1.jpg'
    # resnet_model(process_img_path(dummy_url))

    @app.route('/predictor', methods=['POST'])
    def predictor():
        '''a route that expects an image url and id. returns image classifications, probabilities, and id'''
        # get info from backend 
        lines = request.get_json(force=True)
    
        # # get strings from json
        url = lines['url']
        photo_id = lines['photo_id'] 

        # make sure the input's correct
        assert isinstance(url, str)
        assert isinstance(photo_id, int)

        # process image and predict
        predictions = resnet_model(process_img_path(url))

        # format output for json
        # send_back = str(predictions)
        # send_back = str([{'url': url}, {'photo_id': photo_id}])
    
        # send output to backend
        # return app.response_class(
        #     response=json.dumps(send_back),
        #     status=200)
        return jsonify(photo_id=photo_id,
                       predictions=str(predictions))


        # return app.response_class(
        #     response=json.dumps(send_back),
        #     status=200
        # )

    # @app.route('/hello', methods=['POST'])
    # def hello():
    #     send_this = {
    #         'swing': 0.108803526, 
    #         'wig': 0.0843652, 
    #         'neck_brace': 0.08196747
    #         }
    #     return app.response_class(
    #         respose=json.dumps(send_this),
    #         status=200
    #     )
    
    return app
