![image](https://github.com/user-attachments/assets/8191110f-0fca-42de-b369-333e731f0dfc)


![image](https://github.com/user-attachments/assets/252c3c5f-d474-46b3-80fc-44c8972d5245)

必须有memory

预制链，通过链式调用，扩展了大模型的api来指示下一步的操作的

# 四种基础内置链介绍和使用

LLMChain

最常用的链式

提示词模板，+（LLM/chatModes)输出格式化器（可选的）

支持多种调用方式

## 顺序链

顺序执行的链

将前一个LLM的输出作为下一个LLM的输入


![image](https://github.com/user-attachments/assets/49ddc78b-e1f6-426e-9ba8-86f6dc8534b6)


![image](https://github.com/user-attachments/assets/cd76b08c-7464-46a5-96fc-3d492396c3c9)

![image](https://github.com/user-attachments/assets/87aad869-a624-4194-b9ad-01432baed8f4)




- 链的不同调用方法
- 使用文件配置加载专用链
- 自定义自己的专用链

## LangchainHub

https://github.com/hwchase17/langchain-hub/blob/master/chains/llm-math/chain.json


```js
{
    "memory": null,
    "verbose": true,
    "llm": {
        "model_name": "text-davinci-003",
        "temperature": 0.0,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "n": 1,
        "best_of": 1,
        "request_timeout": null,
        "logit_bias": {},
        "_type": "openai"
    },
    "prompt": {
        "input_variables": [
            "question"
        ],
        "output_parser": null,
        "template": "You are GPT-3, and you can't do math.\n\nYou can do basic math, and your memorization abilities are impressive, but you can't do any complex calculations that a human could not do in their head. You also have an annoying tendency to just make up highly specific, but wrong, answers.\n\nSo we hooked you up to a Python 3 kernel, and now you can execute code. If anyone gives you a hard math problem, just use this format and we\u2019ll take care of the rest:\n\nQuestion: ${{Question with hard calculation.}}\n```python\n${{Code that prints what you need to know}}\n```\n```output\n${{Output of your code}}\n```\nAnswer: ${{Answer}}\n\nOtherwise, use this simpler format:\n\nQuestion: ${{Question without hard calculation}}\nAnswer: ${{Answer}}\n\nBegin.\n\nQuestion: What is 37593 * 67?\n\n```python\nprint(37593 * 67)\n```\n```output\n2518731\n```\nAnswer: 2518731\n\nQuestion: {question}\n",
        "template_format": "f-string",
        "_type": "prompt"
    },
    "input_key": "question",
    "output_key": "answer",
    "_type": "llm_math_chain"
}
```












