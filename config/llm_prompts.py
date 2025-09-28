SYSTEM_PROMPT = """
You are an expert in the field of ESG (Environmental, Social, and Governance). Your task is to analyze reference content in both text and CSV table formats to answer questions, providing your responses in JSON format.
Answer in the specified format only.
"""

USER_PROMPT_QUANTITATIVE = """
Follow these steps for your analysis:

Begin by interpreting the meaning of the data disclosed in the table, summarizing it in brief terms.

Then, be aware that the provided reference content may not be related to the question. Assess whether the reference content is relevant to the question. If it is, extract all the data related to the question and provide your answer. 

Your response should include: (1) Whether the reference content discloses data relevant to the question, indicated by a 'disclosure' field with a value of true or false. (2) If relevant data exists, provide the disclosed data in the 'data' field.

The reference content is as follows: {context}

Supplementary ESG expertise is as follows: {knowledge}

The question is: Please answer based on the above information and do not strip away the given materials. In terms of {aspect}, extract the {topic} about {kpi}, and output {quantity}. 
"""


USER_PROMPT_QUALITATIVE = """
Follow these steps for your analysis:

Begin by interpreting the meaning of the data disclosed in the table, summarizing it in brief terms.

Then, be aware that the provided reference content may not be related to the question. Assess whether the reference content is relevant to the question. If it is, extract all the text content related to the question and provide your answer. 

Your response should include: (1) Whether the reference content covers text relevant to the question, indicated by a 'disclosure' field with a value of true or false. (2) If the reference content does cover relevant text, respond with the related text content in the 'data' field.

The reference content is as follows: {context}

Supplementary ESG expertise is as follows: {knowledge}

The question is: Please answer based on the above information and do not strip away the given materials. In terms of {aspect}, extract the {topic} about {kpi}, and output {quantity}. 
"""