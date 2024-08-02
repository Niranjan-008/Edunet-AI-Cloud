# Edunet-AI-Cloud
This Repository Contains the project that i've done during my internship with IBM Edunet in the domain of AI &amp; Cloud.
# Panda Interface Chatbot

Panda Interface is a simple chatbot application built using Python and Tkinter. It processes user inputs, finds the most similar question from a dataset, and returns the corresponding answer. Additionally, it can summarize the answer for a concise response.

## Features

- Preprocesses user input and dataset questions using NLTK.
- Calculates similarity between user input and questions from the dataset.
- Provides the most relevant response and summarizes the answer.
- Graphical User Interface (GUI) with Tkinter for interactive user experience.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- The following Python libraries:
  - `tkinter`
  - `pandas`
  - `nltk`

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/panda-interface-chatbot.git
    cd panda-interface-chatbot
    ```

2. Install the required Python packages:

    ```bash
    pip install pandas nltk
    ```

3. Download NLTK data:

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

4. Place your dataset (`train.csv`) in the project directory.

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. A GUI window will open. You can type your question in the entry box and click 'Send' or choose from predefined options.

## Project Structure


- `main.py`: The main script containing the chatbot logic and GUI implementation.
- `train.csv`: The dataset file with 'Question' and 'Answer' columns.
- `README.md`: This file.

## Acknowledgments

This project uses the following libraries:

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pandas](https://pandas.pydata.org/)
- [NLTK](https://www.nltk.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
