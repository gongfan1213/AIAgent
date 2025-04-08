from langchain.chains import load_chain
chain = load_chain("lc://chains/llm-math/chain.json")
print(chain.run("2+6等于几"))
chain = load_chain("lc://chains/hello-world/chain.yaml")
print(chain.run("2+6等于几"))
# 自定义CustomChain
# 当通用联不满足的时候，可以自行构建来实现特定的目的的
from typing import Dict,List,Any,Optional
from langchain.callbacks.manager import (
    CallbackManagerFormChainRun
)
from langchain.chains.base import Chain
from langchian.prompts.base import BasePromptTemplate
from langchain.base_language import BaseLanguageModel
class wiki_article_chain(Chain):
    """开发一个wiki文章生成器"""
    prompt:BasePromptTemplate
    llm:BaseLanguageModel
    output_key:str = "text"
    @property
    def input_keys(self) -> List[str]:
        """将返回prompt的所需要的所有的键"""
        return self.prompt.input_variables
    @property
    def output_keys(self) -> List[str]:
        """将返回最终text的键"""
        return [self.output_key]
    def _call(
        self,
        inputs: Dict[str,Any],
        run_manager: Optional[CallbackManagerFormChainRun] = None, 
    ) -> Dict[str,Any]:
        """运行键"""
        prompt_value = self.prompt.format_prompt(**inputs)
        response = self.llm.generate_prompt(
            [prompt_value],callbacks=run_manager.get_child() if run_manager else None
        )
        if run_manager:
            run_manager.on_text("wiki article is written")
        return {self.output_key:response.generations[0][0].text}
    @property
    def _chain_type(self) -> str:
        """返回chain的类型"""
        return "wiki_article_chain"


from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
llm = ChatOpenAI(temperature=0.7)
chain = wiki_article_chain(
    prompt=PromptTemplate.from_template(
        template="write a wiki article about {topic}",
        input_variables=["topic","length"],
        output_variables=["text"],
    ),
    llm=ChatOpenAI(temperature=0.7),
)

result =  chain.run(topic="AI研习社",length="1000")