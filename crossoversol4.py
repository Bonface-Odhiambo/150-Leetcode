from collections import defaultdict, deque

def solution(queries):
    database = {}
    modification_counts = defaultdict(int)
    locks = defaultdict(lambda: {"locked_by": None, "queue": deque()})
    # Track record states before locking
    record_states = {}
    # Track records locked by each user
    user_locks = defaultdict(set)
    results = []

    def set_or_inc(key, field, value, caller_id=None):
        if key in locks and locks[key]["locked_by"] is not None and locks[key]["locked_by"] != caller_id:
            if key in database and field in database[key]:
                return str(database[key][field])
            return ""
            
        if key not in database:
            database[key] = {}
        
        # Save state before first modification during lock
        if caller_id and key in locks and locks[key]["locked_by"] == caller_id:
            if key not in record_states.get(caller_id, {}):
                record_states.setdefault(caller_id, {})[key] = {
                    'data': {k: v.copy() if isinstance(v, dict) else v 
                            for k, v in database[key].items()},
                    'count': modification_counts[key]
                }
        
        try:
            if field in database[key]:
                database[key][field] += int(value)
            else:
                database[key][field] = int(value)
        except ValueError:
            database[key][field] = value
          
        modification_counts[key] += 1
        return str(database[key][field])

    def get(key, field):
        if key in database and field in database[key]:
            return str(database[key][field])
        return ""

    def delete(key, field, caller_id=None):
        if key in locks and locks[key]["locked_by"] is not None and locks[key]["locked_by"] != caller_id:
            return "false"
        
        # Save state before first modification during lock
        if caller_id and key in locks and locks[key]["locked_by"] == caller_id:
            if key not in record_states.get(caller_id, {}):
                record_states.setdefault(caller_id, {})[key] = {
                    'data': {k: v.copy() if isinstance(v, dict) else v 
                            for k, v in database[key].items()},
                    'count': modification_counts[key]
                }
        
        if key in database and field in database[key]:
            del database[key][field]
            modification_counts[key] += 1
            if not database[key]:
                del database[key]
                if key in modification_counts:
                    del modification_counts[key]
            return "true"
        return "false"
    
    def lock(caller_id, key):
        if key not in database:
            return "invalid_request"
        if locks[key]["locked_by"] == caller_id or caller_id in locks[key]["queue"]:
            return ""
        if locks[key]["locked_by"] is None:
            locks[key]["locked_by"] = caller_id
            user_locks[caller_id].add(key)
            return "acquired"
        locks[key]["queue"].append(caller_id)
        return "wait"

    def unlock(key):
        if key not in database:
            was_locked = key in locks and locks[key]["locked_by"] is not None
            if key in locks:
                if locks[key]["locked_by"]:
                    user_locks[locks[key]["locked_by"]].discard(key)
                locks.pop(key)
            return "released" if was_locked else "invalid_request"
        
        if locks[key]["locked_by"] is None:
            return ""
        
        current_user = locks[key]["locked_by"]
        user_locks[current_user].discard(key)
        locks[key]["locked_by"] = None
        
        if locks[key]["queue"]:
            next_caller = locks[key]["queue"].popleft()
            locks[key]["locked_by"] = next_caller
            user_locks[next_caller].add(key)
        return "released"

    def undo(caller_id, key):
        if key not in locks or locks[key]["locked_by"] != caller_id:
            return "false"
        
        if key in record_states.get(caller_id, {}):
            saved_state = record_states[caller_id][key]
            if key in database:
                database[key] = saved_state['data'].copy()
            else:
                database[key] = saved_state['data']
            modification_counts[key] = saved_state['count']
            del record_states[caller_id][key]
        
        # Release lock
        user_locks[caller_id].discard(key)
        locks[key]["locked_by"] = None
        if locks[key]["queue"]:
            next_caller = locks[key]["queue"].popleft()
            locks[key]["locked_by"] = next_caller
            user_locks[next_caller].add(key)
            
        return "true"

    def logout(caller_id):
        released_count = 0
        # Release all locks held by user
        for key in list(user_locks[caller_id]):
            if key in locks and locks[key]["locked_by"] == caller_id:
                locks[key]["locked_by"] = None
                released_count += 1
                if locks[key]["queue"]:
                    next_caller = locks[key]["queue"].popleft()
                    locks[key]["locked_by"] = next_caller
                    user_locks[next_caller].add(key)
        
        # Remove from all queues
        for lock_info in locks.values():
            if caller_id in lock_info["queue"]:
                lock_info["queue"].remove(caller_id)
        
        user_locks[caller_id].clear()
        if caller_id in record_states:
            del record_states[caller_id]
        
        return str(released_count)

    def top_n_keys(n):
        sorted_items = sorted(modification_counts.items(), key=lambda item: (-item[1], item[0]))
        output_list = []
        for i in range(min(n, len(sorted_items))):
            key, count = sorted_items[i]
            output_list.append(f"{key}({count})")
        return ", ".join(output_list)

    for query in queries:
        operation = query[0]
        if operation == "SET_OR_INC":
            results.append(set_or_inc(query[1], query[2], query[3]))
        elif operation == "GET":
            results.append(get(query[1], query[2]))
        elif operation == "DELETE":
            results.append(delete(query[1], query[2]))
        elif operation == "TOP_N_KEYS":
            results.append(top_n_keys(int(query[1])))
        elif operation == "SET_OR_INC_BY_CALLER":
            results.append(set_or_inc(query[1], query[2], query[3], query[4]))
        elif operation == "DELETE_BY_CALLER":
            results.append(delete(query[1], query[2], query[3]))
        elif operation == "LOCK":
            results.append(lock(query[1], query[2]))
        elif operation == "UNLOCK":
            results.append(unlock(query[1]))
        elif operation == "UNDO":
            results.append(undo(query[1], query[2]))
        elif operation == "LOGOUT":
            results.append(logout(query[1]))

    return results