## Key Take Aways from Requirements to Architecture: An AI-Based Journey
1.	Deriving an architecture is challenging, since it requires domain knowledge and understaning, so architects often design only one architecture, instead of multiple candidates. 
2.	The paper proposes a standard procedure to generate architectures, arguing that standard procedures can be applied semi automatically, and an experienced architect can nudge the LLM in the right direction.
3.	The proposed process is as follows:
       1.	Automatically generating a domain model and use-case scenarios based on textual requirements by prompting LLMs. They suggest that LLMs might be suitable for such a task since they provide decent knowledge in plenty of domains. Initial experimentation showed promising results for this step.
       2.	Manually refining the domain model and scenarios.
       3.	Automatically deriving multiple software architecture candidates and architectural decisions leading to them using the domain model, scenarios, and non-functional requirements by prompting LLMs. The study suggests various models such as “4+1 model” that can be represented using PlantUML diagrams. They also aim to extract architectural design decisions taken during generation and model them as architectural design decision records(ADRs)
       4.	Automatically evaluating and comparing the candidates using LLMs. The study aims to automate the existing architectural evaluation technologies like ATAM. Whether this will be possible or not will be the outcome of their research. 
       5.	Manually refining the candidates.
       6.	Manually selecting the best fitting candidate.

The Initial study done by the paper extracts domain model of a system given its requirments. The results can be found on this repository https://github.com/qw3ry/requirements2architecture/tree/exploration 

We used the the similar prompts as in the study to extract the domain models for our examples. We have also extended the study to extract multiple architectures from the extracted domain model(step 3 of the process above). The conversations with chatgpt and generated architectures for these can be found in the folders examaple 1-5.

The prompts uses are summarized here: 

Step 1: Generating domain model from textual requirements 
1.	I will give you some requirements. Please read them and answer with "ok".
2.	The requirements pasted inside the quotation marks “”.
3.	Can you identify the functional requirements for this system.
4.	Can you identify the non-functional requirements for this system.
5.	Generate some use case scenarios involving the main functionalities of the system.
6.	Suppose you are a domain expert. Use your knowledge of the domain of this system, functional and non-functional requirements and the use cases extracted of the system, extract all domain concepts related to this system. Do not attempt to model the system itself.
7.	Please list all relations of these domain concepts to each other. List one relation per line, output the concepts in PascalCase, like "DomainConceptA", and separate the related concepts in each line with "--". Do not explain the relations.
8.	Make the list exhaustive.
9.	Draw a plantuml diagram with the concepts and relations. Keep it simple and do not include any attributes or methods.
Step 3: Generating multiple architectural candidates from the domain model.
1.	Suggest an architectural style that can be used to implement this domain model extracted above.
2.	Can you propose a PlantUML component diagram for the suggested architectural style.
3.	Extract as many architectural candidates as you want.
