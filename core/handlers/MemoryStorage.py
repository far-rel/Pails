# -*- coding: UTF8 -*-
import uuid

class MemoryStorage(object):

    storage = {}

    def get(self, key, handler):
        session_id = handler.get_secure_cookie('_session_id')
        if session_id and session_id in MemoryStorage.storage and key in MemoryStorage.storage[session_id]:
            return MemoryStorage.storage[session_id][key]
        else:
            return None


    def store(self, key, value, handler):
        session_id = handler.get_secure_cookie('_session_id')
        if session_id:
            if session_id not in MemoryStorage.storage:
                MemoryStorage.storage[session_id] = {}
            MemoryStorage.storage[session_id][key] = value
        else:
            session_id = str(uuid.uuid1())
            handler.set_secure_cookie('_session_id', session_id)
            MemoryStorage.storage[session_id] = {}
            MemoryStorage.storage[session_id][key] = value

    def remove(self, key, handler):
        session_id = handler.get_secure_cookie('_session_id')
        if session_id and session_id in MemoryStorage.storage and key in MemoryStorage.storage[session_id]:
            del MemoryStorage.storage[session_id][key]

    def remove_all(self, handler):
        session_id = handler.get_secure_cookie('_session_id')
        if session_id:
            handler.clear_cookie('session_id')
            if session_id in MemoryStorage.storage:
                del MemoryStorage.storage[session_id]