from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images')
def get_image():
    image_name = request.args.get('image_name')
    print(image_name+".jpeg")
    extracted_image = image_name+".jpeg"

    # Check for empty strings or string with only spaces
    #if not bool(image_name.strip()):
        # You could render "image Not Found" instead like we do below
    #    image_name = "banana"

    # image is not found by API
    #if not image_data['cod'] == 200:
    #    return render_template('image-not-found.html')

    return render_template('image.html')
#, img=extracted_image)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=2008)
