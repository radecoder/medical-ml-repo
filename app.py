# from flask import Flask, render_template, request, redirect, url_for
# import pickle
# import numpy as np

# app = Flask(__name__)

# # Load the reduced model
# model = pickle.load(open('model_reduced.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predictor')
# def predictor():
#     return render_template('index.html')

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         features = [float(request.form.get(f)) for f in [
#             'radius_mean', 'perimeter_mean', 'area_mean',
#             'concave_points_mean', 'radius_worst',
#             'perimeter_worst', 'area_worst', 'concave_points_worst'
#         ]]
#         input_array = np.array([features])
#         prediction = model.predict(input_array)[0]
#         result = "Cancer Detected 😟" if prediction == 1 else "No Cancer 🎉"
#         return redirect(url_for('result', prediction=result))
#     except Exception as e:
#         return redirect(url_for('result', prediction=f"Error: {str(e)}"))

# @app.route('/result')
# def result():
#     prediction = request.args.get('prediction')
#     return render_template('result.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model_reduced.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')  # Your dynamic landing page

@app.route('/predictor')
def predictor():
    return render_template('index.html')  # Form page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # List of features used during training
        features = [float(request.form.get(f)) for f in [
            'radius_mean', 'perimeter_mean', 'area_mean',
            'concavity_mean', 'concave_points_mean',
            'radius_worst', 'perimeter_worst', 'area_worst',
            'concavity_worst', 'concave_points_worst'
        ]]
        input_array = np.array([features])
        prediction = model.predict(input_array)[0]

        # 1 = Cancer Detected, 0 = No Cancer
        result = "🔴 Malignant (Cancer Detected)😟" if prediction == 1 else "🟢 Benign (No Cancer Detected) 🎉"
        return redirect(url_for('result', prediction=result))

    except Exception as e:
        return redirect(url_for('result', prediction=f"Error: {str(e)}"))

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
