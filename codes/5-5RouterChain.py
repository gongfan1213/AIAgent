from langchain.prompts import PromptTemplate
physics_template = """你是一个非常聪明的物理老师。你给出的问题是学生的问题，用非常简单的语言来回答。\n
你擅长以简洁易懂的方式回答物理问题\n
当您不hi到问题答案的时候您会坦率承认不知道\n
下面是一个问题
(input)"""
physics_prompt = PromptTemplate(
    input_variables=["input"],
    template=physics_template,
)
# 数学lian
math_template="""你是一个非常聪明的数学老师。你给出的问题是学生的问题，用非常简单的语言来回答。\n
你擅长以简洁易懂的方式回答数学问题\n
当您不hi到问题答案的时候您会坦率承认不知道\n
下面是一个问题
(input)"""
math_prompt = PromptTemplate(
    input_variables=["input"],
    template=math_template,
)

from langchain.chains import ConversationChain
from langchain.chains import LLMChain
from langchain.llms import OpenAI
prompt_infos = [
    {
        "name": "物理",
        "description": "擅长回答物理问题",
        "prompt_template": physics_prompt,
    },
    {
        "name": "数学",
        "description": "擅长回答数学问题",
        "prompt_template": math_prompt, 
    }
]
llm = OpenAI(temperature=0.7)
destination_chains ={}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    chain = LLMChain(llm=llm,prompt=prompt_template)
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["input","options"],
    )
    chain = LLMChain(llm=llm,prompt=prompt)
    destination_chains[name] = chain
default_chain = ConversationChain(llm=llm,output_key="text")

# router chain的操作
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.chains.router.llm_router import MultiPromptChain

destinations =[f"{p['name']}:{p['description']}" for p in prompt_infos]
destination_str = "\n".join(destinations)
print(destination_str)
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destination_str
)
print(router_template)
print(MULTI_PROMPT_ROUTER_TEMPLATE)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(), 
)
print(router_prompt)
router_chain = LLMRouterChain.from_llm(llm,router_prompt)
router_chain.predict(input="帮我计算一下1+1等于多少")
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True, 
)
chain.run("帮我计算一下1+1等于多少")
chain.run("两个靓丽宁翠鸟")
# 下游工具链，desintains,router_chains,defaul_chain