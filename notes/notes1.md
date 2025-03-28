- 不要随意在本笔记本内安装包操作！！
- 该服务器在海外，速度没那么快！！有梯子可以开梯子！
- 慕课的仓库地址：https://git.imooc.com/coding-822/kecheng
- 如果你还是想在本地安装体验，可以先搜索下python相关基础，比如pyenv的安装，这些不在本课程范围内
- 本服务器运行至课程下架为止

### 资源
- 模型选择：openai API > 百度&千问API > 开源大模型
- 推荐使用openai api，如何获取请自行搜索，推荐使用低伦理，几十块钱购买的token，足够使用，LLM开发烧token是不可避免的。
- 如果不会科学上网也不想使用openai，可以使用阿里千问API，我测试过可以使用，详见使用阿里千问API.ipynb
- 课程里还涉及到注册一些其他平台的API，比如搜索工具serpapi：https://serpapi.com/manage-api-key，比如微软云、elevens等，示例里的key已经失效，需要你们自行注册申请！
- 最佳实践那章需要自行架设AutoDL的GPU服务，以及自己在本机上通过Ollama来体验！

### 使用
- 请将old-image openai.env以及new-image openai.env处修改为您自己的key和proxy地址！[重要]
- 推荐使用chrome浏览器
- 笔记本内点击代码块，点击三角箭头是运行；点击快进箭头是全部重新运行；

### 目录
- 【注意下方链接失效，访问http://149.28.145.211-old-image是前7个演示，new-image是后面的演示】
- 第一个实例http://149.28.145.211:8888/notebooks/(1)%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%AE%9E%E4%BE%8B.ipynb
- prompt模板http://149.28.145.211:8888/notebooks/(2)prompt%E6%A8%A1%E6%9D%BF.ipynb 

- Langchain是大模型的粘合剂，是AI应用开发的重要框架
- Langchain是能连接大模型并且为模型增强各种能力的
- Langchain适用于目前的AI应用开发，代理机器人的搭建，
 
# 打造自己的prompt
- 打造io接口的介绍
- 基于prompts模板的输入工程
- Langchain的核心部件的LLM的使用
# 模型IO： 大语言模型的交互接口

![image](https://github.com/user-attachments/assets/a4e95818-4239-4bd2-b9c3-bb1cf2ef3353)

# prompts模板：更加高级和灵活的提示

![image](https://github.com/user-attachments/assets/0f2dfade-e00b-468c-b1b7-904ef94fb68c)

提示词模板

1.将提示词提炼成模板

2.实现提示词的复用，版本管理，动态变化等等。


-  引入包，PromptTemplate
-  
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
