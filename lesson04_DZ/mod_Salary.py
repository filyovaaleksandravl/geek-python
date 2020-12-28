def calculate(work_hours, m_per_hour, prize):
    try:
        return work_hours * m_per_hour + prize
    except TypeError:
        return
