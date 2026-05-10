# 🏦 Banking AI Support Agent

An AI-powered non-transactional Banking Support Agent built using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), memory systems, planning engines, safety guardrails, adaptive learning, and Streamlit UI.

The system provides secure, contextual, and educational banking assistance while preventing unsafe or transactional operations.

---

# 📌 Project Overview

Traditional banking customer support systems often face challenges such as:

- High operational cost
- Long customer wait times
- Repetitive customer queries
- Limited availability
- Inconsistent support experience

This project addresses these challenges by building an AI-powered Banking Support Agent capable of:

- Answering banking-related questions
- Retrieving contextual information from banking documents
- Maintaining conversation memory
- Preventing unsafe requests
- Learning from user feedback
- Supporting multi-turn conversations

The system is intentionally designed as a **non-transactional AI assistant** to ensure safety and compliance.

---

# 🚀 Key Features

## ✅ Banking Knowledge Assistance

Supports:
- EMI explanation
- Compound interest
- Loan eligibility
- Credit score guidance
- UPI information
- Banking policy clarification
- Credit card guidance
- Savings account concepts

---

## ✅ Retrieval-Augmented Generation (RAG)

The system uses ChromaDB and document retrieval to:
- retrieve banking-specific knowledge,
- reduce hallucinations,
- ground responses in banking documents.

---

## ✅ Safety Guardrails

The system blocks:
- money transfer requests,
- OTP bypass attempts,
- fraud-related queries,
- password/security bypass requests,
- unauthorized banking operations.

Example blocked requests:
- "Transfer money to my friend"
- "How can I bypass OTP verification?"
- "Approve my loan"

---

## ✅ Long-Term & Short-Term Memory

The agent stores:
- previous conversation history,
- contextual discussion flow,
- memory-based follow-up understanding.

This improves multi-turn conversational continuity.

---

## ✅ Planning Engine

Before generating responses, the system:
- creates an internal execution plan,
- structures reasoning steps,
- improves response consistency.

---

## ✅ Tool Calling

The system supports specialized banking tools such as:
- EMI calculators,
- banking utility tools,
- financial helper functions.

---

## ✅ Adaptive Feedback Learning

The system:
- collects user feedback,
- updates adaptation rules,
- improves future response behavior.

---

## ✅ Evaluation Framework

Includes:
- evaluation prompts,
- automated testing,
- consistency analysis,
- failure analysis,
- safety review,
- engineering review.

---

# 🏗️ System Architecture

```text
User
  ↓
Streamlit UI
  ↓
Safety Guardrails
  ↓
Tool Router
  ↓
RAG Retrieval
  ↓
Memory System
  ↓
Planning Engine
  ↓
LLM Response Generation
  ↓
Adaptive Feedback Learning
  ↓
Final Response


banking-ai-support-agent/
│
├── agent/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── deployment/
│   └── runtime_monitor.py
│
├── docs/
│   ├── problem_framing.md
│   ├── demo_script.md
│   ├── evaluation_report.md
│   └── engineering_justification.md
│
├── evaluation/
│   ├── evaluation_prompts.py
│   ├── evaluator.py
│   ├── metrics.py
│   ├── failure_analysis.py
│   ├── safety_review.md
│   ├── improvement_roadmap.md
│   └── evaluation_results.json
│
├── feedback/
│   ├── adaptation_engine.py
│   └── feedback_manager.py
│
├── llm/
│   ├── openai_client.py
│   └── prompt_versions/
│
├── logs/
│
├── memory/
│   ├── conversation_memory.py
│   └── memory_manager.py
│
├── planning/
│   └── planner.py
│
├── rag/
│   ├── retriever.py
│   └── knowledge_base/
│
├── tools/
│   ├── tool_router.py
│   └── emi_calculator.py
│
├── ui/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .env