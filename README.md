# A Question
## ?

一问

Questions are very much the connections of our intangible and intermittent thoughts. Branching dialogues through space and time, it extends our scope of knowing, and directs us to our boundaries of the unknown. Through language, the ability to extract from abstract, we formulate the flows and flux of our stream of consciousness. Questions inherits past memories and flourishes future imaginations. Stemming from the roots of our mind, and grows to gradually interweave as a interconnected whole. Enabling us to compose collectively, a continuous reflective monologue inherent within us, a question.

![Screenshot 2022-10-14 182056](https://user-images.githubusercontent.com/60975534/195952313-e9a77f81-0cd9-4e82-8b4b-6ae62228c1bd.png)

This project uses GPT-3 from OpenAI to generate open-ended question based on the user's response to the previous question, as the TouchDesigner program (A Question.toe) converts the text into SVG file, and then into G-Code, ultimately outputs via usb serial to control a CNC plotting machine (GRBL) to write out the generated question.


## ?
GPT-3 Prompt:

"Q: What harsh truths do you prefer to ignore?\nA: The truth of my ignorance of truths.\nQ: Is free will real or just an illusion?\nA: An illusion when it is real, real when it is an illusion.\nQ: Is there a meaning to life?\nA: You can decide for yourself\nQ: What should be the goal of humanity?\nA: Depends\nQ: Does fate exist?\nA: perhaps\nQ: What does it mean to live a good life?\nA: To not have to ask such question\nQ: Why do we dream?\nA: because we believe\nQ: what is?\nA: {Input}\nQ:"

![Screenshot 2021-06-22 205935](https://user-images.githubusercontent.com/60975534/195952231-b1655476-e23b-43c7-8c43-2d1f64dc5a4f.png)


SOP to SVG pipeline by Matthew Ragan: 

https://github.com/raganmd/touchdesigner-sop-to-svg


SVG to G-CODE (GRBL) python script from: 

https://github.com/vishpat/svg2gcode


CNC.tox:

I made a custom tox in TouchDesigner that automatically reads G-Code file and controls CNC plotter via usb serial

![Screenshot 2022-10-14 181854](https://user-images.githubusercontent.com/60975534/195952156-f784f40c-899c-4da1-86ee-2a9dda391e6a.png)

