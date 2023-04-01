# gpt-hackery

## socrates

```
❯ python socrates/extract_epub_text.py "/Users/ryangr/Downloads/The Beginning of Infinity.epub"
Chapter_Acknowledgements.txt (148 tokens)
Chapter_Bibliography.txt (673 tokens)
Chapter_1.txt (15232 tokens)
Chapter_2.txt (3152 tokens)
Chapter_3.txt (16428 tokens)
Chapter_4.txt (13272 tokens)
Chapter_5.txt (8291 tokens)
Chapter_6.txt (10442 tokens)
Chapter_7.txt (7363 tokens)
Chapter_8.txt (13883 tokens)
Chapter_9.txt (12566 tokens)
Chapter_10.txt (16328 tokens)
Chapter_11.txt (21015 tokens)
Chapter_12.txt (9549 tokens)
Chapter_13.txt (12525 tokens)
Chapter_14.txt (6836 tokens)
Chapter_15.txt (12904 tokens)
Chapter_16.txt (8997 tokens)
Chapter_17.txt (11384 tokens)
Chapter_18.txt (8089 tokens)
Chapter_Index.txt (12875 tokens)
Chapter_Introduction.txt (439 tokens)
Chapter_Contents.txt (137 tokens)
```

```
❯ python socrates/socrates.py "socrates/text/The Beginning of Infinity/Chapter_1.txt"
╭─────────────────────────────────╮
│ Welcome to the Socratic Chatbot │
╰─────────────────────────────────╯
Socrates: What is the role of explanations in our understanding of the physical world and how do they differ from predictions?
You: Explanations are the models that produce predictions.
Socrates: That's correct. Explanations are assertions about what is out there in reality, how it behaves, and why it behaves the way it does. They help us understand the underlying processes and reasons behind phenomena. Predictions, on the other hand, are the specific outcomes or events that we expect to happen based on our explanations. The key difference is that explanations address the underlying causes and mechanisms, while predictions deal with the expected outcomes or results of those explanations.
...
```
