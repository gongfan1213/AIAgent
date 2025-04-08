from langchain.prompts import PromptTemplate
prompt = PromptTemplate.from_template(
    """对下面的文字进行总结:
    {output_text}
    """
)
with open("5-7Transformation.txt") as f:
    output_text = f.read()
from langchain.chains import LLMChain, SequentialChain, TransformChain
from langchain.llms import OpenAI
# 文档转换链
def transform_func(input:dict) ->dict:
    text = input["text"]
    # 对文档进行分割
    shortened_text = "\n\n".join(text.split("\n\n")[:3])
    return {"output_text":shortened_text}

tranform_chain = TransformChain(
    input_variables=["text"],
    output_variables=["output_text"],
    transform = tranform_func
)
template = """对下面的文字进行总结:
    {output_text}
    总结:"""
prompt = PromptTemplate(
    input_variables=["output_text"],
    template=template
)
print(prompt)
llm_chain = LLMChain(
    llm=OpenAI(temperature=0.7),
    prompt=prompt
)
# 使用顺序连连接起来
Sequential_chain = SimpleSequentialChain(
    chains=[tranform_chain,llm_chain],
    verbose=True
)