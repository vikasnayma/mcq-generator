import os
from inference import summarize_and_extract
from mcq import generate_mcqs  # 🆕 import your generator

texts = [
    """
    The global shift towards electric vehicles (EVs) is accelerating as governments push for cleaner transportation. 
    Major car manufacturers are investing billions into EV development, with new models offering improved battery life 
    and faster charging times. However, challenges remain, including the need for widespread charging infrastructure 
    and sustainable battery production. Experts argue that innovations in battery recycling and renewable energy 
    integration are essential to making EVs truly eco-friendly. Despite these challenges, consumer interest continues 
    to grow, with EV sales hitting record highs in multiple countries. As technology advances and costs decrease, 
    electric vehicles are expected to become the dominant mode of transportation in the near future.
    """,
    """
    Climate change is one of the most pressing issues facing the world today. Rising global temperatures, melting polar ice caps, 
    and unpredictable weather patterns are some of its visible effects. Human activities, such as burning fossil fuels and deforestation, 
    contribute significantly to this crisis. Governments and organizations worldwide are urging for renewable energy adoption and 
    sustainable practices to mitigate the impact of climate change. The future of the planet depends on immediate and collective action.
    """
]

for text in texts:
    summary, keywords, keyword_sentences = summarize_and_extract(text)

    print("\n📝 **Generated Summary:**")
    print(summary)

    print("\n🔑 **Extracted Keywords:**")
    print(", ".join(keywords))

    print("\n📌 **Keyword Sentences:**")
    for kw, sent in zip(keywords, keyword_sentences):
        print(f"🔹 {kw}: {sent}")

    # 🆕 Generate and display MCQs
    mcqs = generate_mcqs(text)

    print("\n🎯 **Generated MCQs:**")
    for idx, mcq in enumerate(mcqs, start=1):
        print(f"\nQuestion {idx}: {mcq['question']}")
        for opt_idx, option in enumerate(mcq['options']):
            print(f"    {chr(97 + opt_idx)}) {option}")
        print(f"Correct Answer: {mcq['answer']}")

    print("\n" + "=" * 80 + "\n")
