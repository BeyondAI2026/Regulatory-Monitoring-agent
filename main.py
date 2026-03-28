from github import Agent, Task, Crew

# Agents
scraper = Agent(
    role="Scraper",
    goal="Find latest UGC and AICTE updates",
    backstory="Expert in Indian regulatory updates",
    verbose=True
)

summarizer = Agent(
    role="Summarizer",
    goal="Summarize regulatory updates clearly",
    verbose=True
)

impact = Agent(
    role="Impact Analyst",
    goal="Explain impact on EdTech business",
    verbose=True
)

memo = Agent(
    role="Memo Writer",
    goal="Write weekly compliance memo",
    verbose=True
)

# Tasks
task1 = Task(description="Find latest UGC and AICTE updates", agent=scraper)
task2 = Task(description="Summarize updates into bullet points", agent=summarizer)
task3 = Task(description="Explain impact on courses, marketing, and data", agent=impact)
task4 = Task(description="Write final memo: what changed and what to do", agent=memo)

# Crew
crew = Crew(
    agents=[scraper, summarizer, impact, memo],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

result = crew.kickoff()
print(result)
