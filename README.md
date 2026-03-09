# Fine-Tuning a Small Language Model for Mental Health Support

This project demonstrates how a **Small Language Model (SLM)** can be fine-tuned to provide more empathetic and context-aware responses in mental-health conversations.

The base model **Qwen2.5-3B-Instruct** was fine-tuned using **QLoRA (Quantized Low-Rank Adaptation)** on a mental-health conversational dataset to improve response quality.

The project includes:

• Model fine-tuning pipeline  
• Response comparison between base and fine-tuned models  
• Quantitative evaluation using NLP metrics  
• Visualization of model improvements  

---

# Project Pipeline

![WhatsApp Image 2026-03-09 at 15 47 53](https://github.com/user-attachments/assets/34090d42-7871-4382-8052-b333232511a7)



The training pipeline consists of the following stages:

1. **Dataset Preparation**
2. **Instruction Formatting**
3. **QLoRA Fine-Tuning**
4. **Chatbot Generation**
5. **Model Evaluation**

Pipeline flow:

---

# Why Fine-Tuning?

Large language models are trained on broad internet data and are not optimized for specific domains such as **mental-health conversations**.

Fine-tuning allows the model to:

• learn domain-specific language patterns  
• produce more empathetic responses  
• improve contextual understanding  
• reduce generic or insensitive replies  

Instead of training a model from scratch (which requires enormous compute resources), fine-tuning adapts an existing model efficiently for a specialized task.

---

# Why Small Language Models (SLMs)?

Small Language Models are becoming increasingly important in modern AI systems due to their **efficiency and deployability**.

Advantages of SLMs:

• lower inference cost  
• faster response time  
• easier deployment in real applications  
• efficient fine-tuning with limited hardware  
• suitable for domain-specific assistants  

Using a **3B parameter model** provides a good balance between **performance and computational efficiency**.

---

# Base Model Selection

The base model used in this project is:

**Qwen2.5-3B-Instruct**

Reasons for selecting this model:

• strong instruction-following capability  
• optimized for conversational tasks  
• manageable parameter size for fine-tuning  
• good balance between performance and compute requirements  
• compatible with Hugging Face ecosystem  

This makes it an ideal candidate for **efficient domain adaptation using QLoRA**.

---

# Fine-Tuning Method

This project uses **QLoRA (Quantized Low-Rank Adaptation)**.

QLoRA enables efficient fine-tuning by:

• training only a small subset of parameters  
• keeping the base model weights frozen  
• reducing GPU memory usage  
• enabling training on limited hardware

This allows large models to be fine-tuned even with **consumer-level GPUs or cloud notebooks**.

---

# Model Response Comparison

The following comparison illustrates how the fine-tuned model produces more empathetic responses.

![Model Comparison]<img width="3000" height="1000" alt="aligned_model_comparison" src="https://github.com/user-attachments/assets/b6745724-b484-4fcf-bf40-e9c972a75f5c" />


Example prompt:"I feel lonely and cannot sleep"
Base model response:"Loneliness can occur due to stress or changes in life circumstances."
Fine-tuned model response:"I'm really sorry you're feeling lonely.
That can be very difficult. If you'd like,
you can share what has been making you feel this way."


The fine-tuned model demonstrates improved **empathy and conversational tone**.

---

# Model Evaluation

To quantitatively measure improvement, the models were evaluated using:

• **BLEU** — n-gram overlap with reference responses  
• **ROUGE-L** — longest common subsequence similarity  
• **Semantic Similarity** — embedding-based similarity measure  

Results:

![Evaluation]<img width="3600" height="2000" alt="evaluation_results_professional" src="https://github.com/user-attachments/assets/80dfc7f0-f5ec-403f-9e80-ec0759c6b1ef" />


Performance comparison:

| Metric | Base Model | Fine-Tuned Model |
|------|------|------|
| BLEU | 0.18 | **0.41** |
| ROUGE-L | 0.25 | **0.62** |
| Semantic Similarity | 0.55 | **0.84** |

The fine-tuned model shows **significant improvement across all evaluation metrics**.

---

# Challenges Faced

During the development of this project, several challenges were encountered.

### 1. Limited GPU Memory

Fine-tuning large language models requires significant GPU memory.

**Solution**

QLoRA was used to reduce memory consumption by:

• quantizing model weights  
• training only low-rank adapter layers  

This allowed efficient training on limited resources.

---

### 2. Instruction Formatting

Raw conversational datasets often contain inconsistent formats.

**Solution**

The dataset was converted into **instruction-response format**, enabling the model to better learn conversational patterns.

---

### 3. Evaluating Generative Models

Traditional accuracy metrics are not suitable for generative models.

**Solution**

Multiple evaluation metrics were used:

• BLEU  
• ROUGE-L  
• Semantic similarity  

This provided both **lexical and semantic evaluation**.

---

# Technologies Used

Python  
PyTorch  
Hugging Face Transformers  
PEFT (QLoRA)  
Sentence Transformers  
Matplotlib  
FastAPI (for deployment prototype)

---

# Future Improvements

Potential improvements include:

• Retrieval Augmented Generation (RAG)  
• conversation memory using vector databases  
• safety filters for sensitive mental-health queries  
• reinforcement learning alignment  

---




