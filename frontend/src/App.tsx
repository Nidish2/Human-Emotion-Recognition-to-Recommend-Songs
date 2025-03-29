import React, { useState } from "react";
import { SignedIn, SignedOut } from "@clerk/clerk-react";
import ImageUpload from "./components/ImageUpload";
import EmotionResult from "./components/EmotionResult";
import SongList from "./components/SongList";
import Auth from "./components/Auth/Auth";

const App: React.FC = () => {
  const [result, setResult] = useState<{
    emotion: string;
    confidence: string;
    songs: { name: string; artist: string }[];
  } | null>(null);

  const handlePredict = (data: {
    emotion: string;
    confidence: string;
    songs: { name: string; artist: string }[];
  }) => setResult(data);

  return (
    <div>
      <Auth />
      <SignedIn>
        <h1>Emotion-Based Song Recommender</h1>
        <ImageUpload onPredict={handlePredict} />
        {result && (
          <>
            <EmotionResult
              emotion={result.emotion}
              confidence={result.confidence}
            />
            <SongList songs={result.songs} />
          </>
        )}
      </SignedIn>
      <SignedOut>
        <p>Please sign in to use the app.</p>
      </SignedOut>
    </div>
  );
};

export default App;
