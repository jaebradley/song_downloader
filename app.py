from flask import Flask, request, Response
import os

from file_download.downloader import FileDownloader
from soundcloud_api.stream_url_identifier import StreamUrlIdentifier

app = Flask(__name__)
stream_url_identifier = StreamUrlIdentifier()

@app.route('/download/soundcloud/')
def download_soundcloud_song():
    soundcloud_url = request.args.get('url')
    output_filename = request.args.get('filename')
    temp_file = FileDownloader.download_to_temp_file(stream_url_identifier.identify_stream_url(soundcloud_url))
    try:
        resp = Response()
        resp.data = temp_file.read()
        resp.mimetype = "audio/mpeg"
        resp.headers["Content-Disposition"] = "attachment; filename={0}.mp3".format(output_filename)
        return resp
    finally:
        temp_file.close()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)