# 🧠 GGUF Model Benchmarking App

A modular, Gradio-powered application that allows users to upload local `.gguf` LLM models, register them with a custom name and prompt template, and benchmark their performance on their own machine. Results are saved to a CSV file and visually displayed in the UI.

---

## 📌 Features

- ✅ Upload `.gguf` models  
- ✅ Set custom model names and prompt templates  
- ✅ Automatically updates configuration YAML  
- ✅ Launches benchmarking pipeline (`main.py`)  
- ✅ Displays results from `results.csv` in the UI  
- ✅ Clean and intuitive Gradio interface

---

## 🎯 Purpose

This app helps users **locally benchmark large language models** (LLMs) in `.gguf` format—especially quantized models suited for low-resource devices. It’s ideal for:

- Comparing LLMs like TinyLlama, Mistral, and Hermes 2
- Testing performance across quantization levels (Q2, Q4, etc.)
- Ensuring your hardware can support selected models
- Streamlining benchmarking workflows via UI

---

## 🛠️ How It Works

1. **Upload Model**  
   Upload a `.gguf` model file.

2. **Register Metadata**  
   Enter a name and (optional) prompt template. The app updates the `config.yaml` file with this information.

3. **Benchmark Model**  
   When you click "Run Benchmark", it triggers `main.py`, which evaluates the model based on your YAML settings.

4. **View Results**  
   The app reads `benchmark_results.csv` and displays model performance data in a table.
