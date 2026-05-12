#!/usr/bin/env python3
"""
Nobab Self-Reliant Agent - Complete Learning System with ChromaDB Persistence
"""

import os
import json
import smtplib
import re
import time
import argparse
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Necessary Imports for ChromaDB, Embeddings, and Question Generation ---
# ChromaDB: Persistent client for storing and retrieving vector data.
import chromadb
# SentenceTransformer: Creates embeddings for semantic search.
from sentence_transformers import SentenceTransformer
# Questgen: Generates questions from text. Handled with try-except for robustness.
try:
    from Questgen import main as qg
except ImportError:
    print("Questgen not found. Install with: pip install git+https://github.com/ramsrigouthamg/Questgen.ai")
    qg = None

# ======================= CONFIGURATION =======================
# Use a persistent client to save data for GitHub push.
CHROMA_DB_PATH = "./chroma_db"  # Relative path to the directory.
COLLECTION_NAME = "nobab_knowledge"

# Email settings (use GitHub Secrets for security)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.environ.get("SMTP_USERNAME", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
REPORT_EMAIL = os.environ.get("REPORT_EMAIL", "admin@example.com")

# ======================= ChromaDB Setup =======================
# Initialize the persistent client. This ensures data is saved to disk.
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# Use `get_or_create_collection` to avoid conflicts on multiple runs.
collection = client.get_or_create_collection(name=COLLECTION_NAME)

# Load the SentenceTransformer model for creating embeddings.
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# ======================= Helper: Email =======================
def send_email(subject, body):
    """Send an email report using SMTP."""
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

# ======================= Step 1: Generate Questions =======================
def generate_questions(text, max_questions=5):
    """Generate MCQs from a given text using Questgen."""
    if qg is None:
        print("Questgen not available. Skipping question generation.")
        return []
    qe = qg.QGen()
    payload = {"input_text": text}
    try:
        output = qe.predict_mcq(payload)
        questions = []
        # If you need to increase complexity, you can adjust 'max_questions'
        for q_item in output.get('questions', [])[:max_questions]:
            questions.append({
                "question": q_item['question_statement'],
                "options": q_item.get('options', []),
                "answer": q_item['answer'],
                "context": text[:200]  # Save a snippet of context
            })
        print(f"[√] Generated {len(questions)} questions.")
        return questions
    except Exception as e:
        print(f"[!] Questgen error: {e}")
        return []

# ======================= Step 2: Answer & Index =======================
def index_knowledge(text, metadata=None):
    """Store a text chunk and its embedding in ChromaDB."""
    if not text:
        return
    # Create a unique ID for the document.
    doc_id = f"doc_{int(time.time())}_{hash(text) % 10000}"
    # ChromaDB can also accept embedding directly, but we let it auto-generate.
    embedding = embedder.encode([text]).tolist()[0]
    # Upsert (update or insert) the document into the collection.
    collection.upsert(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=metadata or [{}]
    )
    print(f"📚 Indexed: {text[:50]}...")

# ======================= Step 3: Self Evaluation =======================
def evaluate_learning(question_list, answer_text):
    """
    A simple evaluation: check if keywords from the question appear in the answer.
    This simulates self-evaluation; you can enhance it with a local LLM later.
    """
    if not answer_text:
        return 0.0
    # Extract keywords from the question (simple method)
    keywords = re.findall(r'\b\w+\b', question_list[0]['question'].lower()) if question_list else []
    score = 0
    for kw in keywords:
        if kw in answer_text.lower():
            score += 1
    max_score = len(keywords) if keywords else 1
    return (score / max_score) * 100

# ======================= Step 4: Weekly Assessment =======================
def weekly_assessment():
    """Assess the knowledge stored over the week and email a report."""
    print("\n[📊] Weekly Assessment Starting...")
    all_data = collection.get()
    if not all_data['documents']:
        print("[!] No knowledge stored yet. Cannot assess.")
        return
    print(f"Total Knowledge Items: {len(all_data['documents'])}")
    # Simple evaluation: count stored items and check first few.
    # Save a report to a file in the datasets directory (for GitHub push)
    os.makedirs("datasets", exist_ok=True)
    report = f"Weekly Learning Report\nDate: {datetime.now()}\nTotal Items: {len(all_data['documents'])}"
    report += "\nFirst 3 stored items:\n"
    for doc in all_data['documents'][:3]:
        report += f"- {doc[:100]}...\n"
    report_path = "datasets/weekly_report.txt"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Report saved to {report_path}")
    # Send email only if configured
    if SMTP_USERNAME and SMTP_PASSWORD:
        send_email("Nobab Weekly Learning Report", report)
    return len(all_data['documents'])

# ======================= Main Loop =======================
def main():
    parser = argparse.ArgumentParser(description="Nobab Self-Reliant Agent")
    parser.add_argument("--topic", type=str, default="Cybersecurity", help="Topic to learn")
    parser.add_argument("--assess", action="store_true", help="Run weekly assessment only")
    args = parser.parse_args()

    if args.assess:
        weekly_assessment()
        return

    # Step 1: Learn a topic (simulate by using a predefined text chunk)
    print(f"🤖 Nobab Agent starting. Learning about: {args.topic}")
    topic_text = f"Cybersecurity protects networks, devices, and data from unauthorized access, damage, or theft. Core areas include {args.topic}."
    # Step 2: Generate questions from the topic
    questions = generate_questions(topic_text, max_questions=3)
    if questions:
        # Step 3: For evaluation, we use the same topic as an answer (self-generated)
        answer_body = topic_text
        # Step 4: Evaluate the learning (simple keyword matching)
        score = evaluate_learning(questions, answer_body)
        print(f"Self-Evaluation Score: {score:.2f}%")
        # Step 5: Index all knowledge (store text + question contexts)
        index_knowledge(topic_text, metadata={"topic": args.topic, "score": score})
        for q in questions:
            q_text = f"Q: {q['question']} A: {q['answer']}"
            index_knowledge(q_text, metadata={"topic": args.topic, "type": "qa"})
        print("[√] Knowledge Base Built. Ready for Assessment.")
    else:
        print("[!] No questions generated. Check Questgen installation.")

    # Ensure datasets directory exists and add a timestamp file for reassurance.
    os.makedirs("datasets", exist_ok=True)
    with open("datasets/last_run.txt", "w") as f:
        f.write(f"Last run: {datetime.now()}\nTopic: {args.topic}\nScore: {score if questions else 0:.2f}%\n")

if __name__ == "__main__":
    main()
