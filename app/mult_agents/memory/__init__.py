
Usage:
    from mult_agents.memory import MemoryManager
    
    memory = MemoryManager()
    
    # 短期记忆 - 自动通过 State 管理
    state["messages"].append(new_message)
    
    # 长期记忆 - 显式存储
    memory.save_semantic(user_id="user_123", key="preference", value={"theme": "dark"})
    
    # 检索相关记忆
    memories = memory.search_episodic(user_id="user_123", query="之前的分析任务")
"""

from .base import BaseMemory, MemoryType, MemoryEntry
from .short_term import ShortTermMemory, ConversationBuffer
from .long_term import LongTermMemory, SemanticMemoryStore, EpisodicMemoryStore
from .manager import MemoryManager
from .utils import create_memory_checkpoint, extract_memory_from_messages

__all__ = [
    # 基础类型
    "BaseMemory",
    "MemoryType", 
    "MemoryEntry",
    # 短期记忆
    "ShortTermMemory",
    "ConversationBuffer",
    # 长期记忆
    "LongTermMemory",
    "SemanticMemoryStore",
    "EpisodicMemoryStore",
    # 管理器
    "MemoryManager",
    # 工具函数
    "create_memory_checkpoint",
    "extract_memory_from_messages",
]
