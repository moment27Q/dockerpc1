from flask import Flask, render_template, request, redirect, send_from_directory
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "videos"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        opciones = {
            'outtmpl': f'{DOWNLOAD_FOLDER}/video.%(ext)s', 
            'format': 'best',
            'noplaylist': True
        }

        try:
            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])

            return redirect("/download/video.mp4")

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("index.html")


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)