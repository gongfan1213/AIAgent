# 自定义prompt模板
```js
##函数大师：根据函数名称，查找函数代码，并给出中文的代码说明

from langchain.prompts import StringPromptTemplate


# 定义一个简单的函数作为示例效果
def hello_world(abc):
    print("Hello, world!")
    return abc


PROMPT = """\
你是一个非常有经验和天赋的程序员，现在给你如下函数名称，你会按照如下格式，输出这段代码的名称、源代码、中文解释。
函数名称: {function_name}
源代码:
{source_code}
代码解释:
"""

import inspect


def get_source_code(function_name):
    #获得源代码
    return inspect.getsource(function_name)

#自定义的模板class
class CustmPrompt(StringPromptTemplate):

    
    def format(self, **kwargs) -> str:
        # 获得源代码
        source_code = get_source_code(kwargs["function_name"])

        # 生成提示词模板
        prompt = PROMPT.format(
            function_name=kwargs["function_name"].__name__, source_code=source_code
        )
        return prompt

a = CustmPrompt(input_variables=["function_name"])
pm = a.format(function_name=hello_world)

print(pm)

#和LLM连接起来
from langchain.llms import OpenAI
import os
api_base = os.getenv("OPENAI_PROXY")
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base
    )
msg = llm.predict(pm)
print(msg)
```

- 字符串模板-promptTemplate
- 对话模板-ChatPromptTemplate
- 自定义模板
- F-string，jinji2与组合模板
#### 使用jinji2与f-string来实现提示词模板格式化
```js
##f-string是python内置的一种模板引擎
from langchain.prompts import PromptTemplate

fstring_template = """
给我讲一个关于{name}的{what}故事
"""

prompt = PromptTemplate.from_template(fstring_template)

prompt.format(name="翠花", what="悲伤")
```
# jin2

```js
##Jinja2是一个灵活、高效的Python模板引擎，可以方便地生成各种标记格式的文档。
from langchain.prompts import PromptTemplate

jinja2_template = "给我讲一个关于{{name}}的{{what}}故事"
prompt = PromptTemplate.from_template(jinja2_template, template_format="jinja2")

prompt.format(name="狗剩", what="高兴")
```
# 组合模板

- Final prompt最终返回的提示词模板
- PiplelinePrompt组成提示词管道模板

  - 三层提示词的设计
 
  ```js
  # Final Prompt由一系列变量构成
full_template = """{Character}
{behavior}
{prohibit}"""
full_prompt = PromptTemplate.from_template(full_template)
```

```js
input_prompts = [
    ("Character", Character_prompt),
    ("behavior", behavior_prompt),
    ("prohibit", prohibit_prompt)
]
pipeline_prompt = PipelinePromptTemplate(final_prompt=full_prompt, pipeline_prompts=input_prompts)
```

# 序列化和使用文件来管理提示词的模板

- 便于共享
- 便于版本管理
- 便于存储
- 支持常见的版本格式json/yarml/json

- simple_prompt.yaml

  ```js
  ——type: prompt
  _uboyr_varibale:[]
  ```

  - json
  - 格式的

    ```js
    {
    "_type":"prompt",
    ```

    - from langchain.prompts import load_prompt
    - prompt =load_prompt("simple_prompt.yaml")
      


