# Local LLM Hosting Simple Example

This Python script demonstrates hosting a small open-source LLM (GPT-2) locally using Flask. It exposes a simple API endpoint to generate text based on a given prompt, illustrating the core concept of self-hosting.

## Language

`python`

## How to Run

1. Install necessary libraries: `pip install flask transformers torch`
2. Run the script: `python host_llm.py`
3. Send POST requests to `http://127.0.0.1:5000/generate` with a JSON body like `{"prompt": "Once upon a time"}`.

## Original Article

This example accompanies the Turkish article: [10 Milyar Parametre Altı Açık Kaynak Model Hostingi: Kapsamlı Bir Rehber](https://fatihsoysal.com/blog/10-milyar-parametre-alti-acik-kaynak-model-hostingi-kapsamli-bir-rehber/).

## License

MIT — see [LICENSE](LICENSE).
