#最常用的链
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.7)
prompt_template ="帮我给{product}像三个可以注册的域名"
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template)
,verbose=True,# 是否开启日志

)

llm_chain({"product":"ai研习社"})

