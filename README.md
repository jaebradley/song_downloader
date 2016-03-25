# Song Downloader
API for downloading songs

### Introduction
Soundcloud is an awesome service. This API is in no way an indictment of the value they provide -- but sometimes, you just want or need to download your favorite songs for offline use.

### API endpoints

#### `/download/soundcloud/`

###### HTTP Methods
* `GET`
 * Query Parameters *(required unless otherwise noted)*
  * `url`: Represents the Soundcloud song url to download
  * `filename`: Output `mp3` filename
 * Example Request: [`https://song-downloader.herokuapp.com/download/soundcloud/?url=https://soundcloud.com/keynotez/white-iverson&filename=white-iverson`](https://song-downloader.herokuapp.com/download/soundcloud/?url=https://soundcloud.com/keynotez/white-iverson&filename=white-iverson)
