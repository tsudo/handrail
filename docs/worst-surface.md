# Take the worst surface, not the average

Every question in Three Surfaces is rated Low, Medium, High or Severe. The tool's tier is the worst of those ratings. No averaging.

## Why not average

Averaging hides the thing that hurts you. A writing assistant that is harmless on thirteen questions but trains on everything you paste into it is not a "mostly low" tool. It is a tool that puts your clients' information into someone else's model. One Severe answer makes the use case Severe, and that is where the conversation starts.

This feels conservative. It is meant to. Most tools score Low or Medium on every question, and for those the worst-rating rule changes nothing. The rule only bites when one answer is genuinely bad, which is exactly when you want it to.

## The one combination that is always Severe

Some risks only show up in combination. The clearest is the **lethal trifecta**: a tool that

1. holds sensitive information,
2. reads content that someone outside your organization wrote, and
3. can put content where that outsider can see it, such as replying to them, emailing out, posting, or fetching a link it was given.

Any one of these is manageable. Together they are how AI tools are tricked into leaking data: the outsider writes instructions into the content, the tool follows them, and the tool sends the sensitive information back. Three Surfaces rates the trifecta Severe unless one leg is broken by design. A support assistant that can only see the account of the customer it is talking to has nothing else to leak; that breaks a leg. So does switching off web browsing and link previews in a chat assistant. A leg counts as broken only when you can point to the setting, the code or the contract term that breaks it, and the tool is rated as it is actually configured: switch the setting back on and it is Severe again.

## Unknown is worst

If nobody can answer a question yet, rate it at the worst it could plausibly be and mark the result provisional. This is not pessimism. It turns every unknown into a question with an owner. The vendor's own contract terms for your plan count as an answer; their marketing pages do not.

## What the tier decides

The tier decides who approves the tool, how quickly, and how often it is reviewed. At a small firm, Low is "allow," Medium is "allow with conditions," High is "the owner decides in writing," and Severe is "not without a written, time-limited exception." Larger organizations route High to a committee and Severe to an executive.

Next: [place AI by what it may do](function-ladder.md).

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
