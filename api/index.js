const express = require("express");
const fetch = require("node-fetch");
const app = express();

app.get("/api", async (req, res) => {
  const playlistId = req.query.id;
  const apiUrl = `https://api.spotifydown.com/tracks/playlist/${playlistId}`;

  try {
    const response = await fetch(apiUrl, {
      headers: {
        Origin: "https://spotifydown.com",
        Referer: "https://spotifydown.com",
      },
    });
    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).send("Failed to fetch data");
  }
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
