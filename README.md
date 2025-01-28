# Spotify Scraper API

A Python-based API that scrapes data from Spotifydown.com to retrieve track information and playlist details. This service is deployed on Vercel and provides endpoints to fetch Spotify track listings and playlist information.

## 🌟 Features

- **Track List Fetching**: Get detailed track information from Spotify playlists
- **Playlist Information**: Retrieve playlist metadata including title, cover, and creator
- **JSON Response Format**: Clean, well-structured data output
- **Serverless Architecture**: Deployed on Vercel for reliability and scalability
- **Caching Support**: Implements caching for improved performance

## 📚 API Documentation

### Base URL
```
https://sp-sigma.vercel.app
```

### Endpoints

#### 1. Get Playlist Tracks
```http
GET /api/spotify?id={playlist_id}
```

##### Parameters
| Parameter | Type   | Required | Description              |
|-----------|--------|----------|--------------------------|
| id        | string | Yes      | Spotify playlist ID      |

##### Example Request
```http
GET https://sp-sigma.vercel.app/api/spotify?id=37i9dQZF1DXbQDZkQM83q7
```

##### Response Format
```json
{
  "nextOffset": null,
  "statusCode": 200,
  "success": true,
  "trackList": [
    {
      "album": "Album Name",
      "artists": "Artist Names",
      "cover": "Cover URL",
      "id": "Track ID",
      "releaseDate": "YYYY-MM-DD",
      "title": "Track Title"
    }
  ]
}
```

#### 2. Get Playlist Information
```http
GET /api/spotifyPlaylist?id={playlist_id}
```

##### Parameters
| Parameter | Type   | Required | Description              |
|-----------|--------|----------|--------------------------|
| id        | string | Yes      | Spotify playlist ID      |

##### Example Request
```http
GET https://sp-sigma.vercel.app/api/spotifyPlaylist?id=37i9dQZF1DXbQDZkQM83q7
```

##### Response Format
```json
{
  "artists": "Playlist Creator",
  "cache": true,
  "cover": "Playlist Cover URL",
  "releaseDate": null,
  "statusCode": 200,
  "success": true,
  "title": "Playlist Title"
}
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Node.js and npm (for Vercel CLI)

### Local Development

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd spotify-scraper
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Development Server**
   ```bash
   vercel dev
   ```

## 📦 Deployment

### Deploying to Vercel

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Configure Vercel Project**
   ```bash
   vercel login
   vercel link
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

## ⚡ Response Details

### Track List Response Fields
- `title`: Track name
- `artists`: Artist names (comma-separated)
- `album`: Album name
- `cover`: Album cover URL
- `id`: Spotify track ID
- `releaseDate`: Track release date

### Playlist Response Fields
- `title`: Playlist name
- `artists`: Playlist creator
- `cover`: Playlist cover image URL
- `cache`: Cache status
- `success`: Request status
- `statusCode`: HTTP status code

## 🛠️ Error Handling

| Status Code | Description                                    |
|-------------|------------------------------------------------|
| 200         | Successful request                             |
| 400         | Bad request (invalid playlist ID)              |
| 404         | Playlist not found                            |
| 500         | Internal server error                         |

Error Response Format:
```json
{
    "success": false,
    "statusCode": 400,
    "error": "Error message"
}
```

## ⚠️ Rate Limiting

To prevent abuse, please implement reasonable rate limiting in your applications:
- Maximum of 100 requests per minute per IP
- Maximum of 1000 requests per hour per IP



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is not affiliated with, endorsed by, or sponsored by Spotify or Spotifydown.com. Use this API responsibly and ensure compliance with Spotify's Terms of Service.

## 📮 Support

For issues, feature requests, or questions:
- Open an issue in the GitHub repository
  

---

Made with ❤️ 
