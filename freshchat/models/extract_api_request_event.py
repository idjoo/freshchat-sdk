from enum import Enum


class ExtractApiRequestEvent(str, Enum):
    AGENT_ACTIVITY = "Agent-Activity"
    AGENT_INTELLIASSIGN_ACTIVITY = "Agent-Intelliassign-Activity"
    CONVERSATION_AGENT_ASSIGNED = "Conversation-Agent-Assigned"
    CONVERSATION_CREATED = "Conversation-Created"
    CONVERSATION_GROUP_ASSIGNED = "Conversation-Group-Assigned"
    CONVERSATION_RESOLUTION_LABEL = "Conversation-Resolution-Label"
    CONVERSATION_RESOLVED = "Conversation-Resolved"
    CSAT_SCORE = "CSAT-Score"
    FIRST_RESPONSE_TIME = "First-Response-Time"
    MESSAGE_SENT = "Message-Sent"
    RESOLUTION_TIME = "Resolution-Time"
    RESPONSE_TIME = "Response-Time"

    def __str__(self) -> str:
        return str(self.value)
