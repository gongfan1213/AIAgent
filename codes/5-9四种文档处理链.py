# stuffChain
# 最常见的文档链，将文档直接塞进prompt当中，为LLM回答问题提供上下文文档，适合小文档的场景

from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
loader = PyPDFLoader("pdf/1.pdf")
pages = loader.load_and_split()
print(len(pages))
llm = OpenAI(temperature=0.7)
print(loader.load())
prompt_template = """ 对以下文字做简洁的总结{text}
简洁的总结:"""
prompt = PromptTemplate.from_template(prompt_template)
llm =ChatOpenAI()
llm = ChatOpenAI(
    temperature =0,
    model ="gpt-3.5-turbo-16k"
)
llm_chain = LLMChain(
    llm = llm,
    prompt = prompt
)
stuff_chain = StuffDocumentsChain(
   llm_chain = llm_chain,
   document_variable_name = "text" 
)
docs =loader.load()
print(studff_chain.run(docs))
# 使用预先封装号的loader_summarize_chain
from langchain.chains.summarize import load_summarize_chain
loader = PyPDFLoader("pdf/1.pdf")
docs =loader.load()
llm = ChatOpenAI(
    temperature =0,
    model ="gpt-3.5-turbo-16k"
)
chain = load_summarize_chain(
   llm = llm,
   chain_type = "stuff",
   verbose = True
)
chain.run(docs)
# refine过程
# 通过循环引用LLM将文档不断头尾并且产生各种中间答案，适用于逻辑有上下文关联的文档的，不适合交叉引用的文档

from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchian.text_splitter import CharacterTextSplitter
loader = PyPDFLoader("pdf/1.pdf")
docs =loader.load()
text_split = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size = 1000,
    chunk_overlap = 0
) 
split_docs = text_split.split_documents(docs)
prompt_template = """
你的任务是根据下面的文本生成简洁的摘要
{text}
简洁的摘要:"""
prompt = PromptTemplate.from_template(prompt_template)
refine_template=(
    "你的任务是根据下面的文本生成简洁的摘要\n"
    "我们已经提供了一个现有的摘要:{existing_answer}\n"
    "我们有机会通过下面的一些更多的上下文完成现有的回答，仅在需要的时候使用\n"
    "-----\n"
    "{text}\n"
    "-----\n"
    "根据新的上下文完成原始的摘要\n"
    "如果新的上下文没有提供新的信息，返回原来的摘要\n"
)
refine_prompt = PromptTemplate.from_template(refine_template)
llm = ChatOpenAI(
    temperature =0,
    model ="gpt-3.5-turbo-16k"
)
chain = load_summarize_chain(
   llm = llm,
   chain_type = "refine",
   verbose = True,
   question_prompt = prompt,
   refine_prompt = refine_prompt,
   return_intermediate_steps = True, # 返回中间答案的步骤
   input_key = "documents",
   output_key = "output_text"
)
# stuff document将文档列表插入到提示词当中，适用于文档较小或者少量文档的应用
# refine documents chain
# 通过循环输入文档并且迭代更新答案来构建响应，一次只传递给LLM一个文档，适合llm上下文大小不能容纳小文档
result = chain({"documents":split_docs},return_only_outputs = True)
print(result["output_text"])
