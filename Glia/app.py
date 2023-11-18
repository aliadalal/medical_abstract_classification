from flask import Flask, render_template, request
from text_classification_model import classify_text  # Function to classify text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        text = request.form['text']
        modelID=request.form['models']
        print("@@@@@@" , modelID, "@@@@@@\n")
        # Classify text using the model
        classification,conditionL = classify_text(text,modelID)
        return render_template('result.html', text=text, classification=classification,conditionL=conditionL)

if __name__ == '__main__':
    app.run(debug=True)
