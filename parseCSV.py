def parseValue(value):
    """Parses string values into floats, otherwise return origin string."""
    try:
        float(value)
        return float(value)
    except:
        return value

def csvToDictArray(file):
    """Parse incoming data set into an array of dictionaries."""
    f = open(file, 'r')
    lines = f.read().split('\n')

    data_set = []
    attributes = lines[0].split(',')                    # List of data attributes.
    valuesPerAttr = {attr: [] for attr in attributes}   # Dictionary of all values per data attribute.

    for idx, line in enumerate(lines):
        if idx > 0:
            item = {}
            row = line.split(',')

            for _idx, attr in enumerate(attributes):
                if len(row) == len(attributes):
                    value = parseValue(row[_idx])

                    item[attr] = value
                    valuesPerAttr[attr].append(value)

            # Only add items with data in it.
            if bool(item):
                data_set.append(item)

    return [data_set, attributes, valuesPerAttr]
