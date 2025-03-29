import React from "react";

const EmotionResult: React.FC<{ emotion: string; confidence: string }> = ({
  emotion,
  confidence,
}) => (
  <div>
    <h2>Detected Emotion: {emotion}</h2>
    <p>Confidence: {confidence}</p>
  </div>
);

export default EmotionResult;
