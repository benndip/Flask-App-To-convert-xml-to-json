from flask import Flask, render_template, url_for, request, redirect
import json
import xmltodict

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
      if request.method == "POST":
         xmlFile = request.form["uploadedXmlFile"]
         return redirect(url_for("convertToJson",fileToConvert = xmlFile))
      else:
         return render_template("home.html")

@app.route('/converting/<fileToConvert>')
def convertToJson(fileToConvert):
    with open(fileToConvert) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    return data_dict


if __name__ == '__main__':
    app.run()
