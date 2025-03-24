# RAG检索增强生成

Retrieval-Augmented Generation(RAG)检索增强生成

![image](https://github.com/user-attachments/assets/81012d79-c224-49cd-b5cf-0881094332e3)

为LLM提供了来自外部知识源的额外的信息的概念，这允许他们生成更加准确的和有上下文的答案，同时减少幻觉

1.检索外部相似搜索

2.增强。提示词更新

3.生成：更详细的提示词输入llm

# Langchain当中的RAG的实现

![image](https://github.com/user-attachments/assets/773b0a99-a0e9-4924-97a7-881dc8d9b12c)

各种文档，各种loader，文本切片，嵌入向量化，向量存储，各种检索链

# loader让大模型具备实时学习能力

csv loader

filedirectory

html loader

json loader

markdown loader

pdf loader

UnstructedHTMLLoader代码和文本全部加载进来了的

BSHTMLLoader

file_path = "simple_prompt.json",jq_schema=".template",text_content=True
选择器


# langchain中文档转换

文档切割器和按照字符分割

代码文档分割器

按照token分割文档

文档总结，精炼，翻译

做成结构化的数据的，按照token分割文档的

chunk_size=50,#切分的文本块大小，一般通过长度函数计算

    chunk_overlap=20,#切分的文本块重叠大小，一般通过长度函数计算
    
    length_function=len,#长度函数,也可以传递tokenize函数
    
    add_start_index=True,#是否添加起始索引


# 如何处理长文本切分信息的丢失

![image](https://github.com/user-attachments/assets/bf5062c5-d2b3-485e-b71a-e70dc2bbb0ce)

# langchain当中的rag实现

![image](https://github.com/user-attachments/assets/c8ba0272-55db-4684-b83f-17b793f51b17)

# 文本向量量化

Embedding嵌入可以让一组文本或者一段话以向量来表示，从而可以让我们在向量空间当中进行语义搜索之类的操作，从而大幅提升学习能力

embedding document

embedding query

嵌入向量缓存


