import React from "react";

const OutputSection = ({ result, loading }) => {
  if (loading) return <p className="text-center text-lg">Processing...</p>;
  if (!result) return null;

  if (result.error)
    return <p className="text-red-500 text-center">{result.error}</p>;

  return (
    <div className="bg-white rounded-md shadow p-6 space-y-6">
      <div>
        <h2 className="text-xl font-bold text-gray-800 mb-2">📝 Summary</h2>
        <p className="text-gray-700">{result.summary}</p>
      </div>

      <div>
        <h2 className="text-xl font-bold text-gray-800 mb-2">📌 Keywords</h2>
        <ul className="list-disc list-inside text-gray-700">
          {result.keywords?.map((kw, idx) => (
            <li key={idx}>{kw}</li>
          ))}
        </ul>
      </div>

      <div>
        <h2 className="text-xl font-bold text-gray-800 mb-2">❓ MCQs</h2>
        <ul className="space-y-4">
          {result.mcqs?.map((mcq, i) => (
            <li key={i}>
              <p className="font-semibold">{i + 1}. {mcq.question}</p>
              <ul className="pl-5 list-disc text-gray-700">
                {mcq.options.map((opt, j) => (
                  <li key={j}>{opt}</li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default OutputSection;
