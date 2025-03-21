# LangChain提示模板类详解

LangChain提供了几个用于构建和管理提示模板的重要类，下面我将详细介绍每一个：

## 1. PromptTemplate

`PromptTemplate`是LangChain中最基础的提示模板类，用于创建包含变量的模板字符串。

```python
from langchain.prompts import PromptTemplate

# 创建一个简单的提示模板
template = "请为我写一篇关于{topic}的{word_count}字文章，风格要{style}"
prompt = PromptTemplate(
    input_variables=["topic", "word_count", "style"],
    template=template
)

# 使用模板生成提示
formatted_prompt = prompt.format(
    topic="人工智能",
    word_count="500",
    style="通俗易懂"
)
print(formatted_prompt)
```

**主要特点**：
- 定义包含占位符的模板字符串
- 指定需要填充的变量名
- 通过`format()`方法填充变量生成最终提示

## 2. FewShotPromptTemplate

`FewShotPromptTemplate`用于构建包含少量示例的提示模板，适用于少样本学习场景。

```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# 定义示例格式
example_formatter_template = """
输入: {input}
输出: {output}
"""
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_formatter_template
)

# 准备示例
examples = [
    {"input": "把这个句子翻译成英文：我喜欢编程", "output": "Translate this sentence to English: I like programming"},
    {"input": "这段代码有什么问题：print(1/0)", "output": "What's wrong with this code: print(1/0)"}
]

# 创建少样本提示模板
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="以下是关于任务的一些例子：",
    suffix="输入: {input}\n输出:",
    input_variables=["input"],
    example_separator="\n\n"
)

# 使用模板
print(few_shot_prompt.format(input="分析这个句子的情感：这部电影太棒了"))
```

**主要特点**：
- 包含一组示例（examples）
- 使用示例格式化器（example_prompt）定义每个示例的格式
- 可以设置前缀（prefix）和后缀（suffix）
- 可以自定义示例之间的分隔符（example_separator）

## 3. LengthBasedExampleSelector

`LengthBasedExampleSelector`是一个示例选择器，根据输入长度动态选择合适数量的示例，避免超出模型的最大token限制。

```python
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# 定义示例格式
example_formatter_template = """
用户: {question}
AI助手: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template=example_formatter_template
)

# 准备更多示例
examples = [
    {"question": "如何学习Python？", "answer": "可以从基础语法开始，然后做一些小项目..."},
    {"question": "什么是机器学习？", "answer": "机器学习是人工智能的一个分支，它使计算机能够从数据中学习..."},
    {"question": "推荐一本编程书籍", "answer": "《Clean Code》是一本非常好的关于代码质量的书..."},
    # 更多示例...
]

# 创建基于长度的示例选择器
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=1000  # 最大长度限制
)

# 创建使用选择器的少样本提示模板
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,  # 使用选择器而不是固定示例
    example_prompt=example_prompt,
    prefix="你是一个有帮助的AI助手。以下是一些示例对话：",
    suffix="用户: {input}\nAI助手:",
    input_variables=["input"]
)

# 使用动态模板
short_input = "天气怎么样？"
print(dynamic_prompt.format(input=short_input))  # 可能包含所有示例

long_input = "请详细解释量子计算的原理，包括量子比特、量子纠缠和量子算法..." * 5
print(dynamic_prompt.format(input=long_input))  # 可能只包含部分示例
```

**主要特点**：
- 根据输入长度动态选择示例数量
- 设置最大长度限制（max_length）
- 可以与FewShotPromptTemplate结合使用
- 有助于避免超出模型的上下文窗口限制

## 实际应用场景

1. **PromptTemplate**：适用于简单的模板化提示，如问答、翻译等基础任务。

2. **FewShotPromptTemplate**：适用于需要通过示例引导模型理解特定任务格式的场景，如特定格式的文本生成、自定义分类等。

3. **LengthBasedExampleSelector**：适用于处理变长输入，需要动态调整示例数量的场景，特别是在处理长文本或复杂任务时。

这些类可以组合使用，构建出复杂而灵活的提示系统，帮助开发者更好地控制大语言模型的输出。
