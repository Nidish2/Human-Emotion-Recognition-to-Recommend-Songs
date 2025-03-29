import React from "react";

const SongList: React.FC<{ songs: { name: string; artist: string }[] }> = ({
  songs,
}) => (
  <div>
    <h3>Recommended Songs</h3>
    <ul>
      {songs.map((song, index) => (
        <li key={index}>
          {song.name} by {song.artist}
          {/* Playback link placeholder */}
          <a
            href={`https://www.youtube.com/results?search_query=${song.name}+${song.artist}`}
            target="_blank"
          >
            Play
          </a>
        </li>
      ))}
    </ul>
  </div>
);

export default SongList;
