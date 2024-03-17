from flask import Flask , render_template, request , send_file ,jsonify , send_from_directory
import os 
import time 

app = Flask("__main__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload_script", methods = ['GET' , 'POST'])
def upload():
    # data = request.json
    # file_type =  data.get("file_type")
    file = request.files.get("script")
    filename = f"script_{len(os.listdir('temp_files')) + 1}.pdf"
    file.save(filename) 

    # code for converting script to storyboard

    output_file_name = "storyboard.pdf"
    time.sleep(5)
    
    # return render_template("output.html" , file = output_file_name)
    return ( jsonify({"filename": output_file_name.replace(".pdf", "")}), 200 )

@app.route("/output/<filename>")
def output(filename):
    return render_template("/output.html", filename = filename)

@app.route("/story_board/<story_board>")
def storyboard(story_board):
    return send_file(f"output_scripts\\{story_board}.pdf" , as_attachment=True)

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    print(filename)
    return send_from_directory('static', f'{filename}.pdf')

if __name__ == "__main__":
    app.run( port = 8000)