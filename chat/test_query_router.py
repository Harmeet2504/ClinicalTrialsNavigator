from query_router import handle_question

question = "Are there trials for 7-year-olds with glioma in New Jersey?"
results = handle_question(question)

print(f"\n✅ Found {len(results)} matching trials.\n")

for trial in results[:5]:  # Show top 5
    print(trial)