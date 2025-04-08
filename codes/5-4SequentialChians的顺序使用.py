# Sequential chains 支持多个链路的顺序执行的
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
llm = ChatOpenAI(temperature=0.7,model="gpt-3.5-turbo",)
# 给一段中文翻译成英文，然后进行总结摘要
# chain1
first_prompt = ChatPromptTemplate.from_template(
    "把下面内容翻译成中文:\n\n{english_text}"
)
chain_one = LLMChain(llm=llm, prompt=first_prompt,verbose=True,
output_key="chinese_Rview",
)
# chain2任务对翻译后的中文进行总结照耀Input_key是上一个的chain的output_key
chain_two =LLMChain(llm=llm,prompt=second_prompt,
verbose=True,output_key="Chinese_summary",)
# chain3任务3识别语言input_key是上一个chain的output_key
third_prompt = ChatPromptTemplate.from_template(
    "请识别下面内容的语言:\n\n{Chinese_summary}"
)
chain_three = LLMChain(llm=llm, prompt=third_prompt,verbose=True,
output_key="language",)
# chain4任务:针对摘要进行评论，使用指定语言,input_key是上一个的chain的output_key
fourth_prompt = ChatPromptTemplate.from_template(
    "请用{language}对下面内容进行恢复:\n\n{Chinese_summary}\n\n语言:{language}"
)
# overall将任务串联起来
overall_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two,chain_three,chain_four],
    verbose=True,
    input_variables=["Review"],
    output_variables=["Chinese_ Rview","Chinese_summary","language","Language",'Reply'],
)
'''
在LangChain的Sequential Chains中， input_key 和 output_key 是用于指定链之间数据传递的关键参数：

1. output_key ：
   
   - 定义当前链输出结果的键名
   - 例如在 chain_one 中， output_key="chinese_Rview" 表示第一个链的输出将以"chinese_Rview"为键存储
2. input_key ：
   
   - 指定当前链接收上一个链输出的键名
   - 虽然代码中没有明确显示，但在 chain_two 中应该有一个对应的 input_key="chinese_Rview" 来接收第一个链的输出
这种机制允许多个链按顺序执行，并将前一个链的输出作为后一个链的输入。在你的代码中：

- 第一个链( chain_one )将输入的英文文本翻译成中文，并将结果存储为"chinese_Rview"
- 第二个链( chain_two )应该接收"chinese_Rview"作为输入，进行总结，并将结果存储为"Chinese_summary"
- 第三个链将接收"Chinese_summary"作为输入，识别语言
注意：代码中缺少了 second_prompt 的定义，以及第三个链的完整定义。
'''

