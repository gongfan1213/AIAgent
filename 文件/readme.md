

### 【注意】 由于很多同学获取LLM资源有困难，课程仓库更新了如何使用阿里千问的演示代码

- 具体使用见：**使用阿里千问API.ipynb**
- 无需科学上网 
- 能力相当于gpt3.5
- 只要不是很复杂的任务都可以胜任

# AI Agent智能应用从0到1定制开发课程配套代码
* **本代码请配合视频课程食用**
* **代码示例来自于langchain官方示例+自研开发**
* **代码可本地运行**

## 文件说明
- .ipynb文件都是配套视频的演示代码
- 虚拟项目目录为实战代码,其中bot为anget+电报机器人，shuziren为angent+avatar形象数字人
- openai.env是配置LLM的key和代理url的地方


## 运行环境与推荐IDE

- 推荐macos+vscode
- python版本3.11.4,最好不要使用低于这个版本的python
- 推荐使用vscode来运行所有代码

## 关于LLM资源

- AI Agent应用需要有LLM资源，在课程后面章节有介绍获取方式
- 推荐使用Openai api
- 国外闭源大模型API>国内闭源大模型API>gpu云自建LLM>本机电脑运行LLM，优先级依次降低，**能搞到openai资源尽量使用openai!!**
- agent因为要自我决策和执行，所以对LLM要求比较高，本机运行的开源LLM，尤其参数很低的那种，就不要想了，跑不起来，只能做类似chains这种低级点的任务
- langchain社区集成了非常多的LLM资源，不同LLM资源的支持力度不同,具体支持力度可参考：[https://python.langchain.com/docs/integrations/llms/](https://python.langchain.com/docs/integrations/llms/)
- 国产LLM推荐使用阿里的Tongyi API、百度的QianfanLLMEndpoint API
- 租赁GPU服务器来跑，推荐使用autodl，可以跑BaiChuan或智普的chatGLM6B
- Openai已经block了大陆IP，如果你有openai sky那么一定要科学上网运行
- 如果想图省事，可以搜有很多的做国外大模型key代理的站点，注意不是卖十几块钱的那种账号的，那种都是割韭菜，找代理站，用多少充值多少，我项目里用的是ai-yyds.com这一家，你可以搜索有很多。
- anyweay 想要开发AI应用，**大模型资源投入是绕不过去的**，哪怕你有4090卡，目前实际工业生产的时候，也是根本不够用的！
- 不怕麻烦的可以参考这个文章[中国用户如何注册OpenAI（ChatGPT）、获取API Key并搭建API反向代理服务](https://www.typemylife.com/how-to-register-openai-chatgpt-get-api-key-create-api-proxy-in-china/)
- 怕麻烦的可以自行google openai 代理站，有很多可以使用的，比较简单，我个人使用的是ai-yyds.com 70块钱十几万token，足够课程学习。

## 关于演示

- 本课程虚拟项目为python后台+电报客户端，另外有个人开发的商业版本，是web版技术栈，不在本课程内容包里：vue+node+python,可以在线参考体验：[https://shensuan.me](https://shensuan.me)

## 关于其他资源准备

- Agent应用里的工具，大部分是以API形式接入AI的，所以当你开发相关工具的时候，是需要相应准备相关API的key
- langchain已支持的工具列表:[https://python.langchain.com/docs/integrations/tools](https://python.langchain.com/docs/integrations/tools)

## 关于自己运行报错

- 首先检查你的本地环境，包括python版本以及openai、langchain的版本
- AI领域迭代速度非常快，尤其openai，所以在课程路程期间，会有一些类似api被遗弃，或某些模型不支持的现象，遇到问题可以群内问，我看到会回答，另外也可以自行查阅官网(**最建议的是购买一个微软的coplit助手，以插件安装到vscode上，非常好用，效率杠杠的**)

## 目前已知的一些问题和解法：
1. openai模型无法使用，报错之类:openai官方已经遗弃了text-davinci-003模型，当使用OpenAI接口的时候，如果遇到相关错误，可以先手动指定model为gpt-3.5-trubo-instruct。
2. 如遇到类似openai.ChatCompletion之类的报错，先尝试把openai版本回滚到老版本：pip install --upgrade openai==0.27.8
3. penai已经弃用了 V1/engines/ ，但是老的版本langchain里依然会调用，这里要么把openai和langchain版本都更新为最新版本，要么可以自行寻找langchain相关包地址，修改这里的代码[https://github.com/hwchase17/langchain/pull/6573](https://github.com/hwchase17/langchain/pull/6573)

```
#langchain/embeddings/openai.py 第59行：加入以下代码：
#改为使用model以调用新API
    if "engine" in kwargs:
        kwargs["model"] = kwargs.pop("engine")
    #防止传入的input是列表
    if isinstance(kwargs.get("input"), list):
        kwargs["input"] = kwargs["input"][0]
```
4.把openai和langchain都升级到最新版本方法：
```
！pip uninstall langchain -y
! pip uninstall openai -y 
! pip install --upgrade langchain
! pip install --upgrade openai
```
查看版本号的方法：
```
!pip show langchain
!pip show openai
```
5.关于regex_parse报错的问题，因为课程期间langchain发了大版本，使用load_prompt来加载文件的时候，去掉了有安全隐患的regex_parse，只支持字符串。这里如果是学习，建议langchain包版本保持在0.0.0279,就可以正常使用。如果是安装最新版本的，load_prompt只支持str类型的output，可以使用最新的Partial prompt templates来实现对提示词模版的解析：
```
from datetime import datetime
#可以在自定义函数里实现各种解析，包括正则
def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective", "date"],
)
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(adjective="funny"))
```

6.关于OPENAI_PROXY如何配置，配套演示代码中的openai.env就是项目的配置文件，在这个文件里将OPENAI_API_BASE修改为对应的LLM API代理站点地址即可。

7.关于4-3 jq包在windows平台安装的问题，windows不支持jq包，建议把labgchain升级到最新版本，参考代码库：https://git.imooc.com/coding-822/kecheng 里的说明，或者参考官方的git里相似问题解法：https://github.com/langchain-ai/langchain/issues/4396

8.关于产业结构的高清图，见仓库内产业.png。
