# Google ADK imports
from google.adk.tools import VertexAiSearchTool
from google.adk.tools.crewai_tool import CrewaiTool

# Third-party tools
from crewai_tools import DallETool

# =============================
# Tool Instantiation
# =============================
# Vertex AI Search Datastore IDs (replace with your actual IDs as needed)

DND_DATASTORE_CHARACTERS_ID = (
    "<your-characters-datastore-id>"
)
DND_DATASTORE_CAMPAIGN_ID = (
    "<your-campaign-datastore-id>"
)

characters_vertex_search_tool = VertexAiSearchTool(
    data_store_id=DND_DATASTORE_CHARACTERS_ID
)
campaign_vertex_search_tool = VertexAiSearchTool(
    data_store_id=DND_DATASTORE_CAMPAIGN_ID
)

dalle_tool = DallETool(
    model="dall-e-3",
    size="1024x1024",
    quality="hd",
    n=1  # number of images to generate
)

adk_dalle_tool = CrewaiTool(
    name="DallE_Images_Creator",
    description="""A tool designed to generate images using the Dall-E model.""",
    tool=dalle_tool
)
