import React, { useState } from "react";
import axios from "axios";

interface PredictionResponse {
  emotion: string;
  confidence: string;
  songs: { name: string; artist: string }[];
}

const ImageUpload: React.FC<{
  onPredict: (data: PredictionResponse) => void;
}> = ({ onPredict }) => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) setFile(e.target.files[0]);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    try {
      const response = await axios.post("YOUR_NGROK_URL/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      onPredict(response.data);
    } catch (error) {
      console.error("Error predicting emotion:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button type="submit">Analyze Emotion</button>
    </form>
  );
};

export default ImageUpload;
