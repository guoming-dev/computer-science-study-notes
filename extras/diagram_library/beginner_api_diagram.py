from diagrams import Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.client import User
from diagrams.onprem.network import Internet
from diagrams.generic.database import SQL

# Create the flowchart diagram
with Diagram("API Flowchart", show=True, outformat="png", direction="TB"):
    user = User("Client App")
    internet = Internet("API Request")
    api_server = Server("API Server")
    database = SQL("Database")
    response = Internet("API Response")

    # Define data flow
    user >> internet >> api_server >> database
    user << response << api_server << database