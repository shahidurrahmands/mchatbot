from setuptools import find_packages, setup
setup(
    name="medical_chatbot",
    version="0.1.0",
    author="SM Rehman",
    author_email="srsayeedict@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.2.0",
        "langchain-pinecone>=0.1.0",
        "sentence-transformers>=2.7.0",
        "pinecone-client<4.0.0",
        "PyPDF2>=3.0.1",
        "transformers>=4.44.0",
        "huggingface_hub>=0.24.0",
        "e."
    ],
)
