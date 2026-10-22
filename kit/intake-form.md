# AI intake form (Level 2)

*Licensed Apache-2.0 (LICENSE-code). Copyright 2026 Jason Robbins; modifications copyright 2026 Keith Crawford. Modified from the AI Intake Form and the internal-build block of the ai-tool-risk-assessment skill in the AI Security Risk Workbook v3.0 by Jason Robbins. Changes: reworded, People and third-party-model questions added, mapped to Three Surfaces. See NOTICE.*

*For anyone asking to use a new AI tool, a new AI feature in a tool we already use, or an AI system we are building. The tool name and what you want it for are the only required answers; the assessor fills the rest from the vendor's documents and asks you only what they can't find.*

**Requested by:** ____________ **Date:** ____________ **Business owner:** ____________

## About the request

| Question | Answer |
| --- | --- |
| Tool or system name, and plan if known | |
| What kind of request is this? (new vendor tool / AI feature added to a tool we use / something we are building) | |
| What will you use it for? | |
| Who will use it, and roughly how many people? | |
| When do you need it? | |

## Information and reach

| Question | Answer (pick the closest) |
| --- | --- |
| What is the most sensitive information that will go in? | Public / Internal / Confidential (client, customer, strategy, code) / Regulated (health, payment, government IDs, minors) / Not sure |
| Who sees what it produces before anyone on our side reviews it? | Just me / my team / the whole company / clients or customers / the public / Not sure |
| Will people act on its output without checking it? | No, always checked / sometimes / usually / it makes the decision itself / Not sure |
| Can it send, post, change or delete anything? | No / with someone approving each action / on its own / Not sure |
| Will it connect to other systems (CRM, email, file storage, code)? | No / yes: which? |
| Will it read content from outside (web pages, inbound email, customer tickets, uploaded files)? | No / yes: which? |

## Documents

| Question | Answer |
| --- | --- |
| Do you already have the vendor's contract, DPA or security documents? | No / yes, attached / yes, but under NDA |
| Is there anything about how we may use these documents (NDA, no-AI clause)? | |

## For internal builds (engineering owner)

| Question | Answer |
| --- | --- |
| Which model and provider, and how is it reached? | |
| Does any data go to a third-party model or AI API? If yes, under which agreement (DPA, zero data retention, BAA)? | No / yes: [provider, agreement] |
| Where is it hosted? | |
| What data sources does it use? | |
| What tools, credentials and permissions does it have? | |
| How does it log, and where do the logs go? | |
| What testing and red-teaming has been done? | |
| Who is the engineering owner, and who runs it day to day (technical owner)? | |
| Planned go-live date | |
