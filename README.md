# gpt-hackery

## socrates

```
❯ python socrates/extract_epub_text.py "/Users/ryangr/Downloads/The Beginning of Infinity.epub"
socrates/text/The Beginning of Infinity/Chapter_Acknowledgements.txt (148 tokens)
socrates/text/The Beginning of Infinity/Chapter_Bibliography.txt (673 tokens)
socrates/text/The Beginning of Infinity/Chapter_1.txt (15232 tokens)
socrates/text/The Beginning of Infinity/Chapter_2.txt (3152 tokens)
socrates/text/The Beginning of Infinity/Chapter_3.txt (16428 tokens)
socrates/text/The Beginning of Infinity/Chapter_4.txt (13272 tokens)
socrates/text/The Beginning of Infinity/Chapter_5.txt (8291 tokens)
socrates/text/The Beginning of Infinity/Chapter_6.txt (10442 tokens)
socrates/text/The Beginning of Infinity/Chapter_7.txt (7363 tokens)
socrates/text/The Beginning of Infinity/Chapter_8.txt (13883 tokens)
socrates/text/The Beginning of Infinity/Chapter_9.txt (12566 tokens)
socrates/text/The Beginning of Infinity/Chapter_10.txt (16328 tokens)
socrates/text/The Beginning of Infinity/Chapter_11.txt (21015 tokens)
socrates/text/The Beginning of Infinity/Chapter_12.txt (9549 tokens)
socrates/text/The Beginning of Infinity/Chapter_13.txt (12525 tokens)
socrates/text/The Beginning of Infinity/Chapter_14.txt (6836 tokens)
socrates/text/The Beginning of Infinity/Chapter_15.txt (12904 tokens)
socrates/text/The Beginning of Infinity/Chapter_16.txt (8997 tokens)
socrates/text/The Beginning of Infinity/Chapter_17.txt (11384 tokens)
socrates/text/The Beginning of Infinity/Chapter_18.txt (8089 tokens)
socrates/text/The Beginning of Infinity/Chapter_Index.txt (12875 tokens)
socrates/text/The Beginning of Infinity/Chapter_Introduction.txt (439 tokens)
socrates/text/The Beginning of Infinity/Chapter_Contents.txt (137 tokens)
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
