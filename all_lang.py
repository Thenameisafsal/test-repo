# import streamlit as st
# #from langchain.prompts import PromptTemplate
# from langchain_community.llms import CTransformers

# ## Function To get response from LLaMA 2 model
# def getLLamaresponse(input_text, language):
#     ### LLaMA 2 model
#     # llm = CTransformers(model='H:\Test Model\langchain-main\Llma\llama-2-7b-chat.ggmlv3.q8_0.bin',
#     #                     model_type='llama',
#     #                     config={'max_new_tokens': 2000,
#     #                             'temperature': 0.01})
#     llm = CTransformers(model='./Llma/llama-2-7b-chat.ggmlv3.q8_0.bin',
#                         model_type='llama',
#                         config={'max_new_tokens': 2000,
#                                 'temperature': 0.01})
    
#     print("Language: ",language)

#     ## Prompt Template
#     prompt = f"""
#         Write a {language} program or function for the following requirement:
#         {input_text}
#     """
    
#     ## Generate the response from the LLaMA 2 model
#     response = llm(prompt)
#     return response

# def main():
#     st.set_page_config(page_title="ProgAI",
#                        page_icon='🐍',
#                        layout='centered',
#                        initial_sidebar_state='collapsed')

#     st.header("ProgAI 🐍")

#     input_text = st.text_input("Enter the Requirement")
#     language = st.selectbox("Select Programming Language", ["Python", "C", "C++", "Java"])

#     submit = st.button("Generate")

#     ## Final response
#     if submit:
#         st.code(getLLamaresponse(input_text, language), language=language.lower())

# if _name_ == "_main_":
#     main()


# from langchain_community.llms import CTransformers

# ## Function To get response from LLaMA 2 model
# def getLLamaresponse(input_text, language):
    
#     print(input_text)
#     print(language)
#     ### LLaMA 2 model
#     llm = CTransformers(model='Llma/llama-2-7b-chat.ggmlv3.q8_0.bin',
#                         model_type='llama',
#                         config={'max_new_tokens': 2500,
#                                 'temperature': 0.01})
    
#     print("Language: ", language)

#     ## Prompt Template
#     prompt = f"""
#         Write a {language} program or function for the following requirement:
#         {input_text}
#     """
    
#     ## Generate the response from the LLaMA 2 model
#     response = llm(prompt)
#     return response



from langchain_community.llms import CTransformers

## Function to get response from LLaMA 2 model
def getLLamaresponse(input_text, language):
    print("Input Text:", input_text)
    print("Language:", language)
    
    ### Initialize LLaMA 2 model
    llm = CTransformers(model='Llma/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 1024,  # Increase this to the max supported by the model
                                'temperature': 0.01})
    
    ## Function to split input text into chunks
    def split_input_text(input_text, max_tokens=512):
        words = input_text.split()
        chunks = []
        current_chunk = []

        for word in words:
            current_chunk.append(word)
            if len(current_chunk) >= max_tokens:
                chunks.append(" ".join(current_chunk))
                current_chunk = []

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    ## Split input text if it exceeds the context length
    max_context_length = 1024  # Adjust this based on the model's actual context length
    input_chunks = split_input_text(input_text, max_context_length)
    
    print("Language:", language)

    ## Generate response for each chunk
    responses = []
    for chunk in input_chunks:
        prompt = f"Write a {language} program or function for the following requirement:\n{chunk}\n"
        response = llm(prompt)
        responses.append(response)
    
    ## Combine responses if there are multiple chunks
    final_response = "\n".join(responses)
    return final_response
