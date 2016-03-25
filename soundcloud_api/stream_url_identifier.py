import soundcloud


class StreamUrlIdentifier:
    def __init__(self):
        self.client_id = "b1d03f48fd6e888acf06410ddb7f035d"
        self.client = soundcloud.Client(client_id=self.client_id)

    def identify_stream_url(self, url):
        resolved_track = self.client.get('/resolve', url=url)
        if 'stream_url' in resolved_track.obj:
            return self.client.get(resolved_track.obj['stream_url'], allow_redirects=False).location