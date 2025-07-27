"""Main entry point for the FastAPI application and Gradio UI."""

from contextlib import asynccontextmanager
import gradio as gr
from fastapi import FastAPI
from app.ui import create_interface
from app.tutor import Tutor

# This dictionary will hold our global objects
state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the application's startup and shutdown events.
    On startup, it initializes the AI Tutor.
    On shutdown, it clears the application state.
    """
    # Runs on startup
    print("Application Startup: Initializing AI Tutor...")
    state["python_tutor"] = Tutor()
    print("AI Tutor Initialized.")
    yield
    # Runs on shutdown
    state.clear()
    print("Application Shutdown: Resources cleared.")

# Create a FastAPI app instance with the lifespan handler
app = FastAPI(lifespan=lifespan)

# Mount the Gradio app on the FastAPI server
app = gr.mount_gradio_app(app, create_interface(state), path="/")

@app.get("/health")
def read_root():
    """A health check endpoint to confirm the API is running."""
    return {"status": "ok"}
