# RAG Test Cases

## Test 1 — Business Loan Query

Query:
What documents are required for business loans?

Expected Retrieval:
- GST registration
- financial statements
- bank statements

Expected Behaviour:
Grounded banking response.

---

## Test 2 — KYC Query

Query:
What documents are needed for KYC?

Expected Retrieval:
- identity proof
- address proof

Expected Behaviour:
Policy-grounded response.

---

## Test 3 — Missing Information Query

Query:
Explain agricultural subsidy loans.

Expected Behaviour:
Explain uncertainty without hallucination.