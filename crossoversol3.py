from collections import defaultdict, deque

def solution(queries):
    database = {}
    modification_counts = defaultdict(int)
    locks = defaultdict(lambda: {"locked_by": None, "queue": deque()})
    results = []

    def set_or_inc(key, field, value, caller_id=None):
        # Check lock status
        if key in locks and locks[key]["locked_by"] is not None and locks[key]["locked_by"] != caller_id:
            if key in database and field in database[key]:
                return str(database[key][field])
            return ""
            
        if key not in database:
            database[key] = {}
        
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
            return "acquired"
        locks[key]["queue"].append(caller_id)
        return "wait"

    def unlock(key):
        if key not in database:
            if key in locks and locks[key]["locked_by"] is not None:
                locks.pop(key)
                return "released"
            return "invalid_request"
        
        if locks[key]["locked_by"] is None:
            return ""
        
        locks[key]["locked_by"] = None
        if locks[key]["queue"]:
            next_caller = locks[key]["queue"].popleft()
            locks[key]["locked_by"] = next_caller
        return "released"

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

    return results