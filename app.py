from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/spotify', methods=['GET'])
def get_spotify_playlist():
    playlist_id = request.args.get('id')
    if not playlist_id:
        return jsonify({"error": "Playlist ID is required"}), 400

    api_url = f"https://api.spotifydown.com/tracks/playlist/{playlist_id}"

    try:
        # Send the request to the SpotifyDown API with headers
        headers = {
            "Origin": "https://spotifydown.com",
            "Referer": "https://spotifydown.com",
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Return the data from the API
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
