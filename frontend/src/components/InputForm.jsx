import React, { useState } from "react";

const InputForm = ({ setResult, setLoading }) => {
  const [text, setText] = useState("");

  const mockResponse = {
    summary: "This article discusses the importance of clean energy in modern society, highlighting solar and wind as key alternatives to fossil fuels.",
    keywords: ["clean energy", "solar power", "wind energy", "fossil fuels"],
    mcqs: [
      {
        question: "What is one of the clean energy alternatives mentioned in the article?",
        options: ["Coal", "Natural Gas", "Solar Power", "Diesel"],
        answer: "Solar Power",
      },
      {
        question: "Why is clean energy important?",
        options: [
          "It is cheaper than all energy sources",
          "It reduces pollution",
          "It increases fossil fuel usage",
          "It causes global warming",
        ],
        answer: "It reduces pollution",
      },
    ],
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;
  
    setLoading(true);
    
    try {
      const response = await fetch('http://localhost:5000/process-text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      console.log(response);
      const data = await response.json();
  
      if (!response.ok) {
        throw new Error(data.error || "Something went wrong");
      }
  
      setResult(data);
    } catch (error) {
      setResult({ error: error.message });
    } finally {
      setLoading(false);
    }
  };
  

  return (
    <form onSubmit={handleSubmit} className="space-y-6 mb-10">
      <textarea
        className="w-full p-4 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 min-h-[200px]"
        placeholder="Paste your article here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button
        type="submit"
        className="bg-indigo-600 text-white px-6 py-3 rounded-md hover:bg-indigo-700 transition-all duration-200"
      >
        Generate Summary & MCQs
      </button>
    </form>
  );
};

export default InputForm;
