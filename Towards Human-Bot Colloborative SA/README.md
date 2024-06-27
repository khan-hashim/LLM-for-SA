Key Take aways from "Towards Human-Bot Colloborative Software Architecting with ChatGPT" 

The paper divides the process of driving software architecture into two parts

1. Developing the Architecture Story i.e the textual description of the system we are trying to make
2. Colloborative Architecting i.e coming up with an architecture for the system.

The architecturing process is divided into 3 steps

1. Architectural analysis i.e coming up with the functional, non-functional requirements and constraints for the story. The study concludes that ChatGPT is capable of outlining these if queried by the architect. However, ChatGPT expressed requirements and constraints may need to be refined.
2. Architectural synthesis i.e coming up with the model of the system to help visualize the strucural decompostion of the system. They use UML components and class diagrams to model the system.  
4. Architectural evaluation i.e evaluates the synthesized architecture.The study used the Software Architecture Analysis Method (SAAM) to analyze the generated architecture. ChatGPT was prompted to automatically perform SAAM.

The paper uses a case study to perform the three steps. The results from chatgpt are uploaded on this repository https://github.com/shamimaaktar1/ChatGPT4SA/tree/main

We used the the same prompts as in the study to extract the architecutres for our examples. The conversations with chatgpt and generated architectures for these can be found in the folders examaple 1-5.

The prompts are as follows:

1. Prompt gpt to identify functional requirements given the use case.
2. Prompt gpt to identify non-functional requirements given the use case.
3. Prompt gpt to suggest architecural style for the use case.
4. Ask gpt to give a component diagram for the use case(seems to use the same architectural style as it suggested)
5. Ask gpt to give a class diagram for the use case.
6. Ask gpt to suggest come design patterns that can be used in the given class diagram.
