        sorted_list = sorted(people, key=lambda x: x[2])
        formatted = [f(i) for i in sorted_list]
        return formatted