## Design a System Architecture to transition between different stages of a conversation

You can find an architecture diagram  below:

![Alt text](image.png)


### Introduction
- Any user interacts with the system by sending a message through the Chat Interface (UI). The Chat interface then passes this message to the backend server. The backend server interacts with different components to generate a response. The response is then sent back to the Chat Interface, which displays the response to the user.

- At the core of the system is the Agent, an AI Engine that has access to tools like Conversation Stage Classifier, History (Memory) and Response Generator. The Agent utilizes these tools to generate the response. The response is then sent back to the Chat Interface, which displays the response to the user.

- Through the UI, the user can provide feedback on the response. The feedback is logged in the Logging component. The feedback data is then used to train and fine-tune the Agent to improve the response generation over time.

### Components 
- Agent: It is the core component of the system. The Agent gets to decide which tool to utilize at a certain time to generate the response. 

- Logging: The Logging component logs all the messages and responses in a database or any other kind of memoery (discussed in section Memory Management). This is useful for debugging and monitoring the performance of the Chatbot. The Logging component can also be used to collect feedback from the users to improve the Chatbot.

- Conversation Stage Classifier: The Conversation Stage Classifier classifies the message into one of the conversation stages. The Conversation Stage Classifier uses a Deep Learning model(LLM) to classify the message into one of the conversation stages.

- Response Generator: It is a Large Language Model (LLM) that generates the response based on stage, query and context. The Response Generator can also use the context from the previous messages to generate a more coherent response. 


### Memory Management
As we know Large Language Models are stateless and do not have memory. So, we need to store the history in order to make more coherent responses. There are multiple ways to store the history. Some of them are:

- BufferMemory: We can store the history in a buffer memory. The buffer memory can store the messages in the conversation. The Language Model can then query this buffer memory to get the context and generate the response. The problem is it can only store a limited number of messages and the context is lost after the buffer is full.

- BufferMemory with Fixed Size: We can store the history in a buffer memory with a fixed size. The buffer memory can store the most recent `n` messages in the conversation. The problem is it can only store a limited number of messages and the context is lost after the buffer is full.

- SummaryMemory: We can store the history in a summary memory. The summary memory can store the summary of the conversation. The problem is it while creating the summary, some context is lost. Another possibility is storing the summary of only last `n` messages.

- Vector Database: Here, we can store everything in a database like PostGreSQL, and others etc. It is the most stable and long term storage way to store the history. It can also help to store contexts across sessions. The top `n` relevant context can be retrieved from the database and passed to the Language Model to generate the response. 


### Learning from Feedback to improve the Chatbot

- Collect Feedback: After each interaction, provide users with the option to rate the system's response as good or bad, or on a numerical scale. You might also consider allowing users to leave comments for more detailed feedback. We will be logging the (query, response, feedback) in a database or with other tools like LangSmith that store each and every interaction with the LLM. 

- Train with Feedback: Use the feedback data to train and fine-tune your agent aka LLM. One leverage techniques like RLHF (Reinforcement Learning with Human Feedback) to train the LLM. The model is rewarded for responses that received good ratings and penalized for those that received poor ratings. Over time, this helps the chatbot to "learn" to give more responses that are similar to those rated well, and fewer responses similar to those rated poorly. 

- Iterate and Improve: Continuously iterate on this process. The more feedback data you collect and incorporate into your training process, the better your chatbot will perform. 

### Other Thoughts to improve the Chatbot