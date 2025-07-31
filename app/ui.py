"""Creates and configures the Gradio user interface for the application."""

import gradio as gr
from app.agent import get_python_version_info

def create_tutor_response(question, use_context, tutor_instance):
    """Handles the tutor interaction logic."""
    if not tutor_instance:
        return "Tutor is not initialized. Please wait for startup to complete.", ""
        
    answer = tutor_instance.ask_question(question, use_context)
    
    context_info = f"Context Enabled: {use_context}\n"
    context_info += f"History Length: {len(tutor_instance.conversation_history)} items"
    return answer, context_info

def clear_tutor_context(tutor_instance):
    """Clears the tutor's conversation history."""
    if tutor_instance:
        tutor_instance.clear_history()
        return "Context cleared.", "Context Cleared"
    return "Tutor not initialized.", ""

def create_interface(state: dict) -> gr.Blocks:
    """Creates the full Gradio UI with tabs for the tutor and agent."""

    def get_tutor():
        return state.get("python_tutor")
    
    with gr.Blocks(title="Python AI Assistant", theme=gr.themes.Soft()) as interface:
        gr.Markdown("# 🐍 Python AI Assistant")
        # gr.Markdown("Your all-in-one assistant for Python questions and release information.")

        with gr.Tabs():
            # --- Tutor Tab ---
            with gr.TabItem("Python Tutor (RAG)"):
                with gr.Row():
                    with gr.Column(scale=2):
                        question_input = gr.Textbox(
                            label="Your Question",
                            placeholder="e.g., What are Python decorators?",
                            lines=4
                        )
                        context_toggle = gr.Checkbox(
                            label="Remember Conversation History",
                            value=True,
                            scale=1
                        )
                        with gr.Row():
                           submit_btn = gr.Button("Ask Tutor", variant="primary")
                           clear_btn = gr.Button("Clear History")

                    with gr.Column(scale=1):
                        context_info = gr.Textbox(
                            label="Context Info",
                            interactive=False,
                            lines=2
                        )
                        gr.Markdown(
                            "**Sample Questions:**\n"
                            "- What is the difference between a list and a tuple?\n"
                            "- How to define a function in Python?\n"
                            "- How do I handle exceptions in Python?"
                        )

                answer_output = gr.Textbox(
                    label="Tutor's Answer",
                    lines=15,
                    max_lines=20,
                    interactive=False
                )
                
                submit_btn.click(
                    fn=lambda q, u: create_tutor_response(q, u, get_tutor()),
                    inputs=[question_input, context_toggle],
                    outputs=[answer_output, context_info]
                )
                clear_btn.click(
                    fn=lambda: clear_tutor_context(get_tutor()),
                    outputs=[answer_output, context_info]
                )

            # --- MODIFIED Latest Release & Features Agent Tab ---
            with gr.TabItem("Latest Release & Features"):
                gr.Markdown(
                    "### Get Latest Python Release and Major Features\n"
                    "The agent will find the latest Python release and list its top three new features."
                )
                
                # Define the prompt that will be displayed and used
                agent_prompt_text = (
                    "Your task is to find the latest stable Python release and its three major new features. Follow these steps:\n"
                    "1. Use the `python_releases_scraper` tool to identify the single most recent, stable Python version number from the list of found releases.\n"
                    "2. Once you have the version number (e.g., '3.12.4'), use the web search tool to find its three most significant or major new features. Your search query should be specific, like \"Python 3.12 major new features\".\n"
                    "3. Present the final answer clearly, stating the latest version number and then listing the three major features in a bulleted list."
                )

                # Display the prompt in a non-interactive textbox
                agent_prompt_display = gr.Textbox(
                    value=agent_prompt_text,
                    label="Agent Task",
                    lines=5,
                    interactive=False
                )

                # The button to trigger the agent
                agent_button = gr.Button("Get Latest Release Info", variant="primary")
                
                # Output for displaying the agent's report
                agent_output = gr.Markdown(
                    label="Latest Release Report"
                )

                # # Information box to explain what the agent does
                # gr.Markdown(
                #     "**What this agent does:**\n"
                #     "- Scrapes the official Python downloads page to find the latest version.\n"
                #     "- Uses web search to find the three major new features for that version.\n"
                #     "- Returns a formatted report with the findings."
                # )

                agent_button.click(
                    fn=get_python_version_info,
                    inputs=[agent_prompt_display],
                    outputs=[agent_output],
                    api_name="get_latest_release_info"
                )

    print("Gradio UI created.")
    return interface


if __name__ == "__main__":
    # A mock state object is created and passed for standalone testing.
    mock_state = {"python_tutor": None} 
    interface = create_interface(mock_state)
    interface.launch()
