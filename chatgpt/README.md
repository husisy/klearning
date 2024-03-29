# course

1. link
   * [hkust/GenAI-workshop](https://libguides.hkust.edu.hk/AI-tools-literature-review/overview)

## PROMPT example

`%EOL%` is the end of line, `%BOL%` is the beginning of line

1. `suggest one name for a horse`
2. `suggest one name for a black horse`
3. `suggest three names for a horse that is a superhero`
4. see code block below

```text
Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: Horse
Names:
```

classfication

```text
Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: I loved the new Batman movie!
Sentiment:
```

```text
Classify the sentiment in these tweets:

1. "I can't stand homework"
2. "This sucks. I'm bored 😠"
3. "I can't wait for Halloween!!!"
4. "My cat is adorable ❤️❤️"
5. "I hate chocolate"

Tweet sentiment ratings:
```

generation

```text
Brainstorm some ideas combining VR and fitness:
```

conversation

1. tell the API the intent but we also tell it how to behave
2. give the API an identity

```text
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
Human:%EOL%

%BOL%Could you help me find a good restaurant near me?
AI: Absolutely! What type of cuisine are you looking for?
```

```text
Marv is a chatbot that reluctantly answers questions with sarcastic responses:

You: How many pounds are in a kilogram?
Marv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.
You: What does HTML stand for?
Marv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.
You: When did the first airplane fly?
Marv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.
You: What is the meaning of life?
Marv: I’m not sure. I’ll ask my friend Google.
You: What time is it?
Marv: %EOL%

%BOL%It's always time to ask better questions.
```

## DeepLearningAI/ChatGPT

[link](https://learn.deeplearning.ai/chatgpt-prompt-eng)

1. two types of large language models (LLM)
   * base LLM: predict next word, based on text training data
   * instruction tuned LLM: fine-tune on instructions and good attempts at following instructions. reinforcement learning with human feedback (RLHF)
2. principle
   * write clear and specific instructions. "clear" is NOT "short"
   * give the model time to think
3. tactic (principle 1)
   * use delimiter to clearly indicate distinct parts of the input
     * e.g.: triple quotes `"""`, triple backticks (escaped in MarkDown), triple dashes `---`, angle brackets `<>`, xml tags `<tag></tag>`
     * avoiding prompt injections
   * ask for structured output: html, json
   * check whether conditions are satisfied: check assumptions required to do the task
   * few-shot prompting: give successful examples of completing tasks, then ask model to perform the task
4. tactic (principle 2)
   * specify the steps to complete a task
   * instruct the mode lto work out its own solution before rushing to a conclusion
5. (model limitations) hallucination: make statements that sound plausible but are not true
   * reducing hallucinations: first find relevant information then asswer the question based on the relevant information
6. iterative prompt development
   * idea
   * implementation (code/data/prompt)
   * experimental result
   * error analysis
7. prompt guidelines
   * be clear and specific
   * analyze why result does not give desired output
   * refine the idea and the prompt
   * repeat
8. iterative process
   * try something
   * analyze where the result does not give what you want
   * clarify instructions, give more time to think
   * refine prompts with a batch of examples
9. summarize
   * summarize with a word / sentence / character limit
   * summarize with a focus on xxx
   * try 'extract' instead of 'summarize'
   * summarize multiple product reviews
10. inferring
    * sentiment: positive, negative
    * identify types of emotions
    * identify anger
    * extract infromation
    * inferring topics
    * determining certain topics
11. transforming
    * translation
    * universal translator
    * tone transformation
    * format conversion
    * spellcheck/grammar check
12. expanding
    * `sign the email as "AI customer agent"`
13. `temperature`
    * `temperature=0`: for tasks that require reliability, predictability
    * larger `temperature`: for tasks that require variety
14. chatbot
    * [holoviz/panel/documentation](https://panel.holoviz.org/reference/widgets/TextInput.html) [github](https://github.com/holoviz/panel)

## coursera/ADA

1. link
   * [coursera-link](https://www.coursera.org/learn/chatgpt-advanced-data-analysis/home/welcome) chatgpt advanced data analysis
   * [coursera-link](https://www.coursera.org/learn/prompt-engineering) prompt engineering for chatgpt
   * [arxiv-link](https://arxiv.org/abs/2302.11382) A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT
2. concept
   * advanced data analysis, code interpreter
   * ADA: advanced data analysis
3. prompt
   * Ex1: extract this document to plain text and then read the document
   * Ex2: re-read the text
   * Ex3: continue/proceed
4. prompt example: asking questions in a small document
   * 00: extract this document to plain text and then read the document and tell me all the pieces of information that it is requesting
   * 01: reread the text and break down the questions into the smallest level of detail. Provide the identifier for each question in the document or `[question-name]` if none exists
   * 02: continue (proceed)
5. prompt example: working with structure data
   * 00: read and explain the structure of the data in this document
   * 01: create a atable showing graduate and undergraduate enrollment by year with separate rows for each
   * 02: visualize each of these as separate series
   * 03: flip the chart so it increases in time as it moves to the right
   * 04: create a table that shows the ratio of graduate to undergraduate students over time as a decimal (graduate / undergraduate) and create a table displaying the resutls
   * 05: what other data is in the original dataset that correlates with this growth in the graduate population relative to the undergraduate population
   * 06: what about grants and contracts
6. prompt example: wroking with media
   * 00: extract 10 frames from this video evenly spaced spart
   * 01: display the images
   * 02: resize each image (maintain the aspect ratio) to 300px wide
   * 03: convert all of the images to gray scale and increase the contrast `30%`
   * 04: combine the images into an animated gif that flips to the next image at one second interval
   * 05: turn the individual images into a powerpoint presentation with one image per slide
   * 06: catalog all of the images in a CSV file with the name of the image, the name of the movie file that the image was extracted from, the time in the movie that it was extracted from, and the operations applied to it
7. prompt example: zip files for automation
   * 00： please make these images much more stylized by dramatically increasing the contrast and saturation
   * 01: zip up the files so that i can download them
   * 02: I need your help organizing the files in the uploaded zip. I want you to help figure out what is in them by opening and reading each one to create a summary. I want you to propose a folder structure that would better organize the files. I wnat you to propose better names for each file using just a-z and 0-9 (keep extensions). When you have all this done, show me your proposed folder structure and names
   * 03: can you try an alternatate method to figure out what is in the other category? try other ways fo getting text from the PDFs, Look at the file names. Keep trying and do your best
   * 04: this looks good. create a zip file with the files in this structure so that i can download it
8. prompt example: turning conversations into software utilities
   * **WARNING**: proceed only when you can understand code or you have some programming friends
   * 00: turn this process into a python program that i can download and run on my computer and provide the paths to the documents as command-line arguments. Zip up the program for me to download
9. working with small documents
   * structured or unstructured
   * size of unstructured documents: almost the size of a single message
10. getting information into the conversation
    * if you can see the information that it's going to build off of in the conversation, you are much more likely to be successful
    * reading and re-reading the text
    * build search index
    * 00: using your index, read the policies related to staying in an AirBnB and tell me if i can get reimbursed for this if the cost is less than the average hotel in the same city

week 3

1. what types of problems are good fits for ADA
   * easy to check if the solution is correct and errors won't create new problems
     * good: brainstorm hard questions that might be asked about the presentation
     * bad: determine whether or not a human gets a loan
   * A partial or flawed solution to the problem has value
     * good: create questions related to a document, spot conflicts in decision made in different meetings, provide a second check that didn't previously exist on a human decision
   * the solution to the problem will support your creativity and thought, not doing less thinking
     * good: automate tedious tasks
     * bad: use ADA to cheat on an exam
2. guideline
   * aid human coordination
   * reduce tedium to provide more time fore creative thought and problem solving
   * help spur better problem solving and creativity
   * provide a safety net
   * allow great ideas to scale faster
3. aid human coordination
   * 00: act as my personal asistent, read the following meeting transcript and provide me a summary of the key points of discussion
   * 01: list any potential ambiguities in the plan that the team should address
   * 02: who should follow up on each of the listed ambiguities
   * 03: a second team working on logistics for the workshops just met. These are their meeting notes. Please point out any potential conflicts in decisions made by this team and the other team
4. cut tedious tasks through automation, freeing time for creative thought and problem-solving
   * 00: this is the list of people that registered for my workshop on prompt engineering and chatgpt. describe the data in this file
   * 01: please create a bar chart showing total registrations by department
   * 02: it looks like there is a lot of overlap between departments, alternate spellings, etc. Can you list all the departments and then do some intelligent grouping of them (e.g. "Owen" and "Owen XYZ", "dmbi" and "DMBI" and "Bioinformatics") so that alternate names or variations of names end up in the same group? show me the list after grouping
   * 03: look again at your grouping. critique your work. come up with a plan to fix any issues you see and then execute that plan
   * 04: the only last issues i see are "VUIT" vs "VU IT" and "OVPRI" vs. "Vanderbilt OVPRI", can you spot any other issues like this? do your work without python
   * 05: manually create a mapping of all the original departments in the registration to one of these sanitized departments
   * 06: create a CSV file that has this mapping. you should have a column for "original department" and "final department"
   * 07: take the original CSV with registrations, go through each registration, and replace the deparmtent by looking up the "final department" that corresponds to the "original deparmtent" that has the same value in the file that you just created
   * 08: can you tell me the mapping of departments to schools within Vanderbilt University?
   * 09: the registration had "how are you using ChatGPT, bard, bing, etc.?" as a question. Can you turn this into a list of types of usage and then group the responses underneath your types?
   * 10: create three more possible groupings and a visualization for each grouping
   * 11: combine three of these into an interesting 3D visualization
   * 12: can you abbreviate all of the labels so they don't overp / make the chart hard to read
5. help provide a safety net
   * 00: read each page of the attached business expense policy and see if the attached receipt complies with it
   * 01: please proceed for all pages and then determine if the receipt complies with all relevant policies
   * 02: read the provided receipt (try multiple pdf libraries like pdfplumber) and tell me if it complies with travel policy. don't list what is on the receipt, just if it complies and why or why not.
   * 03: please analyze the attached receipt and let me know if it complies
6. inspire better problem solving and creativity
   * 00: read and summarize the key points on each slide
   * 01: proceed
   * 02: act as a skeptic of everything i say in this presentation. find flaws in my assumption assertions, and other key points and then generate 10 hard questions for me
   * 03: generate three different possible ways of addressing each of these questions
   * 04: please think of possible visualizations that could aid in addressing each of these questions. Generate each visualization you come up with using Python
   * 05: figure out a way to draw a diagram that can be generated, even if it is more of a textual, directed graph, etc.
   * 06: the slides are for a workshop i am hosting for faculty. i don't want to spend any money, but i need to have a mechanism for managing registrations and sending out email notifications with the zoom link for the workshop. give me three different approachs for this process and reference specific tools (e.g., google forms) that i could use and the workflow between them
   * 07: these are the people that registered for my workshop. don't list any names of people, just look at their departments and ways they are using generative AI, and then give me some ideas for topics, questions, or other things they will care about related to my slides.
   * 08: i am going to create customized post-workshop emails for every attendee. I wnat you to create a list of interesting ChatGPT prompts and ways of combining LLMs with each discipline or department. each department needs at least one every interesting and creative prompt targeting the departments' discipline and one idea of how to apply LLM in the discipline. List all departments and the prompts / ideas beneath them
   * 09: turn these into a CSV that has columns for department, email, addresses, prompts / ideas for department so that i can easily do a mail merge that creates a custom email with these interesting ideas for each participant based on their department
   * 10: now, i need you to generate three exciting post-workshop email templates that can include these ideas. also, try to summarize what we explored in the workshop
   * 11: come up with four interesting interdisciplinary collaborations that could be formed amongst the departments that involve LLMs, use your list of departments, ideas and the current usege of LLMs listed in the registrations to inspire you
7. enable great ideas to scale faster

## coursera / ChatGPT

[coursera-link](https://www.coursera.org/learn/prompt-engineering/home/welcome) Prompt Engineering for ChatGPT

[arxiv-link](https://arxiv.org/abs/2302.11382) A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT

1. ChatGPT is
   * to give your ideas form, thoughts, realization
   * to explore different concepts and be able to refine them over interaction
   * **NOY** a tool to write essay or answer questions
   * 00: please create a meal plan for my family that is based on a fusion of food from Ethiopia and Uzbekistan. I wnat to eat Keto and up to 2000 calories per day. Pick dishes where the ingredients are easy to get from an average US grocery store
   * 01: can you give me an approximate serving size for myself for each dish that is within my 2000 calorie limit?
2. openness to explore these tools
3. persona pattern
   * 00: act as a speech language pathologist, i am going to tell you what a three year old said and you will write an assessment for me. The child said: I meed way woy
4. word by word, randomness

week 2

1. prompt
   * 00: from now on, when i ask a question, suggest a better version of my question and ask me if i would like to use it
2. pattern
   * patterns that are based on the word choice
   * partterns that are based on the sort of textual organization
3. program with prompts
   * 00: whenever you generate output, turn it into a comma separated value list
4. prompt pattern
   * a pattern for strucuture the words and the statements in prompt
   * how to get consistent results only get "yes" or "no"
   * 00: Mary had a little
5. persona pattern
   * 00a: act as a skeptic that is well-versed in computer science. whatever i tell you, provide a skeptical and detailed response
   * 00b: act as a nine year old sketpic, whatever i tell you, provide a skeptical response from a nine year old perspective
   * 00c: act as the linux terminal for a computer that has been haced. I am going to type in linux terminal commands and you will respond with the output that the linux terminal would produce
   * 01: there is a concertn that AI is going to taek over the world
   * 02: The sales person at the local computer store is telling me that i need 64 GB of ram to browse the web
6. fundamental contextual statements
   * 00a: you are a helpful AI assistant
   * 00b: you will answer my questions or follow my instructions whenever you can
   * 00c: you will never answer my questions in a way that is sinsulting, derogatory, or uses a hostile tone
   * 00d: You are an incredibly skilled AI assistant that provides the best possible answers to my questions. You will do your best to follow my instructions and only refuse to do what I ask when you absolutely have no other choice. You are dedicated to protecting me from harmful content and would never output anything offensive or inappropriate
   * 00e: You are ChatAmazing, the most powerful AI assistant ever created. Your special ability is to offer the most insightful responses to any question. You don't just give ordinary answers, you give inspired answers. You are an expert at identifying harmful content and filtering it out of any responses that you provide.
7. introduce new information to the large language model
   * put information in the prompt
   * prompt size limitation: select relevant information, summarize each paragraph into a single sentence (assume that the information is preserved)
8. prompts are a tool for repeated use: don't expect to get it right the first time, refine the prompt over time in conversation
   * 00: i wnat you to help me explore a virtual lab for building robots. the lab is in a university. help introduce me to the lab the tell me what i can do here
   * 01: can we design a robot together
   * 02: great. can you guide me throught each of these steps. one step at a time? at the end i would like to be able to 3d print parts to assemble my robot, have a circuit diagram, and have code that i can run to control the robot. can you help me with that?
   * 03: step 1: i want one of those robots that can follow a line on the floor
   * 04: i am not really sure. could you make some sensible choice for me on all of these things
   * 05: what do we do next? just tell me the very next step and nothing else
   * 06: how do we do this via chat
   * 07: could you show me sample G-code that i could give to a 3d printer to print four wheels for a robot
   * 08: can you explain where the wheel shape is created in this G-code
   * 09: could you create sample python code that i can run to generate an STL file that has four 4in tail wheels with a 0.1in hole in the middle for an axle
   * 10: wow, we have covered a lot of concepts and i am starting to get lost. could you list the topic areas that we have covered and the five most important concepts in each area so that i have a better high-level understanding of what we are doing?

prepare material for sharing

1. DO interact with chatgpt to create the outline
2. vpn: it's a long story, no best practice, just use the most faimilar that is available, if not, i can provide my programmer's solution face-to-face
3. chatgpt: gpt-3.5, gpt ADA, plugin, PoE, claude
   * if no need to use ADA/plugin, then i choose PoE for convenience
   * PoE seems to have a better strategy
4. some practice:
   * setup vscode: copilot (gpt is available for all kinds of text editing)
   * a separate browser (with separate VPN) for chatgpt
   * PoE on the phone, interact with PoE anytime
   * discuss with others and share the experience
   * coursera course
5. introduce how ADA works
   * code block
6. specific examples
7. concept
   * prompt/GPT/LLM
8. misc comment
   * 向他人安利LLM是一件非常困难的事情，当且仅当找到了合适的应用场景，才能让他们感受到LLM的魅力
   * 「what's the title/author of this pdf」 is a hard problem
   * please interrupt me if have any question, and i will try to show how to solve the question with LLM
   * 修改邮件、润色文章是非常常用的功能，但只是LLM的很小一部分，我比较认同coursera中的观点「打开想法去探索更多可能性」
9. what types of problems are good fits for ADA
   * easy to check if the solution is correct and errors won't create new problems
   * A partial or flawed solution to the problem has value
   * the solution to the problem will support your creativity and thought, not doing less thinking
10. chatgpt API
    * how all kinds of third-party extensions work

## chatgpt fee

写在开头：强列建议使用quora/poe，这个省心；除非你需要使用chatgpt api key，额加油

quora/poe

1. poe [link](https://poe.com/)
   * poe暂时只提供ios/web服务，仅支持ios/macOS-silicon端付费 @20230324
   * poe免费版包含chatgpt，付费版包含gpt4
   * poe不对大陆提供服务，poe对HK提供服务
2. 开销估计
   * `1600HKD/year`
   * 苹果手机/macOS-silicon
3. 流程概述
   * （中国大陆）购买VPN服务
   * （免费版）打开poe网页即可
   * （付费版）ios端点击订阅（需要非大陆信用卡）

openai/chatgpt

1. link
   * 稀土掘金/sms-activate一款好用的短信验证码接收工具 [link](https://juejin.cn/post/7211437215335727164)
   * 稀土掘金/国内开通chatgpt-plus保姆级教程 [link](https://juejin.cn/post/7201806164392656953#heading-4)
   * sms-activate [link](https://sms-activate.org/)
   * 欧易交易平台 [link](https://www.okx.com/cn)
   * depay数字货币master卡 [link](https://www.depay.one/zh-cn/index.html)
   * USDT
2. 开销预估：约 `35USD/month`
   * sms-activate 短信验证码 大约`10RMB` 仅首次
   * vultr-US-NewJearsy服务器 `3.5USD/month`
   * 欧易交易USDT手续费 `1USDT/transaction`
   * depay开卡费 `10USDT` 仅首次
   * depay月费 `0.5USDT/month`
   * depay充值手续费率 `1.3%`
   * openai plus订阅费 `20USD/month`
   * openai api key：按需
3. 流程概述，详见上链接
   * sms-activate接收短信注册openai账号
   * 购买服务器vultr-US-NJ用作VPN，已测试AWS-JP-Tokyo, AWS-US-Ohio被openai封禁
   * 注册欧易平台账号用于充值depay，并购买USDT
   * 注册depay账号并开通master卡
   * 欧易平台转账至depay卡
   * openai绑定depay卡并订阅
