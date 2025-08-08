def expand_ranges(
    input_str,
    unique_sorted_output=False,
    range_delimiters=None,
    step_delimiter=":",
    output_format="list"
):
    if range_delimiters is None:
        range_delimiters = ["-", "..", "to", "~"]

    result = []
    parts = [p.strip() for p in input_str.split(",") if p.strip()]

    for part in parts:
        if "*" in part:
            base, repeat_str = part.rsplit("*", 1)
            try:
                repeat = int(repeat_str.strip())
            except ValueError:
                raise ValueError(f"Invalid repeat value in: '{part}'")
        else:
            base = part
            repeat = 1

        if step_delimiter in base:
            base, step_str = base.split(step_delimiter)
            try:
                step = int(step_str.strip())
            except ValueError:
                raise ValueError(f"Invalid step value in: '{part}'")
        else:
            step = None

        delimiter_used = next((d for d in range_delimiters if d in base), None)
        if delimiter_used:
            try:
                start_str, end_str = map(str.strip, base.split(delimiter_used))
                start, end = int(start_str), int(end_str)

                if step is None:
                    step = 1

                sign = 1 if end >= start else -1
                expanded = list(range(start, end + sign, step * sign))
            except Exception:
                raise ValueError(f"Invalid range format: '{part}'")
        else:
            try:
                expanded = [int(base.strip())]
            except Exception:
                raise ValueError(f"Invalid number: '{part}'")

        result.extend(expanded * repeat)

    #deduplication
    if unique_sorted_output:
        result = sorted(set(result))

    #output format control
    if output_format == "list":
        return result
    elif output_format == "csv":
        return ",".join(map(str, result))
    elif output_format == "set":
        return set(result)
    else:
        raise ValueError(f"Unsupported output format: '{output_format}'")
