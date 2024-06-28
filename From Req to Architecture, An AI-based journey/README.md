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
