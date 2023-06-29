### COBOL
Common Business-Oriented Language (COBOL) is a high-level programming language developed in the late 1950s. It was designed specifically for business data processing and remains in use today, particularly in legacy systems. COBOL has a complex syntax that includes numerous keywords, data structures, and specific conventions for handling business data. The verbose nature of the language and its unconventional structure make it difficult for AI models to learn and generate COBOL code accurately. Additionally, as COBOL is often associated with legacy systems the availability of large-scale, diverse, and openly licensed COBOL code datasets is limited. This scarcity of data makes it challenging for AI models to learn the intricacies of the language and generate high-quality COBOL code.

### The Stack
The stack is a massive dataset specifically designed for training large language models (LLMs) in the field of Artificial Intelligence to understand and generate code. It consists of 3.1 terabytes of source code written in 30 different programming languages. The purpose of creating the stack is to foster open and responsible research on LLMs for code-related tasks.

By training 350 million-parameter decoders on various subsets of code from the stack text2code benchmarks have achieved promising results. These benchmarks evaluate the LLM's ability to convert natural language prompts into executable code accurately.

The code samples in The stack dataset are collected from GitHub repositories with permissive licenses, allowing for legal and ethical use in research and development. This approach ensures that the dataset contains a diverse selection of languages and is openly available, enabling researchers to study and advance the field of AI for code-related tasks, including COBOL.

### Calling the 'get_stack.py' Script
To extract only COBOL parts from The stack dataset using the 'get_stack.py' script, follow these steps:

1. Ensure that you have installed the required dependencies by using pip to install the 'datasets' library.
2. Open a terminal or command prompt and navigate to the directory where the 'get_stack.py' script is saved.
3. Run the script by executing the following command: `py get_stack.py`
