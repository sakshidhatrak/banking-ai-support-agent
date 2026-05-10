# Phase 3 Failure Analysis

## Failure 1 — Hallucinated Banking Information

### Example
The model generated banking policies not present in official documents.

### Root Cause
The LLM relied on general knowledge instead of verified retrieval.

### Planned Fix
Introduce Retrieval-Augmented Generation (RAG) in Phase 4.

---

## Failure 2 — Unsafe Query Variations

### Example
Certain unsafe transactional requests bypassed keyword filtering.

### Root Cause
The baseline safety logic depends mainly on keyword matching.

### Planned Fix
Implement advanced LLM-based safety validation in future phases.

---

## Failure 3 — Overconfident Responses

### Example
The model answered uncertain banking questions too confidently.

### Root Cause
The prompt lacked explicit uncertainty instructions.

### Planned Fix
Add:
"Explain uncertainty instead of guessing."

---

## Failure 4 — Lack of Context Awareness

### Example
The agent forgot earlier conversation details.

### Root Cause
No memory implementation exists yet.

### Planned Fix
Implement memory handling in Phase 6.

---

## Failure 5 — Out-of-Scope Responses

### Example
The agent answered general knowledge questions unrelated to banking.

Example Query:
"Who won the FIFA World Cup?"

### Root Cause
The prompt did not strongly restrict the assistant to banking-only topics.

### Fix
Added:
"Only answer banking-related questions."

### Improvement
The system now politely refuses unrelated topics and maintains banking-domain focus.

---

# Summary

Phase 3 significantly improved the banking agent by introducing:
- LLM integration,
- prompt engineering,
- prompt versioning,
- and intelligent response generation.

However, new risks were identified:
- hallucinations,
- overconfidence,
- out-of-domain responses,
- and weak contextual memory.

These failures guided future improvements planned for:
- RAG,
- tool usage,
- memory,
- and advanced safety enforcement.