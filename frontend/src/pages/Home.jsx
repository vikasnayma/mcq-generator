import React, { useState } from "react";
import InputForm from "../components/InputForm";
import OutputSection from "../components/OutputSection";

function Home() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-gray-50 px-6 py-10 md:px-24">
      <h1 className="text-3xl md:text-4xl font-bold text-center mb-2 font-serif text-indigo-600">
        🧠 QuickLearn
      </h1>
      <p className="text-2xl md:text-2xl text-center pt-0.1 mb-10 text-indigo-300">
         Text Summarization & MCQ Generator
      </p>
      <InputForm setResult={setResult} setLoading={setLoading} />
      <OutputSection result={result} loading={loading} />
    </div>
  );
}

export default Home;


