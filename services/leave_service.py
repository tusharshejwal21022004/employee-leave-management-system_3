# Leave service handles leave request submission logic

from models.leave_request import LeaveRequest

leave_cache = {}


def cache_get(employee_id):
    return leave_cache.get(employee_id)


def cache_set(employee_id, leave):
    leave_cache[employee_id] = leave


def submit_leave_request(employee_id, leave_type, start_date, end_date):
    cached_leave = cache_get(employee_id)

    if cached_leave:
        print("Leave fetched from cache")
        return cached_leave

    leave = LeaveRequest(employee_id, leave_type, start_date, end_date)

    cache_set(employee_id, leave)

    print("Leave request submitted and cached")

    return leave