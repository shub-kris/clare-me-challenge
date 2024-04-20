# Hiring Challenge for Clare

### About Clare

Clare is a Conversational AI that communicates with our users through WhatsApp and calls in order to provide personalized mental health support. 

While a user has **WhatsApp** conversations, Clare needs to distinguish between different conversation scenarios:

1. **Regular conversations** (mental health conversations, exercises, etc.)
2. **Product-related conversations** (e.g. how Clare works, if Clare calls via phone or WhatsApp, etc.)
3. **Subscription-related conversations** (Clare fetches the users info from a database and responds with specific user info, e.g. how long their trial is still running)
4. **Suicide** (if a user gives any form of indication that he is actively considering or planning suicide we need to detect this and place the user in a clinically approved conversational flow that is able to handle this situation)
5. **Non-mental health topics** (if a user asks Clare about her favorite movies we firmly but kindly nudge them that this is a place to talk about mental health)

For each scenario, we have a different agent, e.g. one for regular conversations, one for product-related questions, etc.. 

### Your Mission: Part 1

Implement a Python ML service that we can call from our NodeJS/TypeScript backend. The service will take as **input** a piece of conversation and it will **output** an integer indicating the scenario number (e.g. 1 for regular conversations, 2 for product-related ones, etc.).

b. Please guarantee the following:

- **Please make assumptions** where you see fit
- If you are looking for actual training data, **consider creating it synthetically**
- Pick a ML model that you think will **perform well** on this task
- Think about how you can measure the **performance** of this model
- Follow **software development best practices** (based on how you define them)

### Your Mission: Part 2

For our calls, we want to be **flexibly transition between different stages** of a conversation. You can imagine each conversation having a set **number of stages** (say, 5), e.g. an introduction, a mood-check, a reflection, an exercise, and a wrap-up. 

- How would you design a system that is able to **intelligently decide whether it should progress to the next stage** (or back to previous stages)?
- How could the system **learn** to do these decisions better over time?
- How would you leverage **memory** in these scenarios?
- What other thoughts do you have to **improve** the system?

**Note:**

- **This is an opportunity to think big**. Please see the questions as indications of what we are looking for rather than a fixed number of answers we are expecting.
- We really want to see how ***you*** think about the future for Clare and how you would approach designing an intelligent and empathetic AI system.
- The level of detail we are looking for is **high-level** but we are happy to drill down into specific aspects. (we are curious, too!)
- You can approach this task in any way you want. We will ask you to share the outcome of this, so we recommend **some form of** **visualization**.