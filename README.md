# ASIRI AI

ASIRI AI is an innovative document-based conversational AI application designed to make information retrieval and interaction seamless. It allows users to upload PDF documents, processes the content, and leverages advanced natural language processing (NLP) techniques to provide insightful responses to user queries. ASIRI AI demonstrates the power of combining modern AI models, scalable infrastructure, and intuitive design for enhancing productivity and user engagement.

---

## **Features**

- **PDF Document Upload:** Users can upload multiple PDF files for processing.
- **Document Analysis:** Extracts text from PDF documents efficiently.
- **Text Chunking:** Breaks down lengthy text into manageable chunks for better processing.
- **Semantic Search:** Builds a vector store for high-accuracy document retrieval using FAISS.
- **Conversational AI:** Users can ask questions related to uploaded documents and receive context-aware responses.
- **Memory Management:** Maintains conversational history for personalized and consistent interactions.
- **UI/UX Excellence:** Built with Streamlit for an intuitive and engaging interface.

---

## **Technologies Used**

ASIRI AI combines a robust technology stack for performance, scalability, and flexibility:

### **Frontend & UI**

- **[Streamlit](https://streamlit.io/):** Facilitates the creation of the web-based interface with minimal code.

### **Backend**

- **Python:** The core language powering the entire system.
- **LangChain:** Manages the integration of large language models, conversational chains, and memory.
- **PyPDF2:** Handles PDF reading and text extraction.

### **AI Models & Embeddings**

- **Hugging Face Transformers:** Hosts state-of-the-art LLMs for both text generation and embedding.
  - Example models: `Instructor-Large` for embeddings, `Zephyr-7b-alpha` for text generation.
- **FAISS (Facebook AI Similarity Search):** Provides efficient vector-based document retrieval.

### **Utilities**

- **Dotenv:** Manages environment variables for storing API keys securely.
- **Torch:** Supports the underlying ML computations for the embeddings.

---

## **Installation Guide**

To set up ASIRI AI locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/username/asiri-ai.git
   cd asiri-ai
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your API keys (e.g., Hugging Face token).

5. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## **Challenges Encountered**

1. **Token Limit Errors:**

   - Some language models exceeded token limits when processing long texts, causing runtime errors.
   - **Solution:** Adjusted `max_new_tokens` and chunked text inputs more efficiently.

2. **Model Integration:**

   - Configuring the right models for embeddings and text generation required trial and error.
   - **Solution:** Used `Instructor-Large` for embeddings due to its robust results.

3. **PDF Text Extraction:**

   - Extracting text from diverse PDF formats introduced inconsistencies.
   - **Solution:** Used PyPDF2 for reliable and fast extraction across various document types.

4. **Performance Issues:**
   - Query processing times were occasionally high due to computationally intensive models.
   - **Solution:** Optimized the backend with FAISS for faster retrieval and reduced latency.

---

## **Lessons Learned**

1. **Efficient Text Processing:**
   - Chunking and preprocessing data are critical for handling large documents in NLP applications.
2. **Model Selection Matters:**

   - Choosing the right LLMs and embeddings impacts both accuracy and computational efficiency.

3. **User-Centric Design:**

   - Intuitive interfaces (Streamlit) enhance user experience, even in technical tools.

4. **Scalability with Vector Stores:**
   - Using FAISS for document retrieval proved the importance of scalable, vector-based search methods.

---

## **Future Plans**

1. **Cloud Deployment:** Host ASIRI AI on cloud platforms for greater accessibility.
2. **Enhanced Security:** Add user authentication for a more secure experience.
3. **Support for More File Types:** Expand document processing capabilities beyond PDFs.
4. **Performance Optimization:** Further optimize query processing with more advanced indexing techniques.

---

## **Contribution Guidelines**

We welcome contributions to improve ASIRI AI! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes with clear messages.
4. Create a pull request to the main repository.

---

## **Acknowledgments**

- **Hugging Face Community** for providing cutting-edge models.
- **Streamlit** for an easy-to-use UI framework.
- **FAISS** for enabling efficient vector-based document retrieval.

---
