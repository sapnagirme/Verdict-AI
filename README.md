# ⚖️ Verdict AI – AI-Powered Legal Intelligence Platform

Verdict AI is an end-to-end legal intelligence platform that leverages LLMs, advanced NLP, and transformer models to assist legal professionals, students, and researchers. It offers smart solutions for understanding, processing, and translating legal documents from Indian law.

---

![image](https://github.com/user-attachments/assets/cb25c185-11b3-4fe5-91d6-2c915bdc65fa)

## 🔍 Features

### 1. **Legal AI Chatbot**
- Trained on Indian laws: IPC, Cyber Laws, Banking Laws, Labour Laws
- Uses RAG pipeline with LangChain, HuggingFace embeddings, ChromaDB
- Powered by TinyLlama (1.1B GGUF) for offline local inference
- Deployed via Gradio with example queries and a clear chat option

### 2. **Legal Document Summarization**
- Summarizes long legal texts, PDFs, and images
- Uses Facebook’s BART Large CNN model
- Provides BERTScore & compression ratio for quality metrics

### 3. **Relevant Case Law Recommendation**
- Semantic search over 48,000+ Indian Supreme Court judgments
- Extracts case title, date, bench, legal sections, and summary
- Uses SentenceTransformers and FAISS for similarity search
- Clean UI built with Gradio for querying case categories or keywords

### 4. **Legal Document Translator**
- Translates legal docs from English to 8 Indian languages:
  Hindi, Marathi, Tamil, Telugu, Kannada, Malayalam, Punjabi, Gujarati
- Supports PDF and DOCX files
- Built using rotary-indictrans2-en-indic-dist-200M (HuggingFace)
- Clean preview and downloadable output files

---

## 💻 Tech Stack

- **Languages:** Python
- **Frameworks:** LangChain, HuggingFace Transformers, Gradio, Flask
- **Models:** TinyLlama (GGUF), BART Large CNN, SentenceTransformer, IndicTrans2
- **Vector DBs & Search:** ChromaDB, FAISS
- **Libraries:** PyMuPDF, python-docx, spaCy, scikit-learn, matplotlib

---

### 📽️ Project Demo Video

This demo video walks through all four features of Verdict AI:  
1. Legal AI Chatbot
2. Legal Document Summarization
3. Relevant Case Law Recommendation
4. Legal Document Translator

📂 Video Location: `Verdict AI UI/static/videos/Website Video.mp4`

> 📌 The video is embedded in the `index.html` UI. You can also view it by opening the HTML file locally.
