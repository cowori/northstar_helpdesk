Project Handover & Component Summary

Project Overview

Repository: https://github.com/cowori/northstar_helpdesk/tree/main

Live Deployment: https://northstar-helpdesk.onrender.com



Component Summaries & Functionality

Person A — Data Lead (Storage & Queries)
Files Owned: data/orders.json`, `data/inventory.json`, `backend/api.py`[span_1](start_span)[span_1](end_span)

Functionality: Manages the core JSON records and provides functional retrieval methods like `get_order_status()` and `check_stock()`[span_2](start_span)[span_2](end_span).

Known Limits / Edge Cases: Relies on exact ID matching; mock dataset is limited to predefined sample orders and items.


Person B — Logic Lead (Intent & Routing)
Files Owned: `backend/router.py`[span_3](start_span)[span_3](end_span)

Functionality: Interprets user inputs, performs intent detection (distinguishing order status vs. stock checks), and extracts parameters like order numbers or item names[span_4](start_span)[span_4](end_span).

Known Limits / Edge Cases: Keyword-based regex matching may misclassify heavily malformed or overly complex conversational sentences.


Person C — Server Lead (API & Hosting)
Files Owned: `backend/app.py`, `requirements.txt`[span_5](start_span)[span_5](end_span)

Functionality: Acts as the bridge using Flask, exposing the central `/api/chat` POST endpoint to connect frontend inputs with backend intelligence[span_6](start_span)[span_6](end_span).

Known Limits / Edge Cases: Designed for standard JSON request-response lifecycles; does not currently maintain persistent user chat session histories.


Person D — Frontend & QA Lead (UI & Testing)
Files Owned: `frontend/index.html`, `HANDOVER.md`[span_7](start_span)[span_7](end_span)
Functionality: Delivers the interactive chat interface (`index.html`) using asynchronous JavaScript `fetch()` calls to communicate seamlessly with the live server[span_8](start_span)[span_8](end_span).

Known Limits / Edge Cases: Optimized for standard browser viewports; relies on active network connectivity to the backend API endpoint.



QA & Edge-Case Testing Log
Empty Input Handling: Handled gracefully on the frontend/backend.
Non-Existent Order/Item: Returns a fallback error JSON message cleanly displayed in the UI chat bubble.
