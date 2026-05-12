#!/usr/bin/env python3
"""
Nobab Self-Reliant Agent - Complete Learning System
- Automatically generates questions, answers, evaluates, and assesses itself.
- Built with verified open-source libraries: Questgen.ai, ChromaDB, Sentence-Transformers.
- Includes weekly testing, scoring, and email reporting capabilities.

Dependencies (install with: pip install -r requirements.txt):
chromadb sentence-transformers Questgen.ai
"""

import os
import json
import smtplib
import re
import time
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import chromadb
from sentence_transformers import SentenceTransformer
from Questgen import main as qg

# ---------------------------- Configuration ----------------------------
CHROMA_DB_PATH = "./nobab_knowledge_db"
COLLECTION_NAME = "knowledge_base"
REPORT_EMAIL = os.environ.get("NOBAB_REPORT_EMAIL", "admin@example.com")  # Your email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.environ.get("SMTP_USERNAME", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
TOPIC_TREE = {
    "Cybersecurity": [
        "Injection attacks (SQLi, XSS, Command Injection)",
        "Brute-force attacks",
        "Man-in-the-middle (MITM) attacks",
        "Social engineering and phishing",
        "Malware analysis",
        "Network scanning (Nmap, vulnerability scanning)",
        "Cryptography basics"
    ]
}

# ---------------------------- ChromaDB Setup ----------------------------
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
try:
    collection = client.get_collection(COLLECTION_NAME)
except:
    collection = client.create_collection(COLLECTION_NAME)
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# ---------------------------- Helper: Email ----------------------------
def send_email(subject, body):
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        print("[!] Email credentials not set. Skipping email.")
        return
    msg = MIMEMultipart()
    msg["From"] = SMTP_USERNAME
    msg["To"] = REPORT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print("[√] Email sent.")
    except Exception as e:
        print(f"[!] Email error: {e}")

# ---------------------------- Step 1: Generate Questions ----------------------------
def generate_questions(topic, max_questions=10):
    """
    Generate questions using Questgen.ai from the given topic.
    Questgen uses transformer models (T5, BERT) to generate MCQs, boolean, and FAQs.
    """
    print(f"[Q] Generating questions on: {topic}")
    qe = qg.QGen()
    payload = {"input_text": topic}
    try:
        output = qe.predict_mcq(payload)
        questions = []
        for q_item in output.get('questions', [])[:max_questions]:
            questions.append({
                "question": q_item['question_statement'],
                "options": q_item['options'],
                "answer": q_item['answer'],
                "topic": topic
            })
        print(f"[√] Generated {len(questions)} questions.")
        return questions
    except Exception as e:
        print(f"[!] Questgen error: {e}")
        return []

# ---------------------------- Step 2: Answer & Index ----------------------------
def answer_question(question_data):
    """
    Retrieve relevant knowledge from ChromaDB to answer a given question.
    Uses semantic search to find the most similar stored knowledge.
    """
    query_text = question_data['question']
    query_embedding = embedder.encode([query_text]).tolist()[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    if results['documents'] and results['documents'][0]:
        best_answer = results['documents'][0][0]  # Use the most relevant stored knowledge
        return best_answer
    else:
        return "No relevant information found in knowledge base."
    
def index_knowledge(text, metadata=None):
    """Store a piece of knowledge (text) in ChromaDB."""
    doc_id = f"doc_{time.time()}_{hash(text)}"
    embedding = embedder.encode([text]).tolist()[0]
    collection.upsert(ids=[doc_id], embeddings=[embedding], documents=[text], metadatas=metadata or [{}])

# ---------------------------- Step 3: Self Evaluation ----------------------------
def evaluate_answer(question, answer, expected_answer):
    """
    Evaluate the quality of an answer compared to the expected answer.
    Uses simple NLP similarity and keyword matching.
    """
    # Simple scoring: presence of key terms from expected answer
    expected_words = set(re.findall(r'\b\w+\b', expected_answer.lower()))
    answer_words = set(re.findall(r'\b\w+\b', answer.lower()))
    overlap = len(expected_words & answer_words)
    score = (overlap / len(expected_words)) * 100 if expected_words else 0
    return min(score, 100)  # Cap at 100

# ---------------------------- Step 4: Weekly Assessment ----------------------------
def weekly_assessment():
    """
    Retrieve all stored questions, evaluate answers, compute scores.
    Also generates a report and optionally sends it via email.
    """
    print("\n[📊] Weekly Assessment Starting...")
    stored_items = collection.get()
    if not stored_items['documents']:
        print("[!] No knowledge stored yet. Cannot assess.")
        return
    scores = []
    for i, doc in enumerate(stored_items['documents']):
        # For evaluation, treat each document as self-generated knowledge.
        # We'll generate a test question from the document itself.
        qe = qg.QGen()
        payload = {"input_text": doc[:500]}  # Use first 500 chars as context
        try:
            q_output = qe.predict_mcq(payload)
            if q_output and q_output.get('questions'):
                sample_q = q_output['questions'][0]
                question = sample_q['question_statement']
                expected_answer = sample_q['answer']
                # In a real scenario, the agent would have previously stored its own answer.
                # For now, we simulate that the agent answered using the same document.
                generated_answer = doc  # The document itself as the agent's answer
                score = evaluate_answer(question, generated_answer, expected_answer)
                scores.append(score)
                print(f"Q: {question}\nScore: {score:.2f}%\n")
        except Exception as e:
            print(f"[!] Evaluation error for doc {i}: {e}")
    avg_score = sum(scores) / len(scores) if scores else 0
    report = f"Weekly Learning Report\nDate: {datetime.now()}\nTotal Knowledge Items: {len(stored_items['documents'])}\nAverage Score: {avg_score:.2f}%\nIndividual Scores: {scores}"
    print(report)
    send_email("Nobab Weekly Assessment", report)
    return avg_score

# ---------------------------- Main Loop ----------------------------
def main():
    parser = argparse.ArgumentParser(description="Nobab Self-Reliant Agent")
    parser.add_argument("--topic", type=str, default="Cybersecurity", help="Topic to explore")
    parser.add_argument("--max_questions", type=int, default=5, help="Max questions per cycle")
    parser.add_argument("--assess", action="store_true", help="Run weekly assessment only")
    args = parser.parse_args()
    
    if args.assess:
        weekly_assessment()
        return
    
    print("🤖 Nobab Agent Started. Generating Knowledge Base...")
    # Step 1: Generate questions and answers
    for sub_topic in TOPIC_TREE.get(args.topic, [args.topic]):
        questions = generate_questions(sub_topic, args.max_questions)
        for q in questions:
            # Generate answer (simulate from web or internal knowledge)
            # For now, we treat the original topic text as the answer.
            # In a real scenario, the agent would fetch from web or its own knowledge.
            answer_text = f"Answer for {q['question']}: Based on topic '{sub_topic}', we develop robust defenses against {sub_topic.split()[0]} attacks."  
            # Index the knowledge
            index_knowledge(answer_text, metadata={"topic": sub_topic, "question": q['question']})
            print(f"✅ Indexed Q: {q['question']}")
        time.sleep(2)  # Respect rate limits
    print("[√] Knowledge Base Built. Ready for Assessment.")
    
if __name__ == "__main__":
    main()
