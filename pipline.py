from agents import writer_chain, corrector_chain, search_agent
from rich import print


def run_workflow(query : str) -> dict:
    state = {}
    
    searcher = search_agent()

    search_result = searcher.invoke(
        {"messages": [("user",f"{query}")]}
    )

    state["search_result"] = search_result["messages"][-1].content

    print("\n\n"+"="*50)
    print("======= YOUR SEARCH RESEARCH =======")
    print(state["search_result"])

    writer = writer_chain.invoke({"content": state["search_result"]})
    state["raw_content"] = writer.content

    print("\n\n"+"="*50)
    print("======= YOUR RAW CONTENT =======")
    print(state["raw_content"])

    corrector = corrector_chain.invoke({"data": state["raw_content"]})
    state["final_data"] = corrector.content

    print("\n\n"+"="*50)
    print("======= YOUR FINAL CONTENT =======")
    print(state["final_data"])

    return state


user_input = input("\nEnter your Legal Question: ")
history = run_workflow(user_input)