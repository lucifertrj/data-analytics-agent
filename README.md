# Data Analysis Agent - for CSV data

## Architecture

```mermaid
%%{init: {
  "themeVariables": {
    "fontFamily": "Arial",
    "textColor": "#fff",
    "edgeLabelBackground":"#000",
  }
}}%%
graph TD
    A[User Query] --> B[LLM Analyzes DataFrame Schema]
    B --> C[Generate Python Code]
    C --> D[Python REPL Tool]
    D --> E[Execute on DataFrame]
    E --> F{Success?}
    F -->|Error| G[LLM Sees Error]
    G --> C
    F -->|Yes| H[Format Result]
    H --> I[Return Answer to User]

    style A fill:#29B5E8,color:#fff,stroke:#29B5E8
    style B fill:#11567F,color:#fff,stroke:#11567F
    style C fill:#11567F,color:#fff,stroke:#11567F
    style D fill:#000000,color:#fff,stroke:#000000
    style E fill:#ffffff,color:#000,stroke:#000000
    style F fill:#ffffff,color:#000,stroke:#000000
    style G fill:#ffffff,color:#000,stroke:#000000
    style H fill:#11567F,color:#fff,stroke:#11567F
    style I fill:#29B5E8,color:#fff,stroke:#29B5E8
```

## Overview

This project implements an intelligent data analysis system that:

1. **Accepts User Queries** - Users provide natural language questions about their data
2. **Analyzes DataFrame Schema** - The LLM understands the structure and content of the data
3. **Generates Python Code** - Creates executable Python code to answer the query
4. **Executes Code** - Runs the generated code in a Python REPL environment
5. **Handles Errors** - If execution fails, the LLM sees the error and iterates on the solution
6. **Formats Results** - Presents the answer in a user-friendly format

## Dependencies

See `requirements.txt` for all project dependencies, including:
- LangChain and LangGraph for LLM orchestration
- Streamlit for the web interface
- Pandas and NumPy for data manipulation
- Google Generative AI for LLM capabilities