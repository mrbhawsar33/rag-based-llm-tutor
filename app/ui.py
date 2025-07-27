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

    with gr.Blocks(title="Python AI Assistant", theme=gr.themes.Soft()) as user_interface:
        gr.Markdown("# 🐍 Python AI Assistant")
        gr.Markdown("Your all-in-one assistant for Python questions and release information.")

        with gr.Tabs():
            # --- Tutor Tab (No changes here) ---
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

            # --- SIMPLIFIED Latest Releases Agent Tab ---
            with gr.TabItem("Latest Python Releases"):
                gr.Markdown(
                    "### Get Latest Python Releases\n"
                    "The agent will retrieve the most recent Python release versions available."
                )

                # Define the prompt that will be displayed and used
                agent_prompt_text = (
                    "Find and list the latest Python release versions. Present the "
                    "results in a clear, organized format showing the most recent "
                    "Python versions available for download."
                )

                # Display the prompt in a non-interactive textbox
                agent_prompt_display = gr.Textbox(
                    value=agent_prompt_text,
                    label="Agent Task",
                    lines=3,
                    interactive=False
                )

                # The button to trigger the agent
                agent_button = gr.Button("Get Latest Releases", variant="primary")

                # Output for displaying the latest releases
                agent_output = gr.Textbox(
                    label="Latest Python Releases",
                    lines=8,
                    max_lines=12,
                    interactive=False
                )

                # Information box to explain what the agent does
                gr.Markdown(
                    "**What this agent does:**\n"
                    "- Scrapes the official Python downloads page\n"
                    "- Identifies the most recent Python releases\n"
                    "- Uses web search for additional release information if needed\n"
                    "- Returns a clean list of latest version numbers"
                )

                agent_button.click(
                    fn=get_python_version_info,
                    inputs=[agent_prompt_display],
                    outputs=[agent_output],
                    api_name="get_latest_releases"
                )

    print("Gradio UI created.")
    return user_interface

if __name__ == "__main__":
    # A mock state object is created and passed for standalone testing.
    mock_state = {"python_tutor": None}
    interface = create_interface(mock_state)
    interface.launch()
