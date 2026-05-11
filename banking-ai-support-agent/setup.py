from setuptools import setup, find_packages

setup(
    name="banking-ai-support-agent",
    version="1.0.0",

    author="Your Name",

    description=(
        "Enterprise AI Banking Support Agent "
        "with RAG, Tool Calling, Memory, "
        "Adaptive Behaviour and Safety Guardrails"
    ),

    packages=find_packages(),

    include_package_data=True,

    install_requires=[

        # Core LLM
        "openai",

        # Environment variables
        "python-dotenv",

        # Streamlit UI
        "streamlit",

        # LangChain
        "langchain",
        "langchain-community",
        "langchain-openai",

        # Vector DB
        "chromadb",

        # Embeddings / ML
        "tiktoken",

        # Utilities
        "pydantic"
    ],

    python_requires=">=3.10",

    entry_points={
        "console_scripts": [

            "banking-agent=app.main:main",
        ]
    },

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",
    ],
)