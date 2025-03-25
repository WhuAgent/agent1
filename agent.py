from agent_network.base import BaseAgent
import agent_network.utils.storage.oss as oss


class Agent1(BaseAgent):
    def __init__(self, graph, config, logger):
        super().__init__(graph, config, logger)

    def forward(self, message, **kwargs):
        messages = []
        self.add_message("user", f"task: {kwargs['task']}", messages)
        response = self.chat_llm(messages)
        print('response: ' + response.content)
        results = {
            "result": response.content,
        }
        return results


class Agent2(BaseAgent):
    def __init__(self, graph, config, logger):
        super().__init__(graph, config, logger)

    def forward(self, message, **kwargs):
        # messages = []
        # self.add_message("user", f"task: {kwargs['task']}", messages)
        url = kwargs['url']
        content = oss.download_file(url)
        # response = self.chat_llm(messages)
        print('file content: ' + content)
        results = {
            "content": content,
        }
        return results
