# Week 13: Tool Use and Function Calling

Back to [Phase 2](../README.md)

## Goal

Learn how to let models take structured actions through software interfaces instead of only producing text.

This week is where your AI systems begin to interact with the outside world deliberately.

## Why This Week Matters

Many useful AI systems are not pure text-generation systems. They need to:

- look things up
- run a calculation
- search internal data
- call application APIs
- fetch current state
- produce structured decisions

Tool use is one of the main reasons modern model APIs feel application-native rather than chatbot-native.

If you understand tool use well, you can build:

- research assistants
- support agents
- workflow automations
- internal copilots
- app features that act, not just answer

## Week 13 Outcomes

By the end of this week, you should be able to:

- define tool schemas clearly
- understand how tool selection works conceptually
- execute tool-result loops safely
- distinguish provider-hosted tools from custom client-side functions
- log and inspect tool calls
- build one tool-enabled assistant with at least three tools

## What To Learn

## 1. Tool-use mental model

Tool use is a structured interface between model reasoning and software actions.

The basic loop is:

1. model reads the user goal
2. model decides whether it needs a tool
3. model emits a structured tool call
4. your application executes the tool
5. tool output is returned to the model
6. model continues or answers

This is more reliable than asking the model to pretend it has done something.

## 2. Tool schemas and function interfaces

You should learn how to define:

- tool name
- description
- parameter schema
- required fields
- field types

Important rule:

Tool schemas are part of prompt engineering and application design at the same time.

Weak tool schemas lead to:

- vague arguments
- validation issues
- wrong tool choice

## 3. Tool choice and boundaries

The model should not have unlimited authority.

You need to think about:

- which tools exist
- which tasks each tool is allowed to perform
- which tool results are trustworthy
- when a human should review before action

This matters because tool use increases system power and therefore system risk.

## 4. Client tools vs hosted tools

Study the distinction:

- custom client-side functions that your application executes
- provider-hosted tools such as file search, web search, code tools, or remote MCPs where supported

You should understand the engineering tradeoff:

- hosted tools reduce implementation work
- custom tools give you tighter control

## 5. Validation and execution safety

Tool use should be treated like a boundary crossing.

You need to validate:

- tool arguments
- access scope
- preconditions
- failure responses

Good rule:

- never assume the model's arguments are always safe or correct

## 6. Logging and traces

Once tools are involved, traces become essential.

Track:

- which tool was chosen
- what arguments were requested
- whether validation passed
- what result was returned
- what the model did next

Without this, debugging tool-enabled systems becomes much harder.

## 7. Determinism vs agentic flexibility

Tool systems can be designed with different levels of freedom.

You should think about:

- explicit routing
- model-chosen tool selection
- hybrid approaches

Not every application should let the model choose everything dynamically.

## Best Learning Sequence For This Week

1. tool-use loop
2. schema design
3. validation
4. client vs hosted tools
5. logging and traces
6. tool-enabled assistant build

## Recommended Daily Breakdown

### Day 1: Tool-use concepts

Focus:

- model-to-tool interaction loop
- structured calls vs plain text pretending

### Day 2: Schema design

Focus:

- strong parameter definitions
- tool descriptions
- required fields

### Day 3: Tool execution layer

Focus:

- validate arguments
- call Python functions or API wrappers
- return results cleanly

### Day 4: Hosted vs custom tools

Focus:

- compare platform-native tools with your own function tools

### Day 5: Logging and failure handling

Focus:

- trace tool calls
- inspect bad arguments or wrong choices

### Day 6: Build the assistant

Focus:

- connect at least three tools
- support multiple user questions

### Day 7: Review and document limits

Focus:

- when tool use helped
- where guardrails are still weak

## Build Plan

Build one assistant with at least three tools.

Good starter tools:

- calculator
- internal note search
- current weather or public info lookup
- task or ticket lookup from a local data source

Requirements:

- tool schemas
- validation
- execution logs
- readable final answer generation

## Deliverables

- one tool-enabled assistant
- tool call logs or trace output
- short note on client tools vs hosted tools
- one failure case where tool validation prevented a bad action or bad call

## Exit Criteria

- you can define useful tool schemas
- you can safely execute the tool loop
- you can distinguish tool design from general prompt design
- you can inspect and debug tool traces

## Common Mistakes To Avoid

- using vague tool descriptions
- failing to validate arguments
- giving the model access to tools with unclear boundaries
- hiding tool traces so failures become mysterious

## Expert Notes That Matter Early

### Tool use is application design

The tool interface is as important as the prompt.

### Strong tools reduce hallucination pressure

If the model can fetch real data or compute directly, it needs to guess less.

### Logs are not optional once actions exist

You need a record of how the system decided to act.

## Suggested Official References

- Anthropic tool use overview
- OpenAI Responses and tool-calling guidance
- OpenAI hosted tools documentation

## Final Standard For This Week

The correct outcome of Week 13 is not "I made the model call a function."

The correct outcome is:

"I can design safe, inspectable tool interfaces that let a model act through software reliably."
