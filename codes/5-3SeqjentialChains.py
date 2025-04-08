# 顺序链
# simpleSequentialChain只支持固定的链路
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
chat_model = ChatOpenAI(temperature=0.7
,model="gpt-3.5-turbo",)
# chain1
first_prompt = ChatPromptTemplate.from_template(
    "帮我给{product}的公司起一个响亮容易记忆的名字"
)
chain_one = LLMChain(llm=chat_model,
prompt=first_prompt,verbose=True,)
# chain2
second_prompt = ChatPromptTemplate.from_template(
    "用5个此来描述一下这个公司的名字:{company_name} "
)
chain_two = LLMChain(llm=chat_model,
prompt=second_prompt,verbose=True,)

overall_chain = SimpleSequentialChain(chains=[chain_one, chain_two],
verbose=True)
overall_chain.run("AI研习社")
